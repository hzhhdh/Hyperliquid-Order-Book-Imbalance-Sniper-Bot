pragma solidity ^0.8.0;
interface ICurve { function get_dy(int128 i, int128 j, uint256 dx) external view returns (uint256); }
contract Arbitrage {
    ICurve curve;
    function execute(uint256 amount) external { /* logic */ }
}
