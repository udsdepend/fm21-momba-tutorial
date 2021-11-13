import typing as t

import functools
import pathlib
import warnings

import click

from asciimatics.screen import Screen

from momba import engine
from momba.tools import modest, storm_docker
from momba.moml import expr, prop

from . import analysis, model, interactive


CHECKERS = [modest.get_checker(accept_license=True), storm_docker.checker]


warnings.simplefilter("ignore")


@click.group()
def main():
    pass


@main.command()
@click.argument("tracks", metavar="TRACK", type=pathlib.Path, required=True, nargs=-1)
@click.option("--resolution", type=int, default=10)
def check(tracks: t.Sequence[pathlib.Path], resolution: int):
    analysis.analyze(
        [(track.stem, model.Track.from_path(track)) for track in tracks], resolution
    )


@main.command()
@click.argument("track", type=pathlib.Path)
@click.option("--fail-probability", type=float, default=0.4)
def race(track: pathlib.Path, fail_probability: float):
    Screen.wrapper(
        functools.partial(
            interactive.game,
            model.Track.from_path(track),
            fail_probability=fail_probability,
        )
    )


if __name__ == "__main__":
    main()
