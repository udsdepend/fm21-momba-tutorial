# Schedule


## Motivation

Motivate the tutorial by giving a glimpse on the final results and elucidate what the participants will be learning throughout the tutorial.

How do we proceed: We interleave short talks and technical explanations with hands-on sessions. Some of the hands-on sessions will be moderated. In others, the participants will mostly work on their own and can ask questions.


## Getting Started

Setup the project assuming that the participants already prepared their system. This will be moderated. I will do the steps described in the written tutorial myself and the participants should follow along.


## Best Practices

How to set up a Python project for reproducibility and easy collaboration?


### Dependency Management

The participants learn how to manage dependencies with Poetry.

This also covers the development dependencies used by the example (Black, Flake8, and MyPy) and explains their purpose.

This part is moderated: I follow the steps in the written tutorial. 


### VS Code Workspaces

The participants learn how to properly configure a VS Code workspace for easy collaboration: Recommend extensions and configure the environment.

This part is a talk: I explain what is written in the tutorial. The participants do not have to do anything because everything is already pre-configured for them.


### Consistent Code Style

A deeper introduction to Black and Flake8.

Consistent code style following community standards makes collaboration more easy and ensures that code is easily readable.

This part is a talk.


## Running Example

Introduce the *running example* the tutorial is based upon.

This part is a talk explaining the game again but in more detail.


## Model Creation

The participants will learn how to create a model with Momba.

Starts with a talk about JANI models.

The participants will be given a Python file already implementing parts of the model with comments where they need to add stuff, like creating an automaton and adding edges for synchronization. We will go through this skeleton initially.

For the fast ones: Think of possible extensions of the game (e.g., accelerating and decelerating) and implement them.

Ends with a talk about how the reference implementation works. The participants can then continue either with their own implementation or with the reference implementation.


## Model Validation

The participants will learn how to use Momba's state space exploration engine to write an interactive console game based on the model.

Starts with a talk explaining the state space exploration engine.

The participants will be given a Python file already implementing parts of the console game with comments where thy need to add stuff. They have to add dependencies to the `pyproject.toml` requiring the skills learned in *Dependency Management*.

For the fast ones: ?

Ends with a talk about how the reference implementation works.


## Model Analysis

The participants will learn how to use a model checker to analyze their model.

This will be a moderated session, where I explain the APIs that can be used to 

Covers dependency management, the usage of VS Code workspaces to recommend extensions and configure the environment uniformly, a

- Introduction:
    - What is this tutorial about.
    - What will you be learning?
    - How will we proceed?

