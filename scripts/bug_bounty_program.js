// Example: Smart contract for bug bounty payouts
contract BugBounty {
    mapping(address => uint256) public rewards;

    function reportBug(string memory description) public {
        // Validate bug report
        rewards[msg.sender] += 1000; // Reward in tokens
    }

    function claimReward() public {
        uint256 reward = rewards[msg.sender];
        require(reward > 0, "No rewards to claim");
        // Transfer tokens to reporter
        rewards[msg.sender] = 0;
    }
}
