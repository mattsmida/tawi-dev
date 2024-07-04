# Use Ubuntu as base image for better compatibility
FROM ubuntu:20.04

# Avoid prompts from apt
ENV DEBIAN_FRONTEND=noninteractive

# Install tools
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    vim \
    taskwarrior \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app

# Set the working directory in the container
WORKDIR /app

# Install any needed Python packages
RUN pip3 install --no-cache-dir -r requirements.txt

# Set up a non-root user
RUN useradd -m appuser
USER appuser

# Create a basic TaskWarrior config file
RUN mkdir -p /home/appuser/.task && \
    echo "data.location=/home/appuser/.task" > /home/appuser/.taskrc

# Set up TaskWarrior config
RUN task config confirmation no

# Make Python scripts executable
RUN find /app/app -name "*.py" -exec chmod +x {} + || true

# You might want to set an entrypoint script here
# ENTRYPOINT ["/app/entrypoint.sh"]

# Or you can specify a default command
CMD ["/bin/bash"]
