// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

interface IUniswapV3 {
    function getPrice(address token) external view returns (uint256);
    function buy(address token, uint256 amount) external;
    function updateRange(address tokenA, address tokenB, int24 lowerTick, int24 upperTick) external;
}
