# Momba: Python for Quantitative Models

Dealing with quantitative models encompasses a variety of tasks which can be challenging from time to time.
Everything starts with the *construction* of a formal model or a family thereof.
Often a textual or other, more formal, description of the scenario to be modeled already exists, such as a rough sketch of the desired behavior or a circuit diagram.
Then, after a formal model has finally been conceived, one has to *validate* that the model actually adequately represents what should be modeled.
In this regard models are just like any other human artifact, inadequate initially but over time it gets better.
Only after confidence in the model has been established, one is able to harvest the benefits by handing over the model to *analysis* tools, e.g., a model checker.

```{important}
See [Prepare Your System](preparation) for details on **how to prepare your system for the tutorial**.
```

[Momba](https://momba.dev) is a Python framework for working with quantitative models centered around the [JANI model interchange format](https://jani-spec.org).
Momba strives to deliver an integrated and intuitive experience to aid the process of model construction, validation, and analysis.
In this tutorial, we will guide you through the process from model construction to analysis using a concrete example inspired by the [Racetrack benchmark](https://racetrack.perspicuous-computing.science/).
You will learn (1) how to leverage Momba's API to programmatically turn a domain-specific scenario description (e.g., a map of a game or a circuit diagram) into a quantitative model, (2) how to validate and test such models using Momba's explicit state space exploration engine by prototyping a tool for interactive model exploration and visualization, and (3) how to use the unified interfaces provided by Momba to invoke state-of-the-art tools for model analysis.
Along the way, you will also learn how to set up a Python Project in a way enabling collaboration and easy packaging of reproducible artifacts.
Over the past decade, Python has gained popularity especially in academia where the requirements for reproducibility are high.

We run the tutorial as an interactive online event interleaving talks with hands-on sessions.

```{hint}
This page contains a written version of the tutorial for reference.
We will walk you through the tutorial on the day of the tutorial.
You do not need to do anything upfront besides [preparing your system](preparation).
```

The hands-on experience will be based on the example of a jump'n'run game where a player moves from left to right at a constant speed while avoiding obstacles by moving up or down.
The actions of the player are subject to probabilistic noise, i.e., not every action has an effect and the player may continue moving straight instead of moving up or down.
You will construct a formal model based on a map of the game, write an interactive simulation and visualization based on the model using Momba's explicit state space exploration engine, and analyze the model with the [Modest Toolset](https://modestchecker.org).
We provide you with a project skeleton for the example.


## Preliminary Schedule

The tutorial takes place on **November, 20th** during sessions 1 through 2 ([**16:00–19:30** CST](https://www.timeanddate.com/worldclock/fixedtime.html?msg=FM%2721%3A+Momba+Tutorial&iso=20211120T16&p1=33&ah=3&am=30)).

- **16:00–17:30**: Session 1
  - *Introduction*: What are you going to learn throughout the tutorial?
  - [*Getting Started*](tutorial/getting-started): We walk you through the process of setting up the provided project skeleton such that you can follow along.
    Please make sure to have [prepared your system upfront](preparation).
  - [*Best Practices*](tutorial/best-practices): **How to set up a Python project for reproducibility and easy collaboration?**

      We will walk you through the provided project skeleton.
      You will learn how to manage dependencies in a way that enables reproducibility, prevents version conflicts, and makes collaboration easy.
      We will demonstrate how to use tools such as auto formatters and linters to ensure a consistent code style and how to use VS Code workspaces to unify the development environment across a project.
  - [*Running Example*](tutorial/running-example): We introduce the example you will be working with in more detail.
  - [*Model Construction*](tutorial/model-construction):
      We introduce the theory behind Momba and the [JANI model format](https://jani-spec.org).
- **17:00–17:30**: Break (*deviates from the official schedule*)
- **17:30–19:30**: Session 2
  - [*Model Construction*](tutorial/model-construction): **How to *construct* a formal model with Momba?**

      We walk you through the API provided by Momba to programmatically construct JANI models.
      Afterwards, you will have the opportunity to develop a model on your own using the skeleton we provide.
  - [*Model Validation*](tutorial/model-validation): **How to *validate* a formal model with Momba?**

      We walk you through the state space exploration API provided by Momba.
      You will program an interactive visualization for your model.
  - [*Model Analysis*](tutorial/model-analysis): **How to *analyze* a formal model with Momba?**

      We will briefly introduce quantitative model checking.
      We then walk you through the analysis API provided by Momba.
      Using this API, you will analyze properties of your model.
  - [*Takeaways*](tutorial/takeaways): We wrap up the tutorial with the important takeaways.