# Modeling with Momba

Momba is centered around the [JANI](https://jani-spec.org) model interchange format.
JANI is a well-established standard in the quantitative model checking community and is supported by a variety of tools.
A JANI model is a *network* of interacting *automata*.
These automata are annotated with variables and can comprise non-deterministic choices, probabilistic behavior, continuous dynamics, as well as real-time behavior.
For the purpose of this tutorial, we are only using a subset of these features, namely non-deterministic choices and probabilistic behavior.


## Example: Parking Lot

To get a first intuition, how JANI models work, consider the example of a parking lot with a ticket machine (see {numref}`parking-lot-image`).
The amount of parking spots in the parking lot is of course finite (100 in the following), hence, the ticket machine must not give out more tickets than there are free spaces.
When the parking lot is full, a car must leave before a new ticket can be issued.
To issue a ticket, the driver has to *push* a button.
After pushing the button, the gate will open such that the driver can *enter* the parking lot.
After entering the parking lot, the gate closes again.
As you can see from the picture, the ticket machine is quite old, thus the button fails 10% of the time.


```{figure} ./images/parking-lot-image.drawio.svg
---
name: parking-lot-image
align: center

---
Parking lot ticket machine and gate.
```

{numref}`parking-lot-automaton` shows a JANI automaton modeling the parking lot and ticket machine.
This automaton has two *locations*, *closed* and *open* corresponding to the gate being closed and open, respectively.
These locations are connected by *edges*.
Edges are *labeled*.
In this case, there are three labels: *press*, *enter*, and *leave*.

```{figure} ./images/parking-lot.drawio.svg
---
name: parking-lot-automaton
align: center
---
Parking lot and ticket machine automaton.
```

The variable *counter* keeps track of the amount of cars currently in the parking lot.
It is initialized to zero when entering the initial *closed* state.
Independent on whether the gate is *open* or *closed*, the driver can always *press* the button on the ticket machine.
In case the gate is already *open*, pressing the button has no effect.
In case the gate is *closed*, the effect of pressing the button depends on the amount of cars currently in the parking lot.
In case the parking lot is full, i.e., `counter ≥ 100`, pushing the button has again no effect.
Otherwise, if the parking lot is not full yet, i.e., `counter < 100`, then with a probability of 10%, the button will fail and nothing will happen, and, with a probability of 90%, the counter is increased by one and the gate will *open*.
When the gate is *open*, a car can *enter* the parking lot.
After entering, the gate will be *closed* again.
Also, a car can *leave* the parking lot at any time.
When a car leaves, the counter will be decremented.

{numref}`driver-automaton` shows a JANI automaton modeling a driver who tries to enter the parking lot.
The driver will try to press the button at most three times and enters the parking lot in case the gate opens.
If the gate does not open after pressing the button three times, they will give up trying.

```{figure} ./images/driver.drawio.svg
---
name: driver-automaton
align: center
---
Driver automaton.
```

By synchronizing these automata on their shared labels, *press* and *enter*, we obtain an automaton *network*.
Using this network, we can for instance model check the probability that the driver will eventually enter the parking lot given that the parking lot is in its initial completely empty state.


## Momba

Momba brings to the table an API to work with JANI models.
