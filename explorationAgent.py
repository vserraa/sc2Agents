import sc2
from sc2.constants import NEXUS, PYLON
from sc2.ids.ability_id import AbilityId
from sc2.ids.buff_id import BuffId
from sc2.units import Unit, Units
from sc2.ids.unit_typeid import UnitTypeId

class ExplorationAgent():
    
    def __init__(self, game_ref):
        self.game = game_ref
        self.priority = [UnitTypeId.NEXUS, UnitTypeId.STARGATE, UnitTypeId.GATEWAY, UnitTypeId.FORGE]

    async def on_step(self, iteration):
        #print("Agente explorador!")
        await self.expand()
        await self.chronoboost()

    async def expand(self):
        if self.game.townhalls.ready.amount + self.game.already_pending(UnitTypeId.NEXUS) < 3 and self.game.can_afford(UnitTypeId.NEXUS):
            await self.game.expand_now()
        elif self.game.townhalls.ready.amount + self.game.already_pending(UnitTypeId.NEXUS) < (self.game.iteration / ( 2 * self.game.ITERATIONS_PER_MINUTE) ) and self.game.can_afford(UnitTypeId.NEXUS):
            await self.game.expand_now()
            
    async def chronoboost(self):
        for nexus in self.game.townhalls.ready:
            for cur_type in self.priority:
                for building in self.game.structures(cur_type).ready:
                    if not building.is_idle:
                        if nexus.energy >= 50:
                            nexus(AbilityId.EFFECT_CHRONOBOOSTENERGYCOST, nexus)
