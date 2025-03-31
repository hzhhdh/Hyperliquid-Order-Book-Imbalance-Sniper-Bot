# arbitrage_router.py
from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class ArbitrageRequest(BaseModel):
    dex_price: float
    cex_price: float
    amount: float

@router.post("/arbitrage")
async def calculate_arbitrage(request: ArbitrageRequest):
    spread = (request.cex_price - request.dex_price) / request.dex_price
    profit = request.amount * spread
    return {"spread": f"{spread:.2%}", "potential_profit": profit}
