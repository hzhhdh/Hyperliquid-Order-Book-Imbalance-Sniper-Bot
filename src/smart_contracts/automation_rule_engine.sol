// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import "@chainlink/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol";

contract AutomationRuleEngine {
    address public owner;
    AggregatorV3Interface public priceFeed;

    struct Rule {
        address protocol;
        bytes actionData;
        uint256 threshold;
        bool active;
    }

    mapping(uint256 => Rule) public rules;
    uint256 public ruleCount;

    event RuleExecuted(uint256 ruleId, address protocol, bytes actionData);
    event RuleCreated(uint256 ruleId, address protocol, uint256 threshold);

    constructor(address _priceFeed) {
        owner = msg.sender;
        priceFeed = AggregatorV3Interface(_priceFeed);
    }

    modifier onlyOwner() {
        require(msg.sender == owner, "Not owner");
        _;
    }

    function createRule(address _protocol, bytes calldata _actionData, uint256 _threshold) external onlyOwner {
        rules[ruleCount] = Rule(_protocol, _actionData, _threshold, true);
        emit RuleCreated(ruleCount, _protocol, _threshold);
        ruleCount++;
    }

    function executeRule(uint256 _ruleId) external {
        Rule storage rule = rules[_ruleId];
        require(rule.active, "Rule inactive");

        (, int256 price,,,) = priceFeed.latestRoundData();
        require(uint256(price) > rule.threshold, "Threshold not met");

        (bool success,) = rule.protocol.call(rule.actionData);
        require(success, "Action failed");

        emit RuleExecuted(_ruleId, rule.protocol, rule.actionData);
    }

    function toggleRule(uint256 _ruleId, bool _active) external onlyOwner {
        rules[_ruleId].active = _active;
    }
}
