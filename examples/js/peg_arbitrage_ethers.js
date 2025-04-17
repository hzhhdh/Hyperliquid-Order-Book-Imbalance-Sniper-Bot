import { ethers } from "ethers";
const provider = new ethers.providers.WebSocketProvider(process.env.ALCHEMY);
const curve = new ethers.Contract(CURVE_ADDR, ABI, provider);
curve.on("TokenExchange", (i,j,dx,dy) => { if ((dy/dx-1)>0.005) arbitrage(); });
