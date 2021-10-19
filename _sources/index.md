# Momba Tutorial

Dealing with quantitative models encompasses a variety of tasks which can be challenging from time to time.
Everything starts with the *construction* of a formal model or a family thereof.
Often a textual or other, more formal, description of the scenario to be modeled already exists, such as a rough sketch of the desired behavior or a circuit diagram.
Then, after a formal model has finally been conceived, one has to *validate* that the model actually adequately represents what should be modeled.
In this regard models are just like any other human artifact, inadequate initially but over time it gets better.
Only after confidence in the model has been established, one is able to harvest the benefits by handing over the model to *analysis* tools, e.g., a model checker.

[Momba](https://momba.dev) is a Python framework for working with quantitative models centered around the [JANI model interchange format](https://jani-spec.org).
In this tutorial, we will guide you through the process from model construction to analysis using a concrete example inspired by the [Racetrack benchmark](https://racetrack.perspicuous-computing.science/).
You will learn (1) how to leverage Momba's API to programmatically turn a domain-specific scenario description (e.g., a map of a game or a circuit diagram) into a quantitative model, (2) how to validate and test such models using Momba's explicit state space exploration engine by prototyping a tool for interactive model exploration and visualization, and (3) how to use the unified interfaces provided by Momba to invoke state-of-the-art tools for model analysis.

Over the past decade, Python has gained popularity especially in academia where the requirements for reproducibility are high.
Hence, in this tutorial, you will also learn how to use Python and set up a project in a way enabling collaboration and easy packaging of reproducible artifacts.

We plan to run the tutorial as an interactive online event interleaving talks with hands-on sessions.
We will provide you with material on how to prepare your computer for the tutorial upfront.

The hands-on experience will be based on the example of a jump'n'run game where a player has to move from left to right at a constant speed while avoiding obstacles by moving up or down.
The actions of the player are subject to probabilistic noise, i.e., not every action has an effect and the player may continue moving straight instead of moving up or down.
You will construct a formal model based on a map of the game, write an interactive simulation and visualization based on the model using Momba's explicit state space exploration engine, and analyze the model with [The Modest Toolset](https://modestchecker.org) and [Storm](https://www.stormchecker.org/).
We provide you with a project skeleton for the example.


## Preliminary Agenda

- **9:00--09:45**: The tutorial starts with a talk introducing quantitative modelling with Momba where we aim to answer the following questions:

    - What are *quantitative models*?
    - What is the JANI model interchange format?
    - What features does Momba offer for quantitative modeling?
    - What use cases is Momba suited for?
    
  We will demonstrate the core features of Momba using the Racetrack benchmark and give a glimpse on the APIs Momba provides for model construction, exploration, and analysis.
  We then introduce the example the tutorial will be based upon.
  The idea is that you go through the whole process from model construction to analysis using this example.
  We show what you can expect and what the final result will look like.
- **09:45--10:00**: A short interactive talk explaining the project setup and which tools we recommend using for working with Python in an academic setting.
  This talk covers best practices for reproducibility and collaboration concerning the usage of Python within the academic community.
  You can ask questions and we make sure that everyone has a working setup for the remainder of the tutorial.
- **10:00--10:30**: Coffee Break
- **10:30--11:25**: Hands-on session on model construction.
  We demonstrate how to construct an automaton using Momba and then task you with the construction of a formal model for the example.
- **11:25--12:00**: Hands-on session on model exploration.
  We demonstrate how to use Momba's explicit state space exploration engine and then task you with building a tool for interactive model exploration and visualization which allows playing the game on the console.
- **12:00--12:30**: Hands-on session on model analysis.
  You will take their model and analyze it using the state-of-the-art tools The Modest Toolset and Storm vie the APIs Momba provides.