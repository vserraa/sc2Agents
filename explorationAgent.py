import sc2
from sc2.constants import *
from sc2.units import Unit, Units

class ExplorationAgent():
    
    def __init__(self, game_ref):
        self.game = game_ref

    async def on_step(self, iteration):
        print("Agente explorador!")
        await self.expand()

    async def expand(self):
        if self.game.units(NEXUS).amount < (self.game.iteration / self.game.ITERATIONS_PER_MINUTE) and self.game.can_afford(NEXUS):
            await self.game.expand_now()