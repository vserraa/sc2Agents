import sc2
from sc2 import run_game, maps, Race, Difficulty
from sc2.player import Bot, Computer
from sc2.constants import NEXUS, PROBE, PYLON, ASSIMILATOR, GATEWAY, CYBERNETICSCORE, STALKER, STARGATE, VOIDRAY
import random
from sc2.ids.ability_id import AbilityId
from sc2.ids.buff_id import BuffId

class MilitarAgent():
    
    def __init__(self, game_ref):
        self.game = game_ref

    async def on_step(self, iteration):
        #print("Agente militar!")
        await self.train_offensive_units()
        await self.attack()
        await self.use_ability()

    async def attack(self):
        self.targets = self.game.known_enemy_units.filter(lambda unit: unit.can_be_attacked)
        if self.game.units(VOIDRAY).amount > 5:
            for unit in self.game.units(VOIDRAY).idle:
                await self.game.do(unit.attack(self.find_target(self.game.state, unit)))

    async def use_ability(self):
        for unit in self.game.units(VOIDRAY):
            if self.targets.amount > 0 and unit.target_in_range(self.targets.closest_to(unit)):
                await self.game.do(unit(AbilityId.EFFECT_VOIDRAYPRISMATICALIGNMENT))

    async def train_offensive_units(self):
        for sg in self.game.units(STARGATE).ready.idle:
            if self.game.can_afford(VOIDRAY) and self.game.supply_left > 0:
                await self.game.do(sg.train(VOIDRAY))

    def find_target(self, state, unit):
        if self.targets.amount > 0:
            return self.targets.closest_to(unit)
        elif self.game.known_enemy_structures.amount > 0:
            return self.game.known_enemy_structures.closest_to(unit)
        else:
            return self.game.enemy_start_locations[0]