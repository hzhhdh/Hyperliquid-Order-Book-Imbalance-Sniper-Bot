// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;
import "./IChainlink.sol";

contract PriceOracle {
    IChainlink public chainlink;

    constructor(address _chainlink) {
        chainlink = IChainlink(_chainlink);
    }

    function getETHPrice() public view returns (uint256) {
        return uint256(chainlink.latestAnswer());
    }
}
