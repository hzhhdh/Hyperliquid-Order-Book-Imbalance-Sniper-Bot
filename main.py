import asyncio
from .risk_management import RiskManager
from .hyperliquid_api import HyperLiquidAPI

class HyperGuard:
    def __init__(self):
        self.risk = RiskManager()
        self.api = HyperLiquidAPI()
    
    async def run(self):
        """Main event loop"""
        while True:
            positions = self.api.get_all_positions()
            for pos in positions:
                self._check_liquidation_risk(pos)
            await asyncio.sleep(60)

if __name__ == "__main__":
    bot = HyperGuard()
    asyncio.run(bot.run())
