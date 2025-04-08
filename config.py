CONFIG = {
    # --- Subscription & Network Parameters ---
    "RPC_PROVIDER_URL": "https://mainnet.infura.io/v3/YOUR_INFURA_KEY",
    "FILTER_TYPE": "pending",
    "POLL_INTERVAL": 1.0,  # seconds

    # --- Custom RPC & Network Selection ---
    "AVAILABLE_NETWORKS": {
        "Ethereum": "https://mainnet.infura.io/v3/YOUR_INFURA_KEY",
        "Binance Smart Chain": "https://bsc-dataseed.binance.org/",
        "Polygon": "https://polygon-rpc.com/",
        "Arbitrum": "https://arb1.arbitrum.io/rpc",
        # Add additional networks: Base, Starknet, Optimism, Avalanche, etc.
    },
    "CUSTOM_RPC_ENDPOINTS": {},  # User can add custom endpoints here
    "SELECTED_NETWORK": "Ethereum",  # Default network

    # --- Token Selection ---
    "BUY_TOKEN_ADDRESS": "0xC02aaa39b223FE8D0a0e5C4F27eAD9083C756Cc2",  # Default: WETH on Ethereum
    "TARGET_TOKEN_ADDRESS": "0xTokenAddressToSnipe",  # To be set by user

    # --- DEX Selection ---
    "AVAILABLE_DEXES": {
        "Uniswap": {"router_address": "0x7a250d5630B4cF539739dF2C5dAcb4c659F2488D", "abi_file": "UniswapV2RouterABI.json"},
        "SushiSwap": {"router_address": "0xd9e1ce17f2641f24aE83637ab66a2cca9C378B9F", "abi_file": "SushiSwapRouterABI.json"},
        # Add more DEX details as required.
    },
    "SELECTED_DEX": "Uniswap",

    # --- Mempool Monitoring / Filtering Parameters ---
    "WHALE_THRESHOLD_VALUE": 5 * 10 ** 18,  # e.g., 5 ETH in Wei
    "TARGET_FUNCTION_IDENTIFIER": "swapExactETHForTokens",
    "SLIPPAGE_TOLERANCE_FACTOR": 0.95,
    "ADDRESS_WHITELIST": [],
    "ADDRESS_BLACKLIST": [],

    # --- Signal Generation Parameters ---
    "SIGNAL_COOLDOWN_PERIOD": 1.0,  # seconds
    "VERIFICATION_DELAY_THRESHOLD": 200,  # milliseconds

    # --- Order Execution Parameters ---
    "TRADE_AMOUNT": 0.5 * 10 ** 18,  # 0.5 ETH in Wei
    "GAS_LIMIT": 300000,
    "GAS_PREMIUM_MULTIPLIER": 1.10,  # 10% gas premium
    "TRANSACTION_DEADLINE_OFFSET": 60,  # seconds
    "TWAP_ENABLE": True,
    "TWAP_SLICES": 5,
    "TWAP_INTERVAL": 60,  # seconds between slices
    "TWAP_MIN_ORDER_SIZE": None,  # Calculated as TRADE_AMOUNT/TWAP_SLICES (set at runtime)

    # --- Risk Management Parameters ---
    "STOP_LOSS_LEVEL": 0.90,  # 10% drop triggers stop loss
    "TAKE_PROFIT_LEVEL": 1.20,  # 20% gain triggers take profit
    "TRAILING_STOP_DISTANCE": 0.95,  # 5% trailing stop

    # --- Logging & Monitoring ---
    "LOG_LEVEL": "DEBUG",
    "POLLING_INTERVAL_FOR_METRICS": 1.0,
    "MAX_RETRY_ATTEMPTS": 3,

    # --- Network and Environmental Parameters ---
    "NETWORK_CONGESTION_THRESHOLD": 150 * 10 ** 9,  # e.g. 150 Gwei threshold
}
