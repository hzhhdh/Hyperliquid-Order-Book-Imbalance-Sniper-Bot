import React, { useState } from 'react';
import { electronAPI } from '../global';

export default function TradeTerminal() {
  const [amount, setAmount] = useState('');
  const execute = () => electronAPI.sendTrade({ amount: parseFloat(amount) });
  return (
    <div>
      <input type="number" value={amount} onChange={e => setAmount(e.target.value)} />
      <button onClick={execute}>Execute Trade</button>
    </div>
  );
}
