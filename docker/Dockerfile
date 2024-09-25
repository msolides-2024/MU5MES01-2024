FROM ghcr.io/fenics/dolfinx/dolfinx:v0.8.0
ARG TARGETPLATFORM

WORKDIR /tmp/
ENV DEB_PYTHON_INSTALL_LAYOUT=deb_system
ENV DEBIAN_FRONTEND noninteractive
ENV HDF5_MPI="ON"
ENV HDF5_DIR="/usr/local"
ENV PYVISTA_JUPYTER_BACKEND="static"

# Requirements for pyvista
# Requirements for pyvista (gl1 and render1) and jupyterlab (nodejs and curl)
RUN apt-get update && apt-get install -y libgl1-mesa-glx libxrender1 xvfb curl
RUN curl -sL https://deb.nodesource.com/setup_18.x -o nodesource_setup.sh && \
    bash nodesource_setup.sh && \
    apt install nodejs


RUN python3 -m pip install -U setuptools pip pkgconfig

ADD requirements.txt /tmp/requirements.txt
RUN HDF5_MPI=${HDF5_MPI} CC=mpicc HDF5_DIR=${HDF5_DIR} python3 -m pip install  --no-cache-dir -r requirements.txt
RUN python3 -m pip cache purge
ENTRYPOINT []
