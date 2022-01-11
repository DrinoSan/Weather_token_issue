from web3 import Web3
from scripts.helpful_scripts import fund_with_link, get_account, get_contract
from scripts.chain_informations import LOCAL_BLOCKCHAIN_ENVIRONMENTS
from scripts.deploy import deploy, KEEP_FEEL_SAFE_TOKEN
from brownie import network, LinkToken
import pytest


def test_fund_with_link():
    # deploy token
    # deploy oracle
    # test if oracle was funded with link
    # test if transfer from tokens to oracle worked

    # Arrange
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip()

    # Act
    oracle, feelSafeToken = deploy()

    link = get_contract("link_token")

    # Assert
    print(f"Current amount of feelSafeToken: {feelSafeToken.balanceOf(oracle.address)}")
    assert feelSafeToken.balanceOf(oracle.address) > 0

    # Oracle contract has already been funded in the deploy script
    print(f"Current amount of Link: {link.balanceOf(oracle.address)}")
    assert link.balanceOf(oracle.address) == Web3.toWei(0.3, "ether")

    # Getting total suply
    print(f"FeelSafeToken totalSupply: {feelSafeToken.totalSupply()}")
    # the 100 is amount we did not take. Defined in deploy script... Should parameterize it...
    assert (
        feelSafeToken.balanceOf(oracle.address) + KEEP_FEEL_SAFE_TOKEN
        == feelSafeToken.totalSupply()
    )
