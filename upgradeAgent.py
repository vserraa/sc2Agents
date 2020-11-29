import sc2
from sc2 import run_game, maps, Race, Difficulty
from sc2.player import Bot, Computer
from sc2.ids.unit_typeid import UnitTypeId
from sc2.ids.upgrade_id import UpgradeId

class UpgradeAgent():
    
    def __init__(self, game_ref):
        self.game = game_ref
    
    async def on_step(self, iteration):
        await self.upgrade_ground_units()

    async def upgrade_ground_units(self):
        if self.game.structures(UnitTypeId.FORGE).ready.exists and self.game.units(UnitTypeId.STALKER) and self.game.structures(UnitTypeId.FORGE).ready.first.is_idle:
            if self.game.already_pending_upgrade(UpgradeId.PROTOSSGROUNDWEAPONSLEVEL1) == 0 and self.game.can_afford(UpgradeId.PROTOSSGROUNDWEAPONSLEVEL1) and self.game.units(UnitTypeId.STALKER).ready:
                bay = self.game.structures(UnitTypeId.FORGE).ready.first
                bay.research(UpgradeId.PROTOSSGROUNDWEAPONSLEVEL1)
            elif self.game.already_pending_upgrade(UpgradeId.PROTOSSGROUNDARMORSLEVEL1 ) == 0 and self.game.can_afford(UpgradeId.PROTOSSGROUNDARMORSLEVEL1) and self.game.units(UnitTypeId.STALKER).ready:
                bay = self.game.structures(UnitTypeId.FORGE).ready.first
                bay.research(UpgradeId.PROTOSSGROUNDARMORSLEVEL1 )