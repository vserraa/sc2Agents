import sc2
from sc2 import run_game, maps, Race, Difficulty
from sc2.player import Bot, Computer
from sc2.constants import NEXUS, PROBE, PYLON, ASSIMILATOR, GATEWAY, \
 CYBERNETICSCORE, STALKER, STARGATE, VOIDRAY
import random
from workerAgent2 import WorkerAgent
from constructorAgent2 import ConstructorAgent
from militarAgent2 import MilitarAgent
from explorationAgent2 import ExplorationAgent

class MainAgent2(sc2.BotAI):
    def __init__(self):
        self.ITERATIONS_PER_MINUTE = 165
        self.MAX_WORKERS = 50
        self.workerAgent = WorkerAgent(self)
        self.constructorAgent = ConstructorAgent(self)
        self.militarAgent = MilitarAgent(self)
        self.explorationAgent = ExplorationAgent(self)
        self.iteration = 0

    async def on_step(self, iteration):   
        self.iteration = iteration     
        await self.workerAgent.on_step(iteration)
        await self.constructorAgent.on_step(iteration)
        await self.explorationAgent.on_step(iteration)
        await self.militarAgent.on_step(iteration)