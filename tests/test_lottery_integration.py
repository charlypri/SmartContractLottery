from web3 import Web3
from brownie import Lottery, accounts, config, network
from scripts.helpful_scripts import LOCAL_BLOCKCHAIN_ENVIRONMENTS, get_account
from scripts.deploy import deploy_lottery
from web3 import Web3

# def test_get_entrance_fee():
#     # account = get_account()
    
#     # lottery = Lottery.deploy(
#     #     config["networks"][network.show_active()]["eth_usd_price_feed"],
#     #     {"from":account},
#     # )

#     # assert lottery.getEntranceFee() > Web3.toWei(0.016,"ether")
#     # assert lottery.getEntranceFee() < Web3.toWei(0.019,"ether")
    

#     # Arrange
#     lottery = deploy_lottery()
#     # Act
#     entrance_fee = lottery.getEntranceFee()

#     # Assert
