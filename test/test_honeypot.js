const { expect } = require("chai");
const { ethers } = require("hardhat");

describe("HoneypotChecker", () => {
    let checker;
    before(async () => {
        const HoneypotChecker = await ethers.getContractFactory("HoneypotChecker");
        checker = await HoneypotChecker.deploy();
    });

    it("Detects honeypots", async () => {
        const honeypotToken = "0xMaliciousToken"; // Replace with actual honeypot
        expect(await checker.isHoneypot(honeypotToken)).to.be.true;
    });
});
