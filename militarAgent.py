import sc2
from sc2 import run_game, maps, Race, Difficulty
from sc2.player import Bot, Computer
from sc2.constants import NEXUS, PROBE, PYLON, ASSIMILATOR, GATEWAY, \
 CYBERNETICSCORE, STALKER, STARGATE, VOIDRAY
import random

class MilitarAgent():
    
    def __init__(self, game_ref):
        self.game = game_ref

    async def on_step(self, iteration):
        print("Agente militar!")
        await self.train_offensive_units()
        await self.attack()

    async def attack(self):
        # {UNIT: [n to fight, n to defend]}
        aggressive_units = {STALKER: [15, 5],
                            VOIDRAY: [8, 3]}


        for UNIT in aggressive_units:
            if self.game.units(UNIT).amount > aggressive_units[UNIT][0] and self.game.units(UNIT).amount > aggressive_units[UNIT][1]:
                for s in self.game.units(UNIT).idle:
                    await self.game.do(s.attack(self.find_target(self.game.state)))

            elif self.game.units(UNIT).amount > aggressive_units[UNIT][1]:
                if len(self.game.known_enemy_units) > 0:
                    for s in self.game.units(UNIT).idle:
                        await self.game.do(s.attack(random.choice(self.game.known_enemy_units)))

    async def train_offensive_units(self):
        for gw in self.game.units(GATEWAY).ready.noqueue:
            if not self.game.units(STALKER).amount > self.game.units(VOIDRAY).amount:
                if self.game.can_afford(STALKER) and self.game.supply_left > 0:
                    await self.game.do(gw.train(STALKER))

        for sg in self.game.units(STARGATE).ready.noqueue:
            if self.game.can_afford(VOIDRAY) and self.game.supply_left > 0:
                await self.game.do(sg.train(VOIDRAY))

    def find_target(self, state):
        if len(self.game.known_enemy_units) > 0:
            return random.choice(self.game.known_enemy_units)
        elif len(self.game.known_enemy_structures) > 0:
            return random.choice(self.game.known_enemy_structures)
        else:
            return self.game.enemy_start_locations[0]