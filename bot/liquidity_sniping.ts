import { Interface } from 'ethers/lib/utils';

// PancakeSwap Factory and PairCreated event
const FACTORY_ADDRESS = '0xCA143Ce32Fe78f1f7019d7d551a6402fC5350c73';
const FACTORY_ABI = ['event PairCreated(address indexed token0, address indexed token1, address pair, uint)'];

const factory = new ethers.Contract(FACTORY_ADDRESS, FACTORY_ABI, wsProvider);

// Listen for new pair events to snipe immediately when liquidity appears
factory.on('PairCreated', async (token0, token1, pairAddress) => {
  console.log(`New pair: ${token0}/${token1} at ${pairAddress}`); :contentReference[oaicite:9]{index=9}

  // choose tokenOut if paired with BNB
  const tokenOut = token0 === ethers.constants.AddressZero ? token1 : token0;
  // wait for minimal liquidity
  setTimeout(() => buyToken(tokenOut, ethers.utils.parseEther('1')), 5000); // 5s delay :contentReference[oaicite:10]{index=10}
});
