# VS Code

Of course, everyone has their own beloved editor of choice.
Nevertheless, when working on a project together it might make sense to at least provide some instructions on how to properly configure a common editor for the project.
Especially when one wants to enforce a certain code style and quality.
For instance, VS Code can be configured to invoke the previously discussed tools such as linters, type checkers, and auto formatters to ensure a consistent code style and quality across a project with ease.


## Workspaces

Using a `.code-workspace` file you can recommend extensions for a project and also configure VS Code to use them appropriately.
Now, in our case, we are using a Docker container so the workspace configuration is mostly empty.
It merely defines a single folder and that the *Remote - Containers* extension is recommended:

```json
"folders": [
    {
        "name": "FM Racer",
        "path": "."
    }
],
"extensions": {
    "recommendations": [
        "ms-vscode-remote.remote-containers"
    ]
}
```

## Development Containers

Using a Docker image as a development environment, as we do in this tutorial, has a number of advantages and is, as you have seen, pretty easy with VS Code.
First and foremost, a Docker image provides an additional layer of isolation between the host operating system and the development environment.
You can specify precisely which versions of which tools and dependencies should go into the container and thereby also improve reproducibility.
In particular, this reduces “but it worked on my machine” moments, and, when you have to ship an artifact, you already have a Docker container with everything in it.
Furthermore, bringing new developers and colleges up to speed becomes a breeze as they do not have to spend hours configuring their system and installing the necessary tools.
This is all handled by the Docker image.

To use a development container with VS Code, you have to create a file `.devcontainer/devcontainer.json` in which you specify a `Dockerfile` and other parameters of your desired environment:

```json
"name": "Python 3",

"build": {
    "dockerfile": "Dockerfile",
    "context": "..",
    "args": {
        "VARIANT": "3.9-bullseye",
    }
},
```
Here, `context` tells Docker that the root project directory should be the build context for the image and that the `Dockerfile` located in the same directory as `devcontainer.json` should be used.

The `Dockerfile` is very short as we are using one of Microsoft's pre-built images:
```Dockerfile
ARG VARIANT="3.9-bullseye"
FROM mcr.microsoft.com/vscode/devcontainers/python:0-${VARIANT}

RUN pip3 --disable-pip-version-check --no-cache-dir install poetry \
    && rm -rf /tmp/pip-tmp
```

Within `devcontainer.json`, you can also configure VS Code:
```json
"settings": { 
    "python.defaultInterpreterPath": "/usr/local/bin/python",
    "python.linting.flake8Enabled": true,
    "python.linting.mypyEnabled": true,
    "python.formatting.provider": "black",
    "python.terminal.activateEnvironment": true,

    "[python]": {
        "editor.rulers": [
            99
        ],
        "editor.formatOnSave": true
    }
},
```

This enables linting with Flake8, type checking with MyPy, and automatically formats files with Black when they are saved.
It also displays a vertical line in column 99 in the editor indicating the maximal acceptable line length.
For some, this may be annoying at first.
However, it really helps ensuring a consistent code style and quality across a project.
As argued before, this should be a priority, especially in academia.
After a while, you will adapt to the enforced rules and they will become second nature to you.

In addition, you can specify extensions which should be installed:
```json
"extensions": [
    "streetsidesoftware.code-spell-checker",
    "ms-python.vscode-pylance",
    "ms-python.python",
    "bungcip.better-toml",
],
```
Here we install four extensions for spell checking, Python support, and [TOML](https://toml.io/en/) support.
TOML is the file format of the `pyproject.toml` file used to configure a Python project.

So, now you know how Development Containers work and how you might use them to ensure consistency across a project and to bring new developers up to speed quickly.
When we will begin working with actual source code, you also know why VS Code may suddenly reformat your code or throw various warning towards you.
In case this annoys you, you now also know how to turn it off. 😉
