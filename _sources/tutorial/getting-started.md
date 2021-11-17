# Getting Started

To get started, you first have to obtain the example project for the tutorial.

If you have [Git](https://git-scm.com) installed, clone the example project with:
```
git clone https://github.com/udsdepend/fm21-momba-tutorial.git
```
Otherwise, you can also [download the example project as a ZIP file](https://github.com/udsdepend/fm21-momba-tutorial/archive/refs/heads/master.zip).

After cloning the example project or extracting the ZIP file, you find a file `workspace.code-workspace` in the cloned or extracted folder.
This file defines a [VS Code *workspace*](https://code.visualstudio.com/docs/editor/workspaces).
To open the workspace run:
```
code workspace.code-workspace
```
Alternatively, you can also open the workspace from within VS Code: To this end, open the *command palette* by pressing `F1`, type *File: Open Workspace from File*, and hit the enter key:

```{image} ./images/vscode-open-workspace.png
:name: vscode-open-workspace
:scale: 80%
:align: center
```

Then, choose the `workspace.code-workspace` file to open the workspace.

VS Code will now probably ask you whether you trust the authors of the workspace:

```{image} ./images/vscode-workspace-trust.png
:name: vscode-workspace-trust
:scale: 70%
:align: center
```

This is a security precaution because the workspace may configure VS Code to execute arbitrary code on your system.
Please trust the workspace by clicking *Yes, I trust the authors*.

After opening the workspace, VS Code should ask you whether you want to install the *recommended extensions*:

```{image} ./images/vscode-install-extensions.png
:name: vscode-open-workspace
:scale: 80%
:align: center
```

The workspace comes with one recommended extension: [*Remote - Containers*](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers).
This extension allows using a Docker image to specify a reproducible and versioned development environment.
More about that later.
Please click on *Install* to install the recommended extension.

Should VS Code not ask you to install the recommended extensions, you probably have the extension installed already.
To view the recommended extensions of the workspace and check whether they are installed, open the command palette by pressing `F1` and then choose *Extensions: Show Recommended Extensions*.

After installing the *Remote - Containers* extension you have to reopen the workspace within a *development container*.
To this end, open the command palette by pressing `F1` and then choose *Remote-Containers: Reopen in Container*.
This will reload the window, create a Docker container with Python and all relevant tools installed, and then opens the workspace in this container.

After opening the container, VS Code will install some additional extensions into the container.
After installing these extensions, it may prompt you to reload the window:
```{image} ./images/pylance-reload-prompt.png
:name: pylance-reload-prompt
:scale: 60%
:align: center
```
Please hit *Yes* when prompted to reload the window.

On Windows, reloading may result in the following error:
```{image} ./images/windows-reload-error.png
:name: windows-reload-error
:scale: 60%
:align: center
```
This seems to be due to some kind of race condition in VS Code and Docker Desktop for Windows.
Just wait a few seconds and then hit *Retry*.
Afterwards, it should work.

Congratulations, you are now fully prepared for the tutorial. 🎉
