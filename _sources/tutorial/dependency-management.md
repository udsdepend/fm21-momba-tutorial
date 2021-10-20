# Dependency Management

In academia, *reproducibility* of research is key.
An important aspect of ensuring reproducibility is to precisely capture the dependencies used by a piece of software.
Installing dependencies into the system may lead to conflicts between the dependencies of different projects.
Furthermore, everyone involved in a project may have different versions of the same dependency installed.

We use [Poetry](https://python-poetry.org/) for dependency management.

[PEP 518](https://www.python.org/dev/peps/pep-0518/) partially specifies the format of the `pyproject.toml` file.


Add Momba to your project:
```
poetry add -E engine -E docker momba
```
The `-E` flag enables additional *extras* or features.
The `engine` feature of Momba contains the state space exploration engine we will be using for the interactive game.
The `docker` feature of Momba enables support for running Storm through Docker.

Running this command will add Momba as a dependency in the `dependencies` section of `pyproject.toml`:
```toml
momba = {version = "^0.4.2", extras = ["engine", "docker"]}
```
The caret `^` tells Poetry that we want a version of Momba that is at least `0.4.2` but less than `0.5.0`.
This is used for [semantic versioning](https://semver.org/).
Introducing breaking changes requires increasing the major version.

Note that this may not apply to all parts a library provides.
For instance, Momba provides experimental features that may break existing code anytime.
If you use such features it is best to precisely *pin* the version of the dependency with `==` like so:
```toml
momba = {version = "==0.4.2", extras = ["engine", "docker"]} 
```

Adding Momba also updated the file `poetry.lock`.
This file defines the precise versions that should be used for the *virtual environment* for reproducibility.

When using a version control system, you would commit the `poetry.lock` file alongside the `pyproject.toml` file.
That way, all collaborators an a project will have precisely the same dependencies in the exact versions installed.
