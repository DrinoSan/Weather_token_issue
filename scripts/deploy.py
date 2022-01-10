from brownie import network, config, Oracle, FeelSafeToken
from scripts.helpful_scripts import get_account, get_contract


def deploy():
    account = get_account()
    feelSafeToken = FeelSafeToken.deploy({"from": account})
    print(f"Feel Safe Token has been deployed: {feelSafeToken.address}")
    oracle = Oracle.deploy(
        get_contract("link_token"),
        feelSafeToken.address,
        {"from": account},
        publish_source=config["networks"][network.show_active()]["verify"],
    )
    print(f"Contract has beed deployed oracle: {oracle.address}")
    transfer_tx = feelSafeToken.transfer(
        oracle.address, feelSafeToken.totalSupply() - 100, {"from": account}
    )
    transfer_tx.wait(1)


def main():
    deploy()
