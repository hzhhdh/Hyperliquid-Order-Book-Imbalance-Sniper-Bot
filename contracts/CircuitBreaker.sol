// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract CircuitBreaker {
    bool public stopped;

    modifier stopInEmergency {
        require(!stopped, "Circuit breaker triggered");
        _;
    }

    function toggleCircuitBreaker() external {
        stopped = !stopped;
    }
}
