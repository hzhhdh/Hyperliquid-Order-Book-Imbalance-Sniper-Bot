async def monitor_discord(servers: list):
    messages = await fetch_discord_messages(servers)
    for msg in messages:
        if is_token_launch(msg):
            await snipe_token(msg.contract_address)
