from pydantic import BaseSettings, SecretStr

class Settings(BaseSettings):
    # HyperLiquid API
    HYPERLIQUID_API_KEY: SecretStr
    HYPERLIQUID_API_SECRET: SecretStr
    
    # Binance API for hedging
    BINANCE_API_KEY: SecretStr
    BINANCE_API_SECRET: SecretStr
    
    # Risk Parameters
    MAX_LEVERAGE: int = 10
    VOLATILITY_THRESHOLD: float = 5.0
    STOP_LOSS_TRIGGER: float = 15.0
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

config = Settings()
