---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# Getting Started




### During the Tutorial

1. If you have [Git](https://git-scm.com/) installed, clone the material for the tutorial:
    ```
    git clone https://github.com/udsdepend/fm21-momba-tutorial.git
    ```
    Otherwise, you can also [download the material as a ZIP file](https://github.com/udsdepend/fm21-momba-tutorial/archive/refs/heads/master.zip).

After cloning the material or extracting the ZIP file, you find a file `workspace.code-workspace` in the cloned or extracted folder.
This file defines a VS Code *workspace*.
To open the workspace run:
```
code workspace.code-workspace
```
Alternatively, you can also open the workspace from the UI: To this end, open the *command palette* by pressing `F1`, type *File: Open Workspace from File*, and hit enter:
```{image} ./images/workspace-from-file.png
:name: workspace-from-file
:align: center
```

Then, choose the `workspace.code-workspace` file to open the workspace.


This folders should contain a file `pyproject.toml`.
Please make sure to open the right folder as otherwise the following steps won't work.




```{code-cell} ipython3
from momba import model

ctx = model.Context(model.ModelType.MDP)

print(ctx)
```