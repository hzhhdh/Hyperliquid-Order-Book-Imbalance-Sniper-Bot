from fastapi import WebSocket

async def price_alert(websocket: WebSocket):
    await websocket.accept()
    while True:
        price = get_live_price()  # Your logic
        if price > 3500:
            await websocket.send_text("ETH price exceeded $3500!")
