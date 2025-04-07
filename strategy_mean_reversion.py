class MeanReversionStrategy(BaseStrategy):
    def generate_signals(self):
        """
        Generates signals based on price deviation from a moving average.
        Customizable parameters: window, threshold.
        :return: DataFrame with buy (1) and sell (-1) signals.
        """
        window = self.params.get('window', 30)
        threshold = self.params.get('threshold', 2.0)

        signals = pd.DataFrame(index=self.data.index)
        signals['price'] = self.data['price']
        signals['ma'] = self.data['price'].rolling(window=window).mean()
        signals['std'] = self.data['price'].rolling(window=window).std()
        signals['z_score'] = (self.data['price'] - signals['ma']) / signals['std']
        signals['signal'] = 0.0
        signals.loc[signals['z_score'] > threshold, 'signal'] = -1.0  # sell signal
        signals.loc[signals['z_score'] < -threshold, 'signal'] = 1.0  # buy signal
        logger.info("MeanReversionStrategy signals generated.")
        return signals

if __name__ == "__main__":
    strategy = MeanReversionStrategy(market_data, window=20, threshold=1.5)
    signals = strategy.generate_signals()
    print(signals.tail())
