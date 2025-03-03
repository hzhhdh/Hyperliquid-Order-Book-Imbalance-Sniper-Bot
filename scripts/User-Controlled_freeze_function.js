// Example: Allow users to freeze their own funds
contract UserFreeze {
    mapping(address => bool) public frozen;

    function freeze() public {
        frozen[msg.sender] = true;
    }

    function unfreeze() public {
        frozen[msg.sender] = false;
    }
}
