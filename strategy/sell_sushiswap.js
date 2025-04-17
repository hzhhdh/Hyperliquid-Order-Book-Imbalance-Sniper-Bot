import { ChainId, Token, TokenAmount, Pair, Route, Trade, TradeType } from "@sushiswap/sdk";
import { ethers } from "ethers";

const USDC = new Token(ChainId.MAINNET, "0xA0b86991...", 6);
const WETH = new Token(ChainId.MAINNET, ethers.constants.AddressZero, 18);

async function sellUSDC() {
  const provider = new ethers.providers.JsonRpcProvider(process.env.RPC_URL);
  const wallet = new ethers.Wallet(process.env.PRIVATE_KEY, provider);

  // Fetch pair and route
  const pair = await Pair.fetchData(USDC, WETH, provider);
  const route = new Route([pair], USDC, WETH);
  const trade = new Trade(route, new TokenAmount(USDC, "1000000"), TradeType.EXACT_INPUT);

  const slippageTolerance = new Percent("50", "10000"); // 0.5%
  const executionPrice = trade.executionPrice.toSignificant(6);
  const amountOutMin = trade.minimumAmountOut(slippageTolerance).raw.toString();

  const tx = await wallet.sendTransaction({
    to: "0xd9e1cE17f2641f24aE83637ab66a2cca9C378B9F", // SushiSwap router
    data: Router.swapExactTokensForETH(
      ethers.utils.parseUnits("1.0", 6), // 1 USDC
      amountOutMin,
      [USDC.address, WETH.address],
      wallet.address,
      Math.floor(Date.now() / 1000) + 300
    )
  });
  console.log("SushiSwap sell tx:", tx.hash);
}

sellUSDC();
