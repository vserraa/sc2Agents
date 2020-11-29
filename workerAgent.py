import sc2
from sc2.units import Unit, Units
from sc2.ids.unit_typeid import UnitTypeId

class WorkerAgent():
    
    def __init__(self, game_ref):
        self.game = game_ref

    async def on_step(self, iteration):
        #print("Agente coletor")
        await self.game.distribute_workers()
        await self.build_workers()

    async def build_workers(self):
        if (self.game.townhalls.amount * 22) > self.game.workers.amount and self.game.workers.amount < self.game.MAX_WORKERS:
            for nexus in self.game.townhalls.ready.idle:
                if self.game.can_afford(UnitTypeId.PROBE):
                    nexus.train(UnitTypeId.PROBE)