# Prepare Your System

**We kindly ask you to follow these steps upfront in preparation of the tutorial.**

This page will guide you through the process of setting up your system such that you can follow the tutorial.
To follow along, you have to install [Docker](https://docker.io) and [VS Code](https://code.visualstudio.com).
The following steps have been successfully tested on Windows 10 and Ubuntu 21.10, however, they should analogously apply to your favorite Linux distribution or macOS.
In case you have any questions, join our <a href="https://gitter.im/koehlma/momba?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge"><img alt="Gitter" src="https://badges.gitter.im/koehlma/momba.svg"></a> or send us an email.


## Windows

1. To install Docker, use the [Docker Desktop](https://www.docker.com/products/docker-desktop) installer without changing any settings.
    This may require restarting your computer.
    Please make sure to have the windows features [*Windows Subsystem for Linux* and *Virtual Machine Platform* (for Windows Home) or *Hyper-V* (for Windows Pro) enabled](https://docs.docker.com/desktop/windows/troubleshoot/#virtualization).
    In case you run into any problems checkout the [Docker Troubleshooting Guide](https://docs.docker.com/desktop/windows/troubleshoot/) or send us an email. 
2. To **pull the Docker image required for the tutorial** run in a PowerShell:
    ```
    docker pull mcr.microsoft.com/vscode/devcontainers/python:0-3.9-bullseye
    ```
    This command will download the required image so that it is already present on the day of the tutorial.
    In case Docker is not properly set up, this command will fail.
3. To install VS Code, use the [official installer](https://code.visualstudio.com/#alt-downloads).


## Ubuntu

1. To install and enable Docker run in the terminal of your choice:
    ```
    sudo apt-get install -y docker.io
    sudo systemctl enable --now docker
    sudo groupadd -f docker
    sudo usermod -aG docker $USER
    ```
    This will also add a group `docker` and add the current user to it (required to execute `docker`).
    You may need to logout and login again for the changes to take effect.

2. To **pull the Docker image required for the tutorial** run:
    ```
    docker pull mcr.microsoft.com/vscode/devcontainers/python:0-3.9-bullseye
    ```
    This command will download the required image so that it is already present on the day of the tutorial.
    In case Docker is not properly set up, this command will fail.
3. To install VS Code from the official sources run:
    ```
    wget -O /tmp/vscode.deb "https://code.visualstudio.com/sha/download?build=stable&os=linux-deb-x64"
    sudo apt-get install -y /tmp/vscode.deb
    ```
    Note that this will automatically add an APT repository for future automatic updates.
