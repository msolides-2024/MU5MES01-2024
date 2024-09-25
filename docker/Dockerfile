FROM ghcr.io/jorgensd/dolfinx-tutorial:v0.8.0

ADD requirements.txt /tmp/requirements.txt
RUN HDF5_MPI=${HDF5_MPI} CC=mpicc HDF5_DIR=${HDF5_DIR} python3 -m pip install  --no-cache-dir -r requirements.txt
RUN python3 -m pip cache purge
ENTRYPOINT []
