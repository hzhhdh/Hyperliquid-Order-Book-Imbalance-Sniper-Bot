async def monitor_x(accounts: list):
    posts = await fetch_x_posts(accounts)
    for post in posts:
        if post["reputation"] > threshold:
            await execute_trade(post.token)
