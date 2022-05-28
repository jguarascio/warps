from dataclasses import dataclass
from random import randint
from typing import Dict, List
import yaml


@dataclass
class Warp():
    type: int
    start: int
    end: int


@dataclass
class Player():
    id: int
    name: str


class Game():
    """
    Defines a simple snakes and ladder (or chutes and ladders) type game.
    The constructor takes a list of players and "warps" which define the squares that
    warp you to another square. 

        play: play the game
        show_winner: show the winner

    """

    def __init__(self, players: List[Player], warps: Dict, target: int = 100) -> None:
        """
        players : str
            a list containing player objects
        warps : Dict
            a dictionary with the source as key, destination as value
        target : int, optional
            target square, defaulted to 100
        """

        self._players = players
        self._warps = warps
        self._target = target
        self._winner = None
        self._rounds = 0

    def play(self) -> None:
        positions = [0 for player in self._players]

        play = True

        while play:
            print(positions)
            self._rounds += 1
            for i, player in enumerate(self._players):

                # Roll the die and move
                move = randint(1, 6)
                new_position = positions[i] + move

                # Check if new position is a warp
                if new_position in self._warps:
                    new_position = self._warps[new_position]

                # Check if player is the target
                if new_position == self._target:
                    self._winner = player
                    play = False
                    break

                # Make sure move doesn't go past target
                if new_position < self._target:
                    positions[i] = new_position

    def show_winner(self):
        print(f"{self._winner} won after {self._rounds} rounds")


if __name__ == "__main__":

    with open("config.yaml", "r") as yamlfile:
        data = yaml.load(yamlfile, Loader=yaml.FullLoader)

    players = []
    for id, name in enumerate(data["players"]):
        players.append(Player(id, name))

    warps = data["warps"]

    # Play the game
    game = Game(players, warps)
    game.play()
    game.show_winner()
