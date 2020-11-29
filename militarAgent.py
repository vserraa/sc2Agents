import sc2
from sc2 import run_game, maps, Race, Difficulty
import random
from sc2.ids.ability_id import AbilityId
from sc2.ids.buff_id import BuffId
from sc2.ids.unit_typeid import UnitTypeId

class MilitarAgent():
    
    def __init__(self, game_ref):
        self.game = game_ref

    async def on_step(self, iteration):
        #print("Agente militar!")
        await self.train_offensive_units()
        await self.attack()
        await self.use_ability()

    async def attack(self):
        # {UNIT: [n to fight, n to defend]}
        aggressive_units = {UnitTypeId.STALKER: [15, 3],
                            UnitTypeId.VOIDRAY: [8, 2]}
        self.targets = (self.game.enemy_units | self.game.enemy_structures).filter(lambda unit: unit.can_be_attacked)

        for UNIT in aggressive_units:
            if self.game.units(UNIT).amount > aggressive_units[UNIT][0]:
                for unit in self.game.units(UNIT).idle:
                    unit.attack(self.find_target(self.game.state, unit))

            elif self.game.units(UNIT).amount > aggressive_units[UNIT][1]:
                if self.targets.amount > 0:
                    for unit in self.game.units(UNIT).idle:
                        unit.attack(self.targets.closest_to(unit))

    async def use_ability(self):
        for unit in self.game.units(UnitTypeId.VOIDRAY):
            if self.targets.amount > 0 and unit.target_in_range(self.targets.closest_to(unit)):
                unit(AbilityId.EFFECT_VOIDRAYPRISMATICALIGNMENT)

    async def train_offensive_units(self):
        for gw in self.game.structures(UnitTypeId.GATEWAY).ready.idle:
            if not self.game.units(UnitTypeId.STALKER).amount > 2 * self.game.units(UnitTypeId.VOIDRAY).amount:
                if self.game.can_afford(UnitTypeId.STALKER) and self.game.supply_left > 0:
                    gw.train(UnitTypeId.STALKER)

        for sg in self.game.structures(UnitTypeId.STARGATE).ready.idle:
            if self.game.can_afford(UnitTypeId.VOIDRAY) and self.game.supply_left > 0:
                sg.train(UnitTypeId.VOIDRAY)

    def find_target(self, state, unit):
        if self.targets.amount > 0:
            return self.targets.closest_to(unit)
        elif self.game.enemy_structures.amount > 0:
            return self.game.enemy_structures.closest_to(unit)
        else:
            return self.game.enemy_start_locations[0]