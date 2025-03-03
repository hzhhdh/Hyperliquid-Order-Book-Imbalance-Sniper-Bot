// Example: DAO voting for protocol changes
contract Governance {
    mapping(address => uint256) public votes;

    function vote(bool approve) public {
        votes[msg.sender] = approve ? 1 : 0;
    }

    function executeChange() public {
        require(getApproval() > 50, "Not enough votes");
        // Execute protocol change
    }

    function getApproval() public view returns (uint256) {
        // Calculate approval percentage
    }
}
