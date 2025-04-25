import React from "react";

export default function StrategyBuilder() {
    const [rules, setRules] = React.useState([]);

    const addRule = (condition, action) => {
        setRules([...rules, { condition, action }]);
    };

    return (
        <div>
            {rules.map((rule, i) => (
                <div key={i}>{rule.condition} → {rule.action}</div>
            ))}
        </div>
    );
}
