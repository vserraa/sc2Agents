import sc2
from sc2.constants import NEXUS, PYLON
from sc2.ids.ability_id import AbilityId
from sc2.ids.buff_id import BuffId
from sc2.units import Unit, Units
from sc2.constants import NEXUS, PYLON, GATEWAY, ASSIMILATOR, \
 CYBERNETICSCORE, STALKER, STARGATE, VOIDRAY, FORGE

class ExplorationAgent():
    
    def __init__(self, game_ref):
        self.game = game_ref
        self.priority = [NEXUS, STARGATE, GATEWAY, FORGE]

    async def on_step(self, iteration):
        #print("Agente explorador!")
        await self.expand()
        await self.chronoboost()

    async def expand(self):
        if self.game.townhalls.ready.amount + self.game.already_pending(NEXUS) < 3 and self.game.can_afford(NEXUS):
            await self.game.expand_now()
        elif self.game.townhalls.ready.amount + self.game.already_pending(NEXUS) < (self.game.iteration / ( 2 * self.game.ITERATIONS_PER_MINUTE) ) and self.game.can_afford(NEXUS):
            await self.game.expand_now()
            
    async def chronoboost(self):
        for nexus in self.game.units(NEXUS).ready:
            for cur_type in self.priority:
                for building in self.game.units(cur_type).ready:
                    if not building.is_idle:
                        if nexus.energy >= 50:
                            await self.game.do(nexus(AbilityId.EFFECT_CHRONOBOOSTENERGYCOST, nexus))
