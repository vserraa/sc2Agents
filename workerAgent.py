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
        if (self.game.units(NEXUS).amount * 22) > self.game.units(PROBE).amount and self.game.units(PROBE).amount < self.game.MAX_WORKERS:
            for nexus in self.game.units(NEXUS).ready.idle:
                if self.game.can_afford(PROBE):
                    await self.game.do(nexus.train(PROBE))