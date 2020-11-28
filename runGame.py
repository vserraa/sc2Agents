import sc2
from sc2 import run_game, maps, Race, Difficulty
from sc2.player import Bot, Computer
from mainAgent import MainAgent
from mainAgent2 import MainAgent2

run_game(maps.get("AcropolisLE"), [
    Bot(Race.Protoss, MainAgent()),
    Bot(Race.Protoss, MainAgent2())
    ], realtime=False)