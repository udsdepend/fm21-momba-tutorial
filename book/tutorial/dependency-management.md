# Dependency Management

In academia, *reproducibility* of research is key.
An important aspect of ensuring reproducibility is to precisely capture the dependencies used by a piece of software.

Using a system like [Poetry](https://python-poetry.org/) for dependency management has many advantages:

- The dependencies of your projects are decoupled and installed into a *virtual environment* on a per-project basis.
    This prevents version conflicts between multiple projects.
- The dependencies of your projects are precisely tracked and you can be sure that everyone in your team has the exact same versions installed reducing *but it works on my machine* moments.
- To ensure reproducibility, you have to track the dependencies anyway.
    Doing so in a well-specified format with tool support makes reproducing your experiments a breeze.
- Your software is already in a format suitable for distribution through package managers.
    In the case of Python, this is [Pip](https://pypi.org/project/pip/) and the [Python Package Index](https://pypi.org).

[PEP 518](https://www.python.org/dev/peps/pep-0518/) partially specifies the format of the `pyproject.toml` file.
This file defines how your project is going to be build and what dependencies in which versions are required.


## `pyproject.toml`

The `pyproject.toml` contains information about your project like its *name*, a short *description*, and a list of *authors*:

```toml
[tool.poetry]
name = "fmracer"
version = "0.0.1"
description = "A tutorial on Momba at FM21."
authors = [
    "Maximilian Köhl <koehl@cs.uni-saarland.de>"
]
license = "MIT"
readme = "README.md"
repository = "https://github.com/udsdepend/fm21-momba-tutorial"
classifiers = [
    "Intended Audience :: Science/Research",
    "License :: OSI Approved :: MIT License",
    "Development Status :: 2 - Pre-Alpha",
    "Operating System :: OS Independent"
]
```

Furthermore, it contains a list of dependencies:
```toml
[tool.poetry.dependencies]
# required Python version
python = "^3.8"

[tool.poetry.dev-dependencies]
black = { version = "^21.9b0", allow-prereleases = true }
flake8 = "^3.7.9"
flake8-bugbear = "^20.1.2"
pep8-naming = "^0.9.1"
mypy = "^0.812"
```

This also specifies which versions of Python are supported.
In this case, `^3.8` says that all Python versions greater or equal to `3.8` and less than `4.0` are supported.
This is very useful in case you are using features of Python only found in newer versions and you want to communicate this to users of your tool or package.
From a reproducibility perspective it prevents someone from running your project with a wrong version of Python leading to all kinds of non-obvious errors.

The `dev-dependencies` are dependencies which are not required for using your tool or package but for development.
In this case, we have `black`, an auto formatter, `flake8` and some related packages for linting, and `mypy`, a type checker.


## Managing Dependencies

As you may have noticed, Momba is not yet a dependency of your project.
To add Momba as a dependency we use `poetry`:
```bash
poetry add -E engine -E docker momba
```
This commands adds Momba as a dependency to your project.

The `-E` flag enables optional *features* for the package to be installed.
The `engine` feature of Momba contains the state space exploration engine we will be using for the interactive game.
The `docker` feature of Momba enables support for running Storm through Docker.

Running this command will add Momba as a dependency in the `dependencies` section of `pyproject.toml`:
```toml
momba = {version = "^0.4.2", extras = ["engine", "docker"]}
```
The caret `^` tells Poetry that we want a version of Momba that is at least `0.4.2` but less than `0.5.0`.
This is used for [semantic versioning](https://semver.org/).
Introducing breaking changes requires increasing the major version.
Hence, it documents a minimal and a maximal version.
Again, specifying a version like that enables reproducibility.

In addition to adding Momba to the `pyproject.toml` the command also updated the `poetry.lock` file.
This file contains precise versions of each dependency including transitive dependencies that should be used for development and reproducing results.
It even contains cryptographic hashes of the respective dependencies to further ensure reproducibility, or, at least make it obvious, when the required file has been modified or is not available.

In case you are using experimental features of a dependency which are not subject to semantic versioning, it can make sense to also *pin* the version of a dependency like so:
```toml
momba = {version = "==0.4.2", extras = ["engine", "docker"]} 
```
In case you make any manual changes to the `pyproject.toml` file run
```
poetry lock
```
to synchronize them into the `poetry.lock` file.

When using a version control system, you would commit the `poetry.lock` file alongside the `pyproject.toml` file.
That way, all collaborators an a project will have precisely the same dependencies in the exact versions installed.


## Virtual Environments

To install a virtual environment containing all the dependencies run:
```bash
poetry install
```
This will create a directory `.venv` containing a copy of your local Python interpreter and an installation of all and only the specified dependencies.
For reproducibility, the precise versions are taken from the `poetry.lock` file.

In case you are using VS Code, press `F1` to open the command palette and choose *Python: Select Interpreter*.
Then choose *Entire Workspace*.
You can now select the recommended interpreter from the virtual environment.