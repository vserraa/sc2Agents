import sc2
from sc2 import run_game, maps, Race, Difficulty
from sc2.player import Bot, Computer
from mainAgent import MainAgent

run_game(maps.get("AcropolisLE"), [
    Bot(Race.Protoss, MainAgent()),
    Computer(Race.Zerg, Difficulty.Hard)
    ], realtime=False)