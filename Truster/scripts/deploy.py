from brownie import TrusterLenderPool, Attack, accounts, network, config

def deploy():
   account = getAccount()

   print("Deploying...")

   deploy = TrusterLenderPool.deploy("0xa1Cba00d6e99f52B8cb5f867a6f2db0F3ad62276", {"from": account}, publish_source=True)
   deploy2 = Attack.deploy({"from": account}, publish_source=True)
   #deploy = Sellable.deploy({"from": account}, publish_source=False)


   print(f"Deployed at {deploy.address} !!!")

   title = "Truster"
   link = "https://rinkeby.etherscan.io/address/"
   with open("../Deployment Address.txt", "a+") as file:
      file.write(f"TrusterLenderPool => {link}{deploy.address}\n\n")
      file.write(f"Attack => {link}{deploy2.address}\n\n")


def getAccount():
   if network.show_active() == "development":
      return accounts[0]
   else:
      return accounts.add(config['wallet']['from_key'])

def main():
   deploy()