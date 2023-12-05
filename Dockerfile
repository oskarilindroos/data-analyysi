FROM tensorflow/tensorflow:latest-gpu-jupyter

USER root

# Install Graphviz
RUN apt-get update && \
    apt-get install -y graphviz

RUN pip install graphviz seaborn scikit-learn