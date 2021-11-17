# Running Example

As a running example, we will be using a simple [jump 'n' run](https://en.wikipedia.org/wiki/Platform_game) game where the player has to avoid obstacles while moving forward (from left to right) at a constant speed.
To avoid obstacles, the player can move up or down.
The goal is to reach the end of the *track* without crashing into an obstacle.

With the help of a little ASCII art, a track may be represented as follows:

```
       x         xxxxx     x      
           xxx          x      xx 
 xxxxxxx          xx              
```

Every `x` represents an obstacle the player has to avoid.
The player starts on the left and moves forward to the right.
The player wins, if and only if it moves beyond the *finishing line*, i.e., reaches the end of the track.
Now, given such a track, we will (1) [construct a formal model](model-construction) of the game.
Note that this goes beyond what is possible with mere parametrization of a model.
After creating a formal model, we will (2) [write an interactive simulation](model-validation) of the game based on the model which can be played on the console.
This simulation helps validating the model.
The model will be noisy in the sense that an action of the player may have no effect with a certain probability, i.e., even if playing optimally, the probability of winning is not $1$.
Hence, we will (3) [determine the probability of winning](model-analysis) when playing optimally using a probabilistic model checker.
