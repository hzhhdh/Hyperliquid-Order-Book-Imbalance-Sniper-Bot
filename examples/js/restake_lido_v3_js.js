const wallet = new ethers.Wallet(PRIVATE_KEY, provider);
const vault = new ethers.Contract(LIDO_V3_ADDR, VAULT_ABI, wallet);
await vault.deposit({ value: ethers.utils.parseEther("1") });
