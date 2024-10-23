import mpi4py
import numpy as np
import dolfinx # FEM in python
from dolfinx import fem
from typing import Optional
import ufl
import typing
def evaluate_at_points(points:np.ndarray|typing.Sequence, function: fem.Function) -> Optional[np.ndarray]:
    """
    Evaluate the `function` at all `points`.

    Note:
        The points `p0,p1,..` should be ordered as `p0_x, p1_x, ..., p0_y, p1_y, ... p0_z, p1_z, ...`.

    Note:
        It is assumed that `points` is the same on all processes.

    Note:
        Values are only returned on process 0.
    """
    mesh = function.function_space.mesh

    if isinstance(points, list):
        points = np.array(points)
    if len(points.shape) == 1:
        if points.size < 3:
            # Pad point with zeros
            _points = np.zeros((3,1), dtype=mesh.geometry.x.dtype)
            _points[:len(points),0] = points
        else:
            if len(points) % 3 != 0 and mesh.geometry.dim == 2:
                # Pad points with extra 0
                _points = np.zeros((3, len(points)//2), dtype=mesh.geometry.x.dtype)
                _points[:2, :] = np.array(points).reshape(2, -1)
            elif len(points) % 3 == 0:
                _points = np.zeros((3, len(points)//3), dtype=mesh.geometry.x.dtype)
                _points[:, :] = np.array(points).reshape(3, -1)
            else:
                raise RuntimeError("Received list of points that cannot be formatted as a (n, 3) array")
    else:
        _points = np.array(points, dtype=mesh.geometry.x.dtype)        

    comm = mesh.comm
    if comm.rank == 0:
        input_points = _points.T
    else:
        input_points = np.empty((0, 3), dtype=points.dtype)

    src_owner, dest_owner, dest_points, dest_cells = dolfinx.cpp.geometry.determine_point_ownership(mesh._cpp_object, input_points, 1e-6)
    values = function.eval(np.array(dest_points).reshape(-1, 3), dest_cells).reshape(-1, function.function_space.dofmap.bs)
    if comm.rank != 0:
        assert np.allclose(dest_owner, 0)
    gathered_values = comm.gather(values, root=0)
    src_counter = np.zeros(len(np.unique(src_owner)), dtype=np.int32)
    bs = function.function_space.dofmap.bs
    values = np.zeros((input_points.shape[0], bs),dtype=function.x.array.dtype)
    if comm.rank ==0:
        for i, owner in enumerate(src_owner):
            if owner == -1:
                print(f"Could not find point in mesh for {input_points[i]}")
                continue
            values[i] = gathered_values[owner][src_counter[owner]]
            src_counter[owner] += 1
    else:
        return None    
    return values


def assemble_scalar(J: ufl.form.Form | dolfinx.fem.Form) -> np.floating | np.complexfloating:
    """Assemble a scalar form and gather result across processes

    Args:
        form: The form to assemble.

    Returns:
        The accumulated value of the assembled form.
    """
    compiled_form = dolfinx.fem.form(J)
    if (rank := compiled_form.rank) != 0:
        raise ValueError(f"Form must be a scalar form, got for of arity {rank}")
    local_result = dolfinx.fem.assemble_scalar(compiled_form)
    return compiled_form.mesh.comm.allreduce(local_result, op=mpi4py.MPI.SUM)
    