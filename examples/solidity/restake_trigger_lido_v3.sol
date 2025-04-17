pragma solidity ^0.8.0;
interface ILido { function submit(address _referral) external payable; }
contract LidoRestake {
    ILido lido;
    function restake() external payable { lido.submit{value:msg.value}(address(this)); }
}
