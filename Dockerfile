FROM jupyter/tensorflow-notebook

USER root

# Install Graphviz
RUN apt-get update && \
    apt-get install -y graphviz

RUN pip install graphviz

USER $NB_UID
