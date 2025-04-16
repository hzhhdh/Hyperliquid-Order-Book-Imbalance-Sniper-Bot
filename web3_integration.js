const Web3 = require('web3');
const fs = require('fs');

// Configure your provider (e.g., from MetaMask or an Infura endpoint)
const providerURL = process.env.ETH_RPC_ENDPOINT || "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID";
const web3 = new Web3(new Web3.providers.HttpProvider(providerURL));

// Load the ABI and contract address
const abi = JSON.parse(fs.readFileSync('./TokenTraderABI.json', 'utf8'));
const contractAddress = "0xYourDeployedContractAddress"; // Replace with actual address

// Create contract instance
const tokenTrader = new web3.eth.Contract(abi, contractAddress);

// Example account that will interact with the contract
const account = "0xYourAccountAddress"; // Replace with your account address

// PURCHASE FUNCTION
async function purchaseTokens(tokenAmount) {
    // Calculate the total cost; here we assume price per token = 0.001 ETH = 1e15 wei.
    const pricePerToken = web3.utils.toBN("1000000000000000"); // 0.001 ETH in wei
    const totalCost = pricePerToken.mul(web3.utils.toBN(tokenAmount));
  
    try {
      const receipt = await tokenTrader.methods.purchaseToken(tokenAmount).send({
          from: account,
          value: totalCost
      });
      console.log("Purchase successful:", receipt);
    } catch (error) {
      console.error("Error during purchase:", error);
    }
}

// STRATEGY EXECUTION FUNCTION
async function executeStrategy(strategyName) {
    try {
      const result = await tokenTrader.methods.executeStrategy(strategyName).send({from: account});
      console.log("Strategy executed:", result);
    } catch (error) {
      console.error("Error executing strategy:", error);
    }
}

// LIQUIDITY FUNCTIONS
async function depositLiquidity(amountInEth) {
    const amountInWei = web3.utils.toWei(amountInEth.toString(), 'ether');
    try {
      const receipt = await tokenTrader.methods.depositLiquidity().send({
          from: account,
          value: amountInWei
      });
      console.log("Liquidity deposited:", receipt);
    } catch (error) {
      console.error("Error depositing liquidity:", error);
    }
}

async function withdrawLiquidity(amountInEth) {
    const amountInWei = web3.utils.toWei(amountInEth.toString(), 'ether');
    try {
      const receipt = await tokenTrader.methods.withdrawLiquidity(amountInWei).send({
          from: account
      });
      console.log("Liquidity withdrawn:", receipt);
    } catch (error) {
      console.error("Error withdrawing liquidity:", error);
    }
}

// Call the functions as needed:
(async () => {
    await purchaseTokens(100);            // Purchase 100 tokens
    await executeStrategy("LIQUIDITY_INJECTION"); // Execute a defined strategy
    await depositLiquidity(0.5);          // Deposit 0.5 ETH as liquidity
    // await withdrawLiquidity(0.2);        // Uncomment to withdraw 0.2 ETH
})();
