// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;
import "./interfaces/IUniswapV3.sol";

contract LiquidityManager {
    IUniswapV3 public uniswap;

    constructor(address _uniswap) {
        uniswap = IUniswapV3(_uniswap);
    }

    function adjustRange(
        address tokenA,
        address tokenB,
        int24 lowerTick,
        int24 upperTick
    ) external {
        uniswap.updateRange(tokenA, tokenB, lowerTick, upperTick);
    }
}
