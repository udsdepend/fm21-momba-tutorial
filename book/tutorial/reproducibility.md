# Reproducibility

Developing software in an academia setting comes with its own set of challenges.
Most prominently, experiments conducted and presented in papers should be *reproducible* by other researchers.
This is also the reason why most conferences strongly encourage the submission of artifacts with papers.

Setting up a Python project with reproducibility in mind will make your life much easier down the road when it comes to submitting artifacts or onboarding new developers.
For our example project, we are using [Poetry](https://python-poetry.org/) to manage the project in a way such that reproducibility becomes effortless.


## Virtual Environments

A key to reproducibility is to clearly define an execution environment and prevent user and system-specific circumstances from creeping into it.
The execution environment has to be mostly isolated from the existing system of the user.
With [virtual environments](https://docs.python.org/3/tutorial/venv.html), Python has such isolation builtin.
Poetry will manage a virtual environment for you project.
To **set up a virtual environment for the example project**, run
```bash
poetry install
```
in the project folder.
This command will create a new directory `.venv` containing the virtual environment.
That is, a copy of the Python interpreter and all tools and dependencies necessary for the project.

Assuming you have opened the project workspace (see [*Getting Started*](getting-started) for instructions on how to do that), you activate the virtual environment in VS Code as follows:
Press `F1` to open the command palette and choose *Python: Select Interpreter*.
Then choose *Entire Workspace*.
You can now select the recommended interpreter:

```{image} ./images/vscode-select-interpreter.png
:name: vscode-select-interpreter
:align: center
```

VS Code may also prompt you by itself when it recognizes that a virtual environment has been created.

So, how do you manage this virtual environment with Poetry?


## Dependency Management

[PEP 518](https://www.python.org/dev/peps/pep-0518/) partially specifies the format of a `pyproject.toml` file.
This file defines how your project is going to be build and what dependencies in which versions are required.

The dependencies are specified in the `tool.poetry.dependencies` section.
For our example:
```toml
[tool.poetry.dependencies]
# required Python version
python = "^3.8"
```
Currently, this specifies that a Python version of at least 3.8 but less than 4.0 is needed which is indicated by the caret `^`.
The version 4.0 might include backwards incompatibilities, hence, the version should be less than 4.0.
Also, we are using features introduced with Python 3.8, so, the version should be at least 3.8.

As you may have noticed, Momba is not yet a dependency of the project.
To **add Momba as a dependency** run:
```bash
poetry add -E engine momba
```

Running this command will add Momba as a dependency to the `pyproject.toml` file:
```toml
momba = {version = "^0.4.2", extras = ["engine", "docker"]}
```

The `-E` flag enables optional *extras* for the package to be installed.
The `engine` extra of Momba contains the state space exploration engine we will be using for the interactive model visualization.

Again, the caret `^` in `^0.4.2` specifies that we want a version of Momba that is at least `0.4.2` but less than `0.5.0`.
Introducing breaking changes requires increasing the minor version (i.e., `4` to `5` in this case) when the version number starts with `0` as is the case here.
This kind of guaranteeing compatibility between versions is known as [*semantic versioning*](https://semver.org/).
Note that *experimental features* are often excluded from semantic versioning and sometimes compatibility is broken by accident without changing the version number accordingly.
For these cases, it might make sense to explicitly *pin* a precise version with `==` like so:
```toml
momba = {version = "==0.4.2", extras = ["engine", "docker"]} 
```

Adding a dependency with `poetry add` also modifies the `poetry.lock` file.
This file keeps track of the precise versions needed for reproducibility and development.
Running `poetry install` will not install just any versions compatible with the specification in `pyproject.toml` but instead *the precise versions locked* in `poetry.lock`.
In case you make any manual changes to the `pyproject.toml` file run
```
poetry lock
```
to synchronize them into the `poetry.lock` file.
The `poetry.lock` file even contains cryptographic hashes for all dependencies including transitive ones such that any problems with mismatching packages will become apparent when creating the virtual environment with `poetry install`.
When using a version control system, you should commit the `poetry.lock` file alongside the `pyproject.toml` file.
That way, all collaborators an a project will have precisely the same dependencies in the exact same versions installed.

This mechanism of *locking dependencies* ensures that everyone trying to reproduce your experiments gets the exact same versions you used for running the experiments.
By installing the dependencies with `poetry install` into a virtual environment, interferences with the system of the user are minimized.
Also, onboarding new developers becomes very easy because it usually suffices to run `poetry install` to get a working development environment.
In short, using a tool like Poetry makes reproducibility effortless.


## Project Information

In addition to the dependencies, the `pyproject.toml` file also contains additional metadata about your project.
For instance, its *name*, a short *description*, or a list of *authors*.
For the example:
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
This information makes your project compatible with the wider Python ecosystem.
In particular, your project is in a format suitable for distribution through [Pip](https://pypi.org/project/pip/) and the [Python Package Index](https://pypi.org).
This allows others to use your project by adding it to their project with `poetry add` just like you did with Momba.


## Development Dependencies

In addition to the normal dependencies we have specified, *development dependencies* can also be specified in the `pyproject.toml` file.
This is useful for tools that are not required to *use* your project but to *contribute* to it.
In case of our example project there are five development dependencies:
```toml
[tool.poetry.dev-dependencies]
black = { version = "^21.9b0", allow-prereleases = true }
flake8 = "^3.7.9"
flake8-bugbear = "^20.1.2"
pep8-naming = "^0.9.1"
mypy = "^0.812"
```
These are the auto formatter [Black](https://github.com/psf/black), the linter [Flake8](https://flake8.pycqa.org/en/latest/) with some plugins, and the type checker [MyPy](http://mypy-lang.org/).
These tools are used to ensure a consistent code style and quality.
More on that in the next section.