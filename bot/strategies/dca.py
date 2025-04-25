import schedule
import ccxt

binance = ccxt.binance({'apiKey': 'KEY', 'secret': 'SECRET'})

def daily_buy():
    binance.create_market_buy_order('BTC/USDT', 100)  # $100 daily

schedule.every().day.at("09:00").do(daily_buy)
while True:
    schedule.run_pending()

