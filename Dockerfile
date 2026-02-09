FROM python:3.11-slim

# Build-time arguments (used only during docker build)
ARG GIT_REPO=https://github.com/vivek-co/python-scripts-repo.git
ARG GIT_BRANCH=main

# Set working directory
WORKDIR /home/Vivek

# Install git
RUN apt-get update && \
    apt-get install -y git && \
    rm -rf /var/lib/apt/lists/*

# Clone code from GitHub into /home/Vivek
RUN git clone -b ${GIT_BRANCH} ${GIT_REPO} .

# Default runtime environment variables
ENV NUM1=10 \
    NUM2=5 \
    USERNAME=DefaultUser \
    CITY=India

# Fix runtime to python, script chosen at docker run
ENTRYPOINT ["python"]

