from brownie import ReceiverUnstoppable, accounts, network, config

def deploy():
   account = getAccount()

   print("Deploying...")

   deploy = ReceiverUnstoppable.deploy("0x076b15252eed74F93f99d4b5a714B343351343cd", {"from": account}, publish_source=False)
   #deploy = ReceiverUnstoppable.deploy({"from": account}, publish_source=False)


   print(f"Deployed at {deploy.address} !!!")

   title = "ReceiverUnstoppable"
   link = "https://rinkeby.etherscan.io/address/"
   with open("../Deployment Address.txt", "a+") as file:
      file.write(f"{title} => {link}{deploy.address}\n\n")


def getAccount():
   if network.show_active() == "development":
      return accounts[0]
   else:
      return accounts.add(config['wallet']['from_key'])

def main():
   deploy()