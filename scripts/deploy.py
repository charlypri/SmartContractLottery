from brownie import Lottery, network, config
from scripts.helpful_scripts import (
    get_account,
    get_contract,
    LOCAL_BLOCKCHAIN_ENVIRONMENTS,
    fund_with_link,
)
from web3 import Web3
import time


def deploy_lottery():
    # Llamamos a nuestro helpful method que checkea en que red estamos conectados si local, o testnets y nos proporciona nuestro address dentro de la red
    account = get_account()    
    lottery = Lottery.deploy(
        get_contract("eth_usd_price_feed").address,
        get_contract("vrf_coordinator").address,
        get_contract("link_token").address,
        config["networks"][network.show_active()]["fee"],
        config["networks"][network.show_active()]["keyhash"],
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("verify", False),
    )
    print("Deployed lottery!")
    return lottery

def start_lottery():
    account = get_account()    
    lottery = Lottery[-1]
    starting_tx = lottery.startLottery({"from":account})
    starting_tx.wait(1)
    print("Lottery is started!!")

def enter_lottery():
    account = get_account()    
    lottery = Lottery[-1]
    value = lottery.getEntranceFee() + 10000000
    enter_tx = lottery.enter({"from":account, "value":value})
    enter_tx.wait(1)
    print("You entered the lottery!!")

def end_lottery():
    account = get_account()    
    lottery = Lottery[-1]
    # We need to fund the Lottery.sol contract because the contrat needs to make some transactions to get the random number from the other contract (El Contrato de chainlink)
    fund_link = fund_with_link(lottery.address)
    fund_link.wait(1)
    end_tx = lottery.endLottery({"from":account})
    end_tx.wait(1)
    time.sleep(120)
    print(str(lottery.recentWinner()) + "is the winner!!!")


def main():
    deploy_lottery()
    start_lottery()
    enter_lottery()
    end_lottery()
