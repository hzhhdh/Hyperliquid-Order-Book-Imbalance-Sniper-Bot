import React, { createContext, useState } from "react";

export const BotContext = createContext();

export function BotProvider({ children }) {
    const [wallet, setWallet] = useState(null);
    return (
        <BotContext.Provider value={{ wallet, setWallet }}>
            {children}
        </BotContext.Provider>
    );
}
