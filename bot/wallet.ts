import { ethers } from 'ethers';

// 1. Connect to BSC via WebSocket for instant event feeds
const wsProvider = new ethers.providers.WebSocketProvider(
  'wss://bsc-ws-node.nariox.org:443'
); // WSS endpoint with low latency :contentReference[oaicite:0]{index=0}

// 2. Create a signer from a local private key (ensure ENV-encrypted!)
const wallet = new ethers.Wallet(process.env.PRIVATE_KEY || '', wsProvider); // Key loaded from .env :contentReference[oaicite:1]{index=1}
