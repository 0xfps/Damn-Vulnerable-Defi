from brownie import Attack, SideEntranceLenderPool, accounts, network, config

def deploy():
   account = getAccount()

   print("Deploying...")

   deploy = SideEntranceLenderPool.deploy({"from": account}, publish_source=True)
   print(f"Deployed at {deploy.address} !!!\n\n")


   deploy2 = Attack.deploy({"from": account}, publish_source=True)
   print(f"Deployed at {deploy2.address} !!!")
   #deploy = Sellable.deploy({"from": account}, publish_source=False)
   

   title = "Sellable"
   link = "https://rinkeby.etherscan.io/address/"
   with open("../Deployment Address.txt", "a+") as file:
      file.write(f"SideEntranceLenderPool => {link}{deploy.address}\n\n")
      file.write(f"Attack => {link}{deploy2.address}\n\n")


def getAccount():
   if network.show_active() == "development":
      return accounts[0]
   else:
      return accounts.add(config['wallet']['from_key'])

def main():
   deploy()