from brownie import network, config, Oracle, FeelSafeToken
from scripts.helpful_scripts import fund_with_link, get_account, get_contract

KEEP_FEEL_SAFE_TOKEN = 100


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
        oracle.address,
        feelSafeToken.totalSupply() - KEEP_FEEL_SAFE_TOKEN,
        {"from": account},
    )
    transfer_tx.wait(1)

    link_tx = fund_with_link(oracle.address)
    link_tx.wait(1)

    return oracle, feelSafeToken


def main():
    deploy()
