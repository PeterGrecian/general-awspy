FROM mcr.microsoft.com/devcontainers/base:ubuntu

# Install AWS CLI, unzip, curl, Python and boto3
RUN apt-get update && \
    apt-get install -y unzip curl python3-pip zoxide && \
    curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" && \
    unzip awscliv2.zip && \
    ./aws/install && \
    rm -rf awscliv2.zip aws/ && \
    pip3 install boto3

# Optionally: Clean up cached package lists for smaller image
RUN rm -rf /var/lib/apt/lists/*
RUN echo 'eval "$(zoxide init bash)"' >> /etc/bash.bashrc
