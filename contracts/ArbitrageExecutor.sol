// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;
import "./interfaces/IUniswapV3.sol";
import "./interfaces/IdYdX.sol";

contract ArbitrageExecutor {
    IUniswapV3 public uniswap;
    IdYdX public dydx;

    constructor(address _uniswap, address _dydx) {
        uniswap = IUniswapV3(_uniswap);
        dydx = IdYdX(_dydx);
    }

    function executeArbitrage(address token, uint256 amount, uint256 minProfit) external {
        uint256 uniswapPrice = uniswap.getPrice(token);
        uint256 dydxPrice = dydx.getPrice(token);
        if (uniswapPrice > dydxPrice + minProfit) {
            uniswap.buy(token, amount);
            dydx.short(token, amount);
        }
    }
}
