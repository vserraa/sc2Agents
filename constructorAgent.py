import sc2
from sc2 import run_game, maps, Race, Difficulty
from sc2.player import Bot, Computer
from sc2.constants import NEXUS, PYLON, GATEWAY, ASSIMILATOR, \
 CYBERNETICSCORE, STALKER, STARGATE, VOIDRAY, FORGE
import random

class ConstructorAgent():
    
    def __init__(self, game_ref):
        self.game = game_ref
        self.MAX_DISTANCE = 2000

    async def on_step(self, iteration):
        print("Agente construtor!")
        await self.build_pylons()
        await self.build_assimilators()
        await self.offensive_force_buildings()

    async def build_pylons(self):
        if self.game.supply_left < 5 and not self.game.already_pending(PYLON):
            if self.game.units(NEXUS).ready.exists:
                nexus = self.game.units(NEXUS).ready.random
                if self.game.can_afford(PYLON):
                    await self.game.build(PYLON, near=nexus, max_distance=self.MAX_DISTANCE)

    async def build_assimilators(self):
        for nexus in self.game.units(NEXUS).ready:
            vaspenes = self.game.state.vespene_geyser.closer_than(15.0, nexus)
            for vaspene in vaspenes:
                if not self.game.can_afford(ASSIMILATOR):
                    break
                worker = self.game.select_build_worker(vaspene.position)
                if worker is None:
                    break
                if not self.game.units(ASSIMILATOR).closer_than(1.0, vaspene).exists:
                    await self.game.do(worker.build(ASSIMILATOR, vaspene))

    async def offensive_force_buildings(self):
        if self.game.units(PYLON).ready.exists:
            pylon = self.game.units(PYLON).ready.random

            if self.game.units(GATEWAY).ready.exists and not self.game.units(CYBERNETICSCORE):
                if self.game.can_afford(CYBERNETICSCORE) and not self.game.already_pending(CYBERNETICSCORE):
                    await self.game.build(CYBERNETICSCORE, near=pylon, max_distance=self.MAX_DISTANCE)

            elif len(self.game.units(GATEWAY)) < ((self.game.iteration / self.game.ITERATIONS_PER_MINUTE)/2):
                if self.game.can_afford(GATEWAY) and not self.game.already_pending(GATEWAY):
                    await self.game.build(GATEWAY, near=pylon, max_distance=self.MAX_DISTANCE)

            if self.game.units(CYBERNETICSCORE).ready.exists:
                if len(self.game.units(STARGATE)) < ((self.game.iteration / self.game.ITERATIONS_PER_MINUTE)/2):
                    if self.game.can_afford(STARGATE) and not self.game.already_pending(STARGATE):
                        await self.game.build(STARGATE, near=pylon, max_distance=self.MAX_DISTANCE)
            
            if not self.game.units(FORGE).ready.exists and not self.game.already_pending(FORGE) and len(self.game.units(GATEWAY)) > 2:
                await self.game.build(FORGE, near=pylon, max_distance=self.MAX_DISTANCE)