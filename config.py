CONFIG = {
    # Capital and identity (for higher capital users)
    "CAPITAL": 100_000,  # Capital in USD; used for position sizing, risk limits, etc.
    "YOUR_ADDRESS": "0xYourWalletAddress",  # Your public wallet address
    "PRIVATE_KEY": "YOUR_PRIVATE_KEY",  # NEVER share or hardcode in production; use secure vaults

    # --- Subscription & Network Parameters ---
    "RPC_PROVIDER_URL": "https://mainnet.infura.io/v3/YOUR_INFURA_KEY",
    "FILTER_TYPE": "pending",
    "POLL_INTERVAL": 1.0,  # seconds between polling

    # --- Custom RPC & Network Selection ---
    "AVAILABLE_NETWORKS": {
        "Ethereum": "https://mainnet.infura.io/v3/YOUR_INFURA_KEY",
        "Binance Smart Chain": "https://bsc-dataseed.binance.org/",
        "Polygon": "https://polygon-rpc.com/",
        "Arbitrum": "https://arb1.arbitrum.io/rpc",
        "Avalanche": "https://api.avax.network/ext/bc/C/rpc",
        "Optimism": "https://mainnet.optimism.io",
        # Add additional networks: Base, Starknet, AAVE, etc.
    },
    "CUSTOM_RPC_ENDPOINTS": {},  # Custom endpoints can be added here by the user.
    "SELECTED_NETWORK": "Ethereum",  # Default network; change as desired.

    # --- Token Selection ---
    "BUY_TOKEN_ADDRESS": "0xC02aaa39b223FE8D0a0e5C4F27eAD9083C756Cc2",  # e.g., WETH on Ethereum
    "TARGET_TOKEN_ADDRESS": "0xTokenAddressToSnipe",  # Set this to the token you wish to buy

    # --- DEX Selection ---
    "AVAILABLE_DEXES": {
        "Uniswap": {
            "router_address": "0x7a250d5630B4cF539739dF2C5dAcb4c659F2488D",
            "abi_file": "UniswapV2RouterABI.json"
        },
        "SushiSwap": {
            "router_address": "0xd9e1ce17f2641f24aE83637ab66a2cca9C378B9F",
            "abi_file": "SushiSwapRouterABI.json"
        },
        # Additional DEXes can be added with their router addresses and ABI files.
    },
    "SELECTED_DEX": "Uniswap",  # Default DEX

    # --- Mempool Monitoring / Filtering Parameters ---
    "WHALE_THRESHOLD_VALUE": 5 * 10**18,  # e.g., 5 ETH in Wei
    "TARGET_FUNCTION_IDENTIFIER": "swapExactETHForTokens",
    "SLIPPAGE_TOLERANCE_FACTOR": 0.95,  # Acceptable output is 95% of expected tokens
    "ADDRESS_WHITELIST": [],  # Optional list of trusted whale addresses
    "ADDRESS_BLACKLIST": [],  # Optional list of addresses to ignore

    # --- Signal Generation Parameters ---
    "SIGNAL_COOLDOWN_PERIOD": 1.0,  # seconds cooldown between signals
    "VERIFICATION_DELAY_THRESHOLD": 200,  # milliseconds delay allowed

    # --- Order Execution Parameters ---
    "TRADE_AMOUNT": int(0.5 * 10**18),  # Trade amount in Wei (example: 0.5 ETH)
    "GAS_LIMIT": 300000,
    "GAS_PREMIUM_MULTIPLIER": 1.10,  # 10% premium gas fee multiplier
    "TRANSACTION_DEADLINE_OFFSET": 60,  # seconds before order expires
    # TWAP settings for order splitting:
    "TWAP_ENABLE": True,      # Enable TWAP order splitting module
    "TWAP_SLICES": 5,         # Split the order into 5 slices
    "TWAP_INTERVAL": 60,      # 60 seconds between each slice
    "TWAP_MIN_ORDER_SIZE": None,  # Calculated as TRADE_AMOUNT / TWAP_SLICES

    # --- Risk Management Parameters ---
    "STOP_LOSS_LEVEL": 0.90,  # 10% drop triggers stop loss
    "TAKE_PROFIT_LEVEL": 1.20,  # 20% rise triggers take profit
    "TRAILING_STOP_DISTANCE": 0.95,  # Trailing stop set at 5% below the high

    # --- Logging & Monitoring ---
    "LOG_LEVEL": "DEBUG",  # or INFO in production
    "POLLING_INTERVAL_FOR_METRICS": 1.0,  # seconds
    "MAX_RETRY_ATTEMPTS": 3,

    # --- Network & Environmental ---
    "NETWORK_CONGESTION_THRESHOLD": 150 * 10**9,  # e.g., 150 Gwei threshold
}
