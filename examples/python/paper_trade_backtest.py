from barter_rs import Backtester
bt = Backtester(strategy="delta_neutral", data="historical.csv")
results = bt.run()
print(results.summary())
