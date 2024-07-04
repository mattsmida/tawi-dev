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

# Set up a non-root user
RUN useradd -m appuser

# Create necessary directories
RUN mkdir -p /home/appuser/.task /home/appuser/tawi-data

# Set up Taskwarrior config
RUN echo "data.location=/home/appuser/.task" > /home/appuser/.taskrc

# Set correct ownership and permissions
RUN chown -R appuser:appuser /home/appuser && \
    chmod -R 755 /home/appuser

# Switch to non-root user
USER appuser

# Set the working directory in the container
WORKDIR /home/appuser

# Copy the current directory contents into the container
COPY --chown=appuser:appuser . /home/appuser

# Install any needed Python packages
RUN pip3 install --user --no-cache-dir -r /home/appuser/src/requirements.txt

# Taskarrior config
RUN task config confirmation no

# Volumes for persistent data
VOLUME /home/appuser/.task
VOLUME /home/appuser/tawi-data

# Make Python scripts executable
RUN find /home/appuser/src -name "*.py" -exec chmod +x {} + || true

# Start the shell
RUN /bin/bash
