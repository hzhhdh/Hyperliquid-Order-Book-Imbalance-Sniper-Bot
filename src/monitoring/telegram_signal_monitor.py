async def monitor_telegram(channels: list):
    messages = await fetch_telegram_messages(channels)
    for msg in messages:
        if is_contract_address(msg):
            await trigger_trade(msg.contract_address)
