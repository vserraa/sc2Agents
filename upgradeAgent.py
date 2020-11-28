import sc2
from sc2 import run_game, maps, Race, Difficulty
from sc2.player import Bot, Computer
from sc2.constants import NEXUS, PYLON, GATEWAY, ASSIMILATOR, \
 CYBERNETICSCORE, STALKER, STARGATE, VOIDRAY, FORGE, FORGERESEARCH_PROTOSSGROUNDWEAPONSLEVEL1, FORGERESEARCH_PROTOSSGROUNDWEAPONSLEVEL2, FORGERESEARCH_PROTOSSGROUNDWEAPONSLEVEL3, FORGERESEARCH_PROTOSSGROUNDARMORLEVEL1, FORGERESEARCH_PROTOSSGROUNDARMORLEVEL2, FORGERESEARCH_PROTOSSGROUNDARMORLEVEL3
import random
from sc2.ids.upgrade_id import UpgradeId

class UpgradeAgent():
    
    def __init__(self, game_ref):
        self.game = game_ref
        self.MAX_DISTANCE = 2000
    
    async def on_step(self, iteration):
        await self.upgrade_ground_units()

    async def upgrade_ground_units(self):
        if self.game.units(FORGE).ready.exists and self.game.units(STALKER) and self.game.units(FORGE).ready.first.is_idle:
            if self.game.already_pending_upgrade(UpgradeId.PROTOSSGROUNDWEAPONSLEVEL1) == 0 and self.game.can_afford(FORGERESEARCH_PROTOSSGROUNDWEAPONSLEVEL1) and self.game.units(STALKER).ready:
                bay = self.game.units(FORGE).ready.first
                await self.game.do(bay.research(UpgradeId.PROTOSSGROUNDWEAPONSLEVEL1))
            elif self.game.already_pending_upgrade(UpgradeId.PROTOSSGROUNDARMORSLEVEL1 ) == 0 and self.game.can_afford(FORGERESEARCH_PROTOSSGROUNDARMORLEVEL1 ) and self.game.units(STALKER).ready:
                bay = self.game.units(FORGE).ready.first
                await self.game.do(bay.research(UpgradeId.PROTOSSGROUNDARMORSLEVEL1 ))

    
