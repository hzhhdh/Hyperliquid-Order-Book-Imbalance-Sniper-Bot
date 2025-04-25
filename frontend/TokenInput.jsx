import React from "react";

export default function TokenInput({ onTokenSelect }) {
    const [token, setToken] = React.useState("");

    return (
        <input
            type="text"
            placeholder="Search tokens..."
            value={token}
            onChange={(e) => {
                setToken(e.target.value);
                onTokenSelect(e.target.value);
            }}
        />
    );
}
