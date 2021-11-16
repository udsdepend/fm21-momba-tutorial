# Prepare Your System

```{important}
Please wait until the 18th of November before following these steps. We are still in the process of optimizing them for the tutorial.
```

**We kindly ask you to follow these steps upfront in preparation of the tutorial.**

This page will guide you through the process of setting up your system such that you can follow the tutorial.
To follow along, you have to install [Docker](https://docker.io) and [VS Code](https://code.visualstudio.com).
The following steps have been successfully tested on Windows 10 and Ubuntu 20.04, however, they should analogously apply to your favorite Linux distribution or macOS.
In case you have any questions, join our <a href="https://gitter.im/koehlma/momba?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge"><img alt="Gitter" src="https://badges.gitter.im/koehlma/momba.svg"></a> or send us an email.


## Ubuntu

1. To install and enable Docker run:
    ```
    sudo apt-get install -y docker.io
    sudo systemctl enable --now docker
    sudo groupadd -f docker
    sudo usermod -aG docker $USER
    ```
    This will also add a group `docker` and add the current user to it (required to execute `docker`).
    You may need to logout and login again for the changes to take effect.

    To **pull the Docker image required for the tutorial** run:
    ```
    docker pull mcr.microsoft.com/vscode/devcontainers/python:0-3.9-bullseye
    ```
    This command will download the required image so that it is already present on the day of the tutorial.
    In case Docker is not properly set up, this command will fail.
2. To install VS Code from the official sources run:
    ```
    wget -O /tmp/vscode.deb "https://code.visualstudio.com/sha/download?build=stable&os=linux-deb-x64"
    sudo apt-get install -y /tmp/vscode.deb
    ```
    Note that this will automatically add an APT repository for future automatic updates.


## Windows

1. To install Docker, use the [Docker Desktop](https://www.docker.com/products/docker-desktop) installer without changing any settings.
    
    To **pull the Docker image required for the tutorial** run:
    ```
    docker pull mcr.microsoft.com/vscode/devcontainers/python:0-3.9-bullseye
    ```
    This command will download the required image so that it is already present on the day of the tutorial.
    In case Docker is not properly set up, this command will fail.
2. To install VS Code, use the [official installer](https://code.visualstudio.com/#alt-downloads).
