from asciimatics.screen import Screen

import momba
from momba import engine

from . import model


def game(track: model.Track, screen: Screen, *, fail_probability: float = 0.4):
    network = model.construct_model(track, fail_probability=fail_probability)

    # TODO: Construct a new state space explorer.
    explorer = ...

    # SOLUTION:
    explorer = engine.Explorer.new_discrete_time(network)

    # TODO: The model has exactly one initial state, extract it from the model.
    (state,) = ...

    # SOLUTION:
    (state,) = explorer.initial_states

    while True:
        # TODO: Access the global variables of the state to construct
        # a cell object containing the current position of the player.
        player = model.Cell(...)

        # SOLUTION:
        player = model.Cell(
            state.global_env["pos_x"].as_int, state.global_env["pos_y"].as_int
        )

        # Prints the current state of the game to the console.
        for y in range(track.height):
            for x in range(track.width):
                cell = model.Cell(x, y)
                if cell in track.obstacles:
                    screen.print_at("█", x, y, Screen.COLOUR_RED)
                elif cell == player:
                    screen.print_at("x", x, y, Screen.COLOUR_BLUE)
                else:
                    screen.print_at(" ", x, y)

        screen.refresh()

        # We now have to check whether there are any transitions from the
        # current state. If there are transitions, we will ask the user
        # to chose a transition, i.e., a move. Otherwise, we show a screen
        # indicating whether the player won or crashed.

        # TODO:

        if not ...:
            # Clear the screen
            screen.clear()

            if ...:
                screen.centre("Congratulations, you won! 🏆", screen.height // 2)
            else:
                assert ...
                screen.centre("You crashed! 💥", screen.height // 2)

            # Allow the user to quit the program by pressing any key.
            screen.refresh()
            screen.wait_for_input(300)
            return

        # SOLUTION:
        if not state.transitions:
            screen.clear()
            if state.global_env["has_won"].as_bool:
                screen.centre("Congratulations, you won! 🏆", screen.height // 2)
            else:
                assert state.global_env["has_crashed"].as_bool
                screen.centre("You crashed! 💥", screen.height // 2)
            screen.refresh()
            screen.wait_for_input(300)
            return

        # Wait for some user input.
        screen.wait_for_input(300)
        event = screen.get_event()
        assert event is not None

        # Allow the user to press Q to quit the game
        if event.key_code in {ord("Q"), ord("q")}:
            return

        # We now construct a dictionary mapping action labels
        # to transitions.
        # TODO:
        transitions = {}
        for transition in state.transitions:
            ...

        # SOLUTION:
        transitions = {}
        for transition in state.transitions:
            if transition.action is not None:
                label = transition.action.action_type.label
                transitions[label] = transition

        # Select a transition based on the input of the user.
        if event.key_code == Screen.KEY_UP:
            transition = transitions["left"]
        elif event.key_code == Screen.KEY_DOWN:
            transition = transitions["right"]
        else:
            transition = transitions["stay"]

        # TODO: Pick a successor state at random.
        state = ...

        # SOLUTION:
        state = transition.destinations.pick().state
