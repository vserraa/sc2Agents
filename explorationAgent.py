import sc2
from sc2.constants import *
from sc2.units import Unit, Units

class ExplorationAgent():
    
    def __init__(self, game_ref):
        self.game = game_ref

    async def on_step(self, iteration):
        #print("Agente explorador!")
        await self.expand()

    async def expand(self):
        if self.game.townhalls.ready.amount + self.game.already_pending(NEXUS) < 3 and self.game.can_afford(NEXUS):
            await self.game.expand_now()
        elif self.game.townhalls.ready.amount + self.game.already_pending(NEXUS) < (self.game.iteration / ( 3 * self.game.ITERATIONS_PER_MINUTE) ) and self.game.can_afford(NEXUS):
            await self.game.expand_now()