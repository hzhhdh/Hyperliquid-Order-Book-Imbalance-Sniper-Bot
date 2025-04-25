// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract HoneypotChecker {
    function isHoneypot(address token) external view returns (bool) {
        (bool success,) = token.staticcall(abi.encodeWithSignature("transfer(address,uint256)", address(this), 0));
        return !success; // If transfer fails, likely a honeypot
    }
}
