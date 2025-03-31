from fastapi import HTTPException

async def check_pool_eligibility(apr: float, il: float):
    if apr < 0.2 or il > 0.05:
        raise HTTPException(400, "Pool doesn't meet requirements")
    return {"approved": True}
