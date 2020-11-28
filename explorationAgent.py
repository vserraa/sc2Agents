import sc2
from sc2.constants import NEXUS, PYLON
from sc2.ids.ability_id import AbilityId
from sc2.ids.buff_id import BuffId
from sc2.units import Unit, Units

class ExplorationAgent():
    
    def __init__(self, game_ref):
        self.game = game_ref

    async def on_step(self, iteration):
        print("Agente explorador!")
        await self.expand()
        await self.chronoboost()

    async def expand(self):
        if self.game.units(NEXUS).amount < (self.game.iteration / self.game.ITERATIONS_PER_MINUTE) and self.game.can_afford(NEXUS):
            await self.game.expand_now()

    async def chronoboost(self):
        if self.game.units(PYLON).exists:
            for nexus in self.game.units(NEXUS):
                abilities = await self.game.get_available_abilities(nexus)
                if AbilityId.EFFECT_CHRONOBOOSTENERGYCOST in abilities:
                    if not nexus.has_buff(BuffId.CHRONOBOOSTENERGYCOST):
                        await self.game.do(nexus(AbilityId.EFFECT_CHRONOBOOSTENERGYCOST, nexus))