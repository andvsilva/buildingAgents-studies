#!/usr/bin/env bash

# ============================================================
# 🐳 Docker Installation Script (Ubuntu/Debian-based systems)
# ============================================================
#
# This script performs a clean installation of Docker by:
# 1. Removing any conflicting or old container-related packages
#    (docker.io, docker-compose, podman-docker, containerd, etc.)
# 2. Installing required dependencies (curl, certificates)
# 3. Adding Docker’s official GPG key for package verification
# 4. Configuring the official Docker APT repository
# 5. Installing the latest Docker Engine and CLI tools
# 6. Starting the Docker service
#
# Notes:
# - Requires sudo privileges
# - Designed for Ubuntu/Debian systems
# - Ensures installation from Docker's official repository
# ============================================================


# Remove old/conflicting Docker and container-related packages
sudo apt remove -y $(dpkg --get-selections docker.io docker-compose docker-compose-v2 docker-doc podman-docker containerd runc | cut -f1)

# Update package list and install required dependencies
sudo apt update
sudo apt install -y ca-certificates curl

# Create directory for APT keyrings (if it doesn't exist)
sudo install -m 0755 -d /etc/apt/keyrings

# Download Docker’s official GPG key and save it securely
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc

# Set read permissions for the key
sudo chmod a+r /etc/apt/keyrings/docker.asc


# Add Docker’s official repository to APT sources using .sources format
sudo tee /etc/apt/sources.list.d/docker.sources <<EOF
Types: deb
URIs: https://download.docker.com/linux/ubuntu
Suites: $(. /etc/os-release && echo "${UBUNTU_CODENAME:-$VERSION_CODENAME}")
Components: stable
Signed-By: /etc/apt/keyrings/docker.asc
EOF

# Update package index to include Docker repository
sudo apt update

# Install Docker Engine and related components
sudo apt install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

# Start Docker service
sudo systemctl start docker