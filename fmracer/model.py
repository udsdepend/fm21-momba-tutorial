# -*- coding:utf-8 -*-

from __future__ import annotations

import dataclasses as d
import typing as t

import pathlib


# import the modelling API from Momba
from momba import model
from momba.moml import expr


@d.dataclass(frozen=True)
class Cell:
    """Represents a cell on a track."""

    x: int
    y: int


@d.dataclass(frozen=True)
class Track:
    """Represents a track with a certain width, height, and obstacles."""

    width: int
    height: int
    obstacles: t.Set[Cell]

    @classmethod
    def from_ascii(cls, ascii: t.Tuple[str, ...]) -> Track:
        """Constructs a track from an ASCII art representation."""
        width = len(ascii[0])
        height = len(ascii)
        obstacles = set()
        for y, line in enumerate(ascii):
            for x, symbol in enumerate(line):
                if symbol == "x":
                    obstacles.add(Cell(x, y))
        return cls(width, height, obstacles)

    @classmethod
    def from_path(cls, path: pathlib.Path) -> Track:
        """Loads a track from a file."""
        return cls.from_ascii(tuple(path.read_text("utf-8").splitlines(keepends=False)))


def construct_model(track: Track, *, fail_probability: float = 0.4) -> model.Network:
    """
    Constructs a model for the given track.

    Here *fail_probability* is the probability that an action has no effect.
    """

    # Creates a *Markov Decision Process* (MDP) modeling context. We are going
    # to create an MDP model of the game.
    ctx = model.Context(model.ModelType.MDP)

    # TODO: Declare two global variables `pos_x` and `pos_y` for the $x$ and $y$
    # position of the player, respectively. Both variables should be integers and
    # have an initial value of $0$, i.e., the player starts at the top left. Hint:
    # you need to call the method `declare_variable` on the `global_scope` of the
    # modeling context `ctx`. You may find the following resources helpful:
    # - https://momba.dev/reference/model/context/#context
    # - https://momba.dev/reference/model/context/#scope

    # SOLUTION:
    ctx.global_scope.declare_variable("pos_x", typ=model.types.INT, initial_value=0)
    ctx.global_scope.declare_variable("pos_y", typ=model.types.INT, initial_value=0)

    # TODO: In addition to those two variables declare two boolean variables `has_won`
    # and `has_crashed` which should initially be set to `False`.

    # SOLUTION:
    ctx.global_scope.declare_variable(
        "has_won", typ=model.types.BOOL, initial_value=False
    )
    ctx.global_scope.declare_variable(
        "has_crashed", typ=model.types.BOOL, initial_value=False
    )

    # TODO: The player needs to be able to do something. To this end, we have to
    # declare the *action types* it can perform. An action type is a label on a
    # transition of the constructed model. Declare three action types `left` (for
    # moving left), `right` (for moving right), and `stay` (for not moving).
    # Action types are declared with the method `create_action_type` on the
    # modeling context `ctx`. Each of the declared action types which are
    # returned by `create_action_type` should be assigned to a respective
    # variable `left_action`, `right_action`, and `stay_action` such that we can
    # use them in the following. You may find the following resources helpful:
    # - https://momba.dev/reference/model/context/#context
    left_action = ...
    right_action = ...
    stay_action = ...

    # SOLUTION:
    left_action = ctx.create_action_type("left")
    right_action = ctx.create_action_type("right")
    stay_action = ctx.create_action_type("stay")

    # TODO: The automaton network will consist of a single automaton which
    # contains nondeterminism as far as the players actions are concerned.
    # Create this automaton. Automata are created on the modeling context
    # `ctx` using the method `create_automaton`. You should assign the
    # automaton to a variable such that locations and edges can be added
    # to the automaton in the next steps. For this step, it suffices to
    # just create the automaton itself.
    automaton = ...

    # SOLUTION:
    automaton = ctx.create_automaton(name="Environment")

    # You now have to model the actual automaton. Depending on which of the
    # actions is taken by the player, the automaton should advance the
    # position of the player and track whether the player won or crashed
    # into an obstacle. You can create locations with the `create_location`
    # and edges with the `create_edge` method of the automaton. You may
    # find the following resources helpful:
    # - https://momba.dev/reference/model/automata/
    #
    # The automaton we create will just have a single location and an edge
    # for each of the action types defined earlier.

    # TODO: Create an initial location for the automaton and assign it to
    # a variable such that it can be used later.
    location = ...

    # SOLUTION:
    location = automaton.create_location("ready", initial=True)

    # Momba allows you to write JANI expressions using a concise syntax.
    # To this end, the function `expr` (imported above) can be used. The
    # following line constructs an expression which evaluates to a boolean
    # indicating whether the player can move in a given state:
    can_move = expr("not has_won and not has_crashed")
    # Clearly, when the player has not already or crashed, then it should
    # be able to move. We are going to use this expression in a guard for
    # the edges of the automation. These edges should be enabled only if
    # the player can actually still move.
    #
    # The grammer for the expressions is straightforward. A reference can
    # be found here: https://momba.dev/incubator/moml/grammar/. The syntax
    # for expressions is defined by the `<expression>` nonterminal.

    # In our model we will need to update the variables `has_won` and
    # `has_crashed` based on whether the player wins or crashes with
    # a given move. To this end, we define two auxiliary functions which
    # take coordinates and determine whether the player wins or crashes
    # when being at those coordinates.

    def has_won(x: model.Expression) -> model.Expression:
        """Constructs an expression for whether the player won."""
        # The player won if its x coordinate is greater or equal to the
        # width of the track as this means that it reached the end. Note
        # how the following line allows constructing an expression from
        # other expressions and Python values in a concise way:
        return expr("$x >= $width", x=x, width=track.width)

    def has_crashed(x: model.Expression, y: model.Expression) -> model.Expression:
        """Constructs an expression for whether the player crashed."""

        # The player crashes if and only if it drives of the track at the sides or
        # crashes into an obstacle. We construct expressions for each of these
        # cases individually and later combine them with an `or`.

        # TODO: Construct an expression checking whether the player has moved out
        # of bounds in y direction. The player has moved out of bounds if the y
        # coordinate is less than zero or greater or equal to the height of the
        # track. Hint: You can again use the function `expr`. Analogously to `x`
        # and `track.width` in the function `has_won`, you should pass `y` as well
        # as `track.height` into the expression.
        out_of_bounds = ...

        # SOLUTION:
        out_of_bounds = expr("$y >= $height or $y < 0", y=y, height=track.height)

        # TODO: Now, construct an expression for checking whether the player
        # has crashed into an obstacle. To this end, iterate over the obstacles
        # of the track and check for each obstacle individually whether the
        # provided x and y coordinates are the same as the coordinates of the
        # obstacle. We will use the `logic_any` function which essentially
        # implements existential quantification. Analogously to above, construct
        # an expression comparing the coordinates.
        on_obstacle = model.expressions.logic_any(
            *(expr(...) for obstacle in track.obstacles)
        )

        # SOLUTION:
        on_obstacle = model.expressions.logic_any(
            *(
                expr(
                    "$x == $obstacle_x and $y == $obstacle_y",
                    x=x,
                    y=y,
                    obstacle_x=obstacle.x,
                    obstacle_y=obstacle.y,
                )
                for obstacle in track.obstacles
            )
        )

        # Finally, we use `logic_or` to combine both expressions.
        return model.expressions.logic_or(out_of_bounds, on_obstacle)

    # We now have to create the edges of the automaton.

    # To avoid code repetition we are using a dictionary mapping each of the
    # action types to the effect they should have on the y position of the
    # player. Note that this assumes that you have named the variables in
    # the previous step as described.
    moves = {left_action: -1, right_action: 1, stay_action: 0}

    # We now iterate over the items in the dictionary and create an edge
    # corresponding to the respective action type.
    for action_type, delta in moves.items():
        # TODO: Create two expressions `new_pos_x` and `new_pos_y` for the
        # new position of the player after applying the respective action.
        # The x position is advanced by $1$ in each step and the y position
        # is advanced by `delta`. You again need to use `expr`.
        new_pos_x = ...
        new_pos_y = ...

        # SOLUTION:
        new_pos_x = expr("pos_x + 1")
        new_pos_y = expr("pos_y + $delta", delta=delta)

        # We are now ready to create an edge for the respective action type. This
        # edge needs two probabilistic destinations, one for when the action has an
        # effect and one for when the action has no effect.

        # TODO: Create an expression for the probability that the action takes
        # effect. This is $1 - fail_probability$. To this end, you can again
        # use the `expr` function:
        success_probability = ...

        # SOLUTION:
        success_probability = expr(
            "1 - $fail_probability", fail_probability=fail_probability
        )

        # TODO: Create the destination where the action takes effect. To this end,
        # you have to use the function `create_destination` of the module `model`:
        # https://momba.dev/reference/model/automata/#momba.model.create_destination
        success_destination = model.create_destination(
            # TODO: Pass in the target location `location` and the probability
            # expression `success_probability` defined above.
            assignments={
                # These assignments are executed when transitioning to the
                # respective destination. We update the variables here.
                "pos_x": new_pos_x,
                # TODO: Update the remaining variables `pos_y`, `has_won`, and
                # `has_crashed` based on the new position. Hint: You want to
                # use the earlier defined functions `has_won` and `has_crashed`
                # here to update the variables `has_won` and `has_crashed`.
                ...: ...,
            },
        )

        # SOLUTION:
        success_destination = model.create_destination(
            location,
            probability=success_probability,
            assignments={
                "pos_x": new_pos_x,
                "pos_y": new_pos_y,
                "has_won": has_won(new_pos_x),
                "has_crashed": has_crashed(new_pos_x, new_pos_y),
            },
        )

        # TODO: Construct a destination for when the action takes no effect.
        # In this case, the x coordinate should be updated to `new_pos_x`.
        # However, the y coordinate should stay as it is. Note that the
        # probability passed to the `create_destination` function has to be
        # an expression. To transform a Python value into an expression you
        # can use the function `model.ensure_expr`.
        fail_destination = ...

        # SOLUTION:
        fail_destination = model.create_destination(
            location,
            probability=model.ensure_expr(fail_probability),
            assignments={
                "pos_x": new_pos_x,
                "has_won": has_won(new_pos_x),
                "has_crashed": has_crashed(new_pos_x, expr("pos_y")),
            },
        )

        # Now, it reamins to create the edge for the respective action type.
        automaton.create_edge(
            # TODO: Add the arguments for the source location `location`, the
            # guard of the edge which should be `can_move` such that the edge
            # is enabled if and only if the player can move, as well as the
            # earlier defined destinations for this edge.
            ...,
            # Momba supports a non-standard JANI feature for value passing. This
            # is why we have to create an *action pattern* here:
            action_pattern=action_type.create_pattern(),
        )

        # SOLUTION:
        automaton.create_edge(
            location,
            action_pattern=action_type.create_pattern(),
            guard=can_move,
            destinations=[success_destination, fail_destination],
        )

    instance = automaton.create_instance()

    network = ctx.create_network()
    network.add_instance(instance)
    for action_type in moves.keys():
        network.create_link(
            {instance: action_type.create_pattern()},
            result=action_type.create_pattern(),
        )

    return network
