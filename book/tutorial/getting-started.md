# Getting Started

To get started, you first have to obtain the material for the tutorial.

If you have [Git](https://git-scm.com) installed, clone the material with:
```
git clone https://github.com/udsdepend/fm21-momba-tutorial.git
```
Otherwise, you can also [download the material as a ZIP file](https://github.com/udsdepend/fm21-momba-tutorial/archive/refs/heads/master.zip).

After cloning the material or extracting the ZIP file, you find a file `workspace.code-workspace` in the cloned or extracted folder.
This file defines a [VS Code *workspace*](https://code.visualstudio.com/docs/editor/workspaces).
To open the workspace run:
```
code workspace.code-workspace
```
Alternatively, you can also open the workspace from within VS Code: To this end, open the *command palette* by pressing `F1`, type *File: Open Workspace from File*, and hit the enter key:

```{image} ./images/vscode-open-workspace.png
:name: vscode-open-workspace
:align: center
```

Then, choose the `workspace.code-workspace` file to open the workspace.

After opening the workspace, VS Code should ask you whether you want to install the *recommended extensions*:

```{image} ./images/vscode-install-extensions.png
:name: vscode-open-workspace
:align: center
```

The workspace comes with four recommended extensions for spell checking, Python support, and [TOML](https://toml.io/en/) support.
TOML is the file format used to configure a Python project.
More about that later.

Should VS Code not ask you to install the recommended extensions, you probably have them installed already.
To view the recommended extensions of the workspace and check whether they are installed, open the command palette by pressing `F1` and then choose *Extensions: Show Recommended Extensions*.

The workspace also contains settings for the project.

Congratulations, you are now fully prepared for the tutorial. 🎉
