import sc2
from sc2.ids.unit_typeid import UnitTypeId
import random

class ConstructorAgent():
    
    def __init__(self, game_ref):
        self.game = game_ref
        self.MAX_DISTANCE = 60
        self.MAX_GATEWAY = 12
        self.MAX_STARGATE = 8

    async def on_step(self, iteration):
        #print("Agente construtor!")
        await self.build_pylons()
        await self.build_assimilators()
        await self.offensive_force_buildings()

    async def build_pylons(self):
        if self.game.supply_left < 5 and not self.game.already_pending(UnitTypeId.PYLON):
            if self.game.townhalls.ready.exists:
                nexus = self.game.townhalls.ready.random
                if self.game.can_afford(UnitTypeId.PYLON):
                    await self.game.build(UnitTypeId.PYLON, near=nexus.position.towards(self.game.game_info.map_center, 8), max_distance=self.MAX_DISTANCE)

    async def build_assimilators(self):
        for nexus in self.game.townhalls.ready:
            vaspenes = self.game.vespene_geyser.closer_than(15.0, nexus)
            for vaspene in vaspenes:
                if not self.game.can_afford(UnitTypeId.ASSIMILATOR):
                    break
                worker = self.game.select_build_worker(vaspene.position)
                if worker is None:
                    break
                if not self.game.structures(UnitTypeId.ASSIMILATOR).closer_than(1.0, vaspene).exists:
                    worker.build(UnitTypeId.ASSIMILATOR, vaspene)

    async def offensive_force_buildings(self):
        if self.game.structures(UnitTypeId.PYLON).ready.exists:
            pylon = self.game.structures(UnitTypeId.PYLON).ready.random

            if self.game.structures(UnitTypeId.GATEWAY).ready.exists and not self.game.structures(UnitTypeId.CYBERNETICSCORE):
                if self.game.can_afford(UnitTypeId.CYBERNETICSCORE) and not self.game.already_pending(UnitTypeId.CYBERNETICSCORE):
                    await self.game.build(UnitTypeId.CYBERNETICSCORE, near=pylon, max_distance=self.MAX_DISTANCE)

            elif self.game.structures(UnitTypeId.GATEWAY).amount + self.game.already_pending(UnitTypeId.GATEWAY) < ((self.game.iteration / self.game.ITERATIONS_PER_MINUTE)/2) and self.game.structures(UnitTypeId.GATEWAY).amount + self.game.already_pending(UnitTypeId.GATEWAY) < self.MAX_GATEWAY:
                if self.game.can_afford(UnitTypeId.GATEWAY) and not self.game.already_pending(UnitTypeId.GATEWAY):
                    await self.game.build(UnitTypeId.GATEWAY, near=pylon, max_distance=self.MAX_DISTANCE)

            if self.game.structures(UnitTypeId.CYBERNETICSCORE).ready.exists:
                if self.game.structures(UnitTypeId.STARGATE).amount + self.game.already_pending(UnitTypeId.STARGATE) < ((self.game.iteration / self.game.ITERATIONS_PER_MINUTE)/2) and self.game.structures(UnitTypeId.STARGATE).amount + self.game.already_pending(UnitTypeId.STARGATE) < self.MAX_STARGATE:
                    if self.game.can_afford(UnitTypeId.STARGATE) and not self.game.already_pending(UnitTypeId.STARGATE):
                        await self.game.build(UnitTypeId.STARGATE, near=pylon, max_distance=self.MAX_DISTANCE)
            
            if not self.game.structures(UnitTypeId.FORGE).ready.exists and not self.game.already_pending(UnitTypeId.FORGE) and self.game.structures(UnitTypeId.GATEWAY).amount > 2:
                await self.game.build(UnitTypeId.FORGE, near=pylon, max_distance=self.MAX_DISTANCE)