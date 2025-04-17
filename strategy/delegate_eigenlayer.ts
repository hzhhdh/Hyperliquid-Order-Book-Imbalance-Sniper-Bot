import { ethers } from "ethers";
import DelegationManagerABI from "./abis/DelegationManager.json";

async function delegateToOperator() {
  const provider = new ethers.providers.JsonRpcProvider(process.env.RPC_URL);
  const wallet = new ethers.Wallet(process.env.PRIVATE_KEY, provider);
  const delegation = new ethers.Contract(
    "0xDELEGATION_MANAGER_ADDRESS",
    DelegationManagerABI,
    wallet
  );

  // Approve first if needed
  const approveTx = await delegation.tokenContract.approve(
    delegation.address,
    ethers.utils.parseEther("10")
  );
  await approveTx.wait();

  // Delegate 10 stETH to operator
  const tx = await delegation.delegateTo("0xOPERATOR_ADDRESS", ethers.utils.parseEther("10"));
  console.log("EigenLayer delegate tx:", tx.hash);
}
delegateToOperator();
