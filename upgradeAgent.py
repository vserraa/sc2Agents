import sc2
from sc2 import run_game, maps, Race, Difficulty
from sc2.player import Bot, Computer
from sc2.constants import NEXUS, PYLON, GATEWAY, ASSIMILATOR, \
 CYBERNETICSCORE, STALKER, STARGATE, VOIDRAY, FORGE
import random

class UpgradeAgent():
    
    def __init__(self, game_ref):
        self.game = game_ref
        self.MAX_DISTANCE = 2000
    
    async def on_step(self, iteration):
        print("Agente de upgrade!")
        await self.upgrade_air_units()
        await self.upgrade_ground_units()

    async def upgrade_air_units(self):
        foo()

    async def upgrade_air_units(self):
        foo()

    
