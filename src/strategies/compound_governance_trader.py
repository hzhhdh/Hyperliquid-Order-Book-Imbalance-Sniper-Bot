async def trade_on_governance():
    proposals = await fetch_compound_proposals()
    for proposal in proposals:
        if proposal["status"] == "passed" and is_favorable(proposal):
            await execute_buy_trade("COMP", amount=0.1)
