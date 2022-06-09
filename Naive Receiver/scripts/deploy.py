from brownie import FlashLoanReceiver, NaiveReceiverLenderPool, Attack, accounts, network, config

def deploy():
   account = getAccount()

   print("Deploying...")

   deploy2 = NaiveReceiverLenderPool.deploy({"from": account}, publish_source=True)
   print(f"Deployed at {deploy2.address} !!!")

   deploy = FlashLoanReceiver.deploy(deploy2.address, {"from": account}, publish_source=True)
   print(f"Deployed at {deploy.address} !!!")

   deploy3 = Attack.deploy({"from": account}, publish_source=True)
   print(f"Deployed at {deploy3.address} !!!")
   #deploy = Sellable.deploy({"from": account}, publish_source=False)


   title = "Sellable"
   link = "https://rinkeby.etherscan.io/address/"
   with open("../Deployment Address.txt", "a+") as file:
      file.write(f"FlashLoanReceiver => {link}{deploy.address}\n\n")
      file.write(f"NaiveReceiverLenderPool => {link}{deploy2.address}\n\n")
      file.write(f"Attack => {link}{deploy3.address}\n\n")


def getAccount():
   if network.show_active() == "development":
      return accounts[0]
   else:
      return accounts.add(config['wallet']['from_key'])

def main():
   deploy()