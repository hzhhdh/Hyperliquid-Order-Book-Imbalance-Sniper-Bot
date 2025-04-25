// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;
import "./HoneypotChecker.sol";
import "./ArbitrageExecutor.sol";
import "./LiquidityManager.sol";

contract ManualMaxBot {
    address public owner;
    HoneypotChecker public honeypotChecker;
    ArbitrageExecutor public arbitrageExecutor;
    LiquidityManager public liquidityManager;

    constructor(address _honeypotChecker, address _arbitrageExecutor, address _liquidityManager) {
        owner = msg.sender;
        honeypotChecker = HoneypotChecker(_honeypotChecker);
        arbitrageExecutor = ArbitrageExecutor(_arbitrageExecutor);
        liquidityManager = LiquidityManager(_liquidityManager);
    }

    modifier onlyOwner() {
        require(msg.sender == owner, "Unauthorized");
        _;
    }

    function executeStrategy(
        address token,
        uint256 amount,
        uint256 minProfit
    ) external onlyOwner {
        require(!honeypotChecker.isHoneypot(token), "Token is a honeypot");
        arbitrageExecutor.executeArbitrage(token, amount, minProfit);
    }
}
