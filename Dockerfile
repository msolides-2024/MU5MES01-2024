FROM ghcr.io/fenics/dolfinx/lab:v0.8.0

# create user with a home directory
ARG NB_USER
ARG NB_UID=1000
ENV USER ${NB_USER}
ENV HOME /home/${NB_USER
ENV PYVISTA_JUPYTER_BACKEND="static"

# Requirements for pyvista (gl1 and render1) and jupyterlab (nodejs and curl)
RUN apt-get update && apt-get install -y libgl1-mesa-glx libxrender1 xvfb curl
RUN curl -sL https://deb.nodesource.com/setup_18.x -o nodesource_setup.sh && \
    bash nodesource_setup.sh && \
    apt install nodejs

# Upgrade setuptools and pip
RUN python3 -m pip install -U setuptools pip pkgconfig
ADD pyproject.toml /tmp/pyproject.toml
RUN python3 -m pip install --no-cache-dir --no-binary=h5py -v .
RUN python3 -m pip cache purge
RUN jupyter lab build
RUN pip install -r requirements.txt

# Copy home directory for usage in binder
WORKDIR ${HOME}
COPY . ${HOME}
USER root
RUN chown -R ${NB_UID} ${HOME}

USER ${NB_USER}
ENTRYPOINT []
