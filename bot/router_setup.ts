// PancakeSwap V2 Router address on BSC Mainnet
const PANCAKE_ROUTER_ADDRESS = '0x10ED43C718714eb63d5aA57B78B54704E256024E'; :contentReference[oaicite:2]{index=2}

// Minimal ERC20 ABI for approvals & balances
const ERC20_ABI = [
  'function approve(address spender, uint256 amount) external returns (bool)',
  'function balanceOf(address owner) external view returns (uint256)'
];

// UniswapV2Router02 ABI slice (swap functions)
const ROUTER_ABI = [
  'function swapExactETHForTokensSupportingFeeOnTransferTokens(uint amountOutMin, address[] calldata path, address to, uint deadline) external payable',
  'function swapExactTokensForETHSupportingFeeOnTransferTokens(uint amountIn, uint amountOutMin, address[] calldata path, address to, uint deadline) external'
]; :contentReference[oaicite:3]{index=3}

const router = new ethers.Contract(
  PANCAKE_ROUTER_ADDRESS,
  ROUTER_ABI,
  wallet
);
