# VS Code Workspaces

Of course, everyone has their own beloved editor of choice.
Nevertheless, when working on a project together it might make sense to at least provide some instructions on how to properly configure a common editor for the project.
Especially when one wants to enforce a certain code style and quality.
For instance, VS Code can be configured to invoke the previously discussed tools such as linters, type checkers, and auto formatters to ensure a consistent code style and quality across a project with ease.

With VS Code workspaces, configuring VS Code for a project is straightforward.
The `.code-workspace` file of the workspace can contain settings as well as recommended extensions.
This makes bringing new developers up to speed a breeze because it suffices to simply open the workspace and install the necessary extensions as you did before.
The workspace we are using comes with the following settings:

```json
"settings": {
    "python.linting.flake8Enabled": true,
    "python.linting.mypyEnabled": true,
    "python.formatting.provider": "black",
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

In case of our example project, the recommended extensions are defined by:

```json
"extensions": {
    "recommendations": [
        "bungcip.better-toml",
        "ms-python.vscode-pylance",
        "ms-python.python",
        "streetsidesoftware.code-spell-checker"
    ]
}
```

Within a workspace there can also be multiple *folders*.
In our case there is just one:

```json
"folders": [
    {
        "name": "Momba Tutorial",
        "path": "."
    }
],
```

So, now you know how VS Code workspaces work and how you might use them to ensure consistency across a project and to bring new developers up to speed quickly.
When we will begin working with actual source code, you also know why VS Code may suddenly reformat your code or throw various warning towards you.
In case this annoys you, you now also know how to turn it off. 😉
