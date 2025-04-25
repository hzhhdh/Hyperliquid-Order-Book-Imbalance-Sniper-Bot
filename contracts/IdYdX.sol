// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

interface IdYdX {
    function getPrice(address token) external view returns (uint256);
    function short(address token, uint256 amount) external;
}
