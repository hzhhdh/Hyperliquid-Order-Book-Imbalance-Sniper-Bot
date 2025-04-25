// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract GasEstimator {
    function estimateOptimalGas() public view returns (uint256) {
        return tx.gasprice * 120 / 100; // 20% premium
    }
}
