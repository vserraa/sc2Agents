import sc2
from sc2.constants import *
from sc2.units import Unit, Units

class WorkerAgent():
    
    def __init__(self, game_ref):
        self.game = game_ref

    async def on_step(self, iteration):
        #print("Agente coletor distribuindo tropas!")
        await self.game.distribute_workers()
        await self.build_workers()

    async def build_workers(self):
        if (len(self.game.units(NEXUS)) * 16) > len(self.game.units(PROBE)) and len(self.game.units(PROBE)) < self.game.MAX_WORKERS:
            for nexus in self.game.units(NEXUS).ready.noqueue:
                if self.game.can_afford(PROBE):
                    await self.game.do(nexus.train(PROBE))