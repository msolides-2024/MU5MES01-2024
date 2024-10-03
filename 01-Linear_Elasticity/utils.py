import mpi4py
import numpy as np
import dolfinx # FEM in python
from dolfinx import fem, io, mesh, plot, geometry
from typing import Optional
import ufl

def evaluate_at_points(points:np.ndarray, function: fem.Function) -> Optional[np.ndarray]:
    """
    Evaluate the `function` at all `points`.

    Note:
        It is assumed that `points` is the same on all processes.

    Note:
        Values are only returned on process 0.
    """
    mesh = function.function_space.mesh
    comm = mesh.comm
    if comm.rank == 0:
        input_points = points.T
    else:
        input_points = np.empty((0, 3), dtype=points.dtype)
    src_owner, dest_owner, dest_points, dest_cells = dolfinx.cpp.geometry.determine_point_ownership(mesh._cpp_object, input_points, 1e-6)
    values = function.eval(np.array(dest_points).reshape(-1, 3), dest_cells)
    if comm.rank != 0:
        assert np.allclose(dest_owner, 0)
    gathered_values = comm.gather(values, root=0)
    src_counter = np.zeros(len(np.unique(src_owner)), dtype=np.int32)
    bs = function.function_space.dofmap.bs
    values = np.zeros((input_points.shape[0], bs),dtype=function.x.array.dtype)
    if comm.rank ==0:
        for i, owner in enumerate(src_owner):
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
    