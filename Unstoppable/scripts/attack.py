from brownie import UnstoppableLender, ReceiverUnstoppable, accounts, network, config

def deploy():
   account = getAccount()
   lender = UnstoppableLender[-1]
   receiver = ReceiverUnstoppable[-1]

	# To break the contract, simply fund it with tokens from the address of the selected tokens.
	# This will unset the line 43, which will be hard to fix.
	# assert(poolBalance == balanceBefore);
   
   #deploy = UnstoppableLender.deploy({"from": account}, publish_source=False)


def getAccount():
   if network.show_active() == "development":
      return accounts[0]
   else:
      return accounts.add(config['wallet']['from_key'])

def main():
   deploy()