import sc2
from sc2 import run_game, maps, Race, Difficulty
from sc2.player import Bot, Computer
from sc2.constants import NEXUS, PROBE, PYLON, ASSIMILATOR, GATEWAY, \
 CYBERNETICSCORE, STALKER, STARGATE, VOIDRAY
import random
from workerAgent2 import WorkerAgent2
from constructorAgent2 import ConstructorAgent2
from militarAgent2 import MilitarAgent2
from explorationAgent2 import ExplorationAgent2

class MainAgent2(sc2.BotAI):
    def __init__(self):
        self.ITERATIONS_PER_MINUTE = 165
        self.MAX_WORKERS = 50
        self.workerAgent = WorkerAgent2(self)
        self.constructorAgent = ConstructorAgent2(self)
        self.militarAgent = MilitarAgent2(self)
        self.explorationAgent = ExplorationAgent2(self)
        self.iteration = 0

    async def on_step(self, iteration):   
        self.iteration = iteration     
        await self.workerAgent.on_step(iteration)
        await self.constructorAgent.on_step(iteration)
        await self.explorationAgent.on_step(iteration)
        await self.militarAgent.on_step(iteration)