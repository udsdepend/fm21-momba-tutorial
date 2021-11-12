# Consistent Code Style

Let us approach this potentially controversial topic with a quote by Donald Knuth:

> “Let us change our traditional attitude to the construction of programs: Instead of imagining that our main task is to instruct a *computer* what to do, let us concentrate rather on explaining to *human beings* what we want a computer to do.”
>
> — Donald Knuth, *Literate Programming*, The Computer Journal 27, 1984

Programs are usually much more often read than written and, especially in academia, we should think of them as artifacts “explaining to *human beings* what we want a computer to do.”
A well-written and documented reference implementation accompanying a paper about a novel algorithm is as valuable as, or even more valuable than, the paper describing the actual algorithm.
In the best case, the implementation “explains to human beings” how the algorithm solves the problem in a clear, precise, and concrete way.
Therefore, an implementation accompanying a paper should not just be a quick and dirty hack to get it done and conduct some benchmarks but instead be crafted with the same scientific care and passion with which the paper itself is written.

A *consistent code style and quality* makes reading and understanding programs much easier.
Especially when following established *community standards*, it reduces cognitive load such that the reader can focus on the important aspects of the implementation.
Just like a paper with bad typography and grammar is difficult and annoying to read, a program with bad formatting and inconsistent or unusual use of the programming language is difficult and annoying to read.
In both cases, the bad style occludes the relevant details and induces cognitive strain keeping the reader busy with irrelevant ballast.

Fortunately, for many programming languages there are established community standards and even tools which will help you adhere to these standards.
Python is no exception here.
With [Black](https://github.com/psf/black) the [Python Software Foundation](https://www.python.org/psf/) provides a tool to automatically format your code according to a well-established standard.
With [Flake8](https://flake8.pycqa.org/en/latest/) a linter is available which will help you catch bugs and in general produce higher quality code following the official [PEP 8 – Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/).
Like you would not write a paper without a spell checker, you should not write Python programs without using those (or similar) tools.

Since [version 3.5](https://docs.python.org/3.5/whatsnew/3.5.html#whatsnew-pep-484), Python officially supports *gradual static typing*.
Despite being optional, using static types can reduce bugs in your code and also serve as a documentation of interfaces.
There are, however, some tradeoffs to static types and they may not be suited for all use cases as they only work for a subset of Python.
Momba is almost fully statically typed.
The example project comes with the type checker [MyPy](http://mypy-lang.org/) enabled, however, it is configured such that you do not have to provide types for the code you will be writing.

Note that by using the provided VS Code workspace, VS Code is already configured to highlight violations of the Python style guidelines and format your code automatically.
In the next section, we will have a look how this is done and how you can leverage VS Code workspaces for your projects.
