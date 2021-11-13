# Model Validation

After a formal model has been conceived, one has to *validate* that the model actually adequately models what should be modeled.
In case the model is not adequate, results obtained by analysis techniques are meaningless.
One way to validate a formal model is to program an interactive simulation where the modeler and other stakeholders can interact with the model and test whether it has the desired properties.

To validate the model of the jump'n'run game, you will program an interactive simulation in terms of a console game where you can steer the car through a track.
To this end, you will use Momba's state space exploration engine.
Given a JANI automaton network, Momba provides an API to explore its state space.

{numref}`interactive-game` shows the console game.
The player (blue `x`) is controlled with the arrow keys.

```{figure} ./images/interactive-game.gif
---
name: interactive-game
scale: 70%
align: center
---
Interactive simulation of the jump'n'run game.
```


## Interactive Game

For the console interface, we first have to add a few dependencies:
```
poetry add asciimatics
poetry add click
```
[Asciimatics](https://github.com/peterbrittain/asciimatics) is a package for creating full-screen console UIs and [Click](https://click.palletsprojects.com/) is a package for parsing command line arguments.
With Momba you have Python's whole ecosystem right at your fingertips.


```{admonition} Exercise

The file `fmracer/interactive.py` provides a skeleton of the interactive simulation which you have to complete by filling in the gaps.
Again, each gap comes with detailed instructions and hints what you need to do.
```

To run the simulation, you have to first activate the virtual environment.
In the VS Code terminal, this is done automatically.
Within another terminal, you activate the environment with:
```
poetry shell
```
Having activated the virtual environment, you start the game with:
```
fmracer race tracks/simple.txt
```
This will use the track defined in `tracks/simple.txt`.

Using the option `--fail-probability` you can also change the probability with which an action fails.

The file `solutions/interactive.py` contains a possible solution.