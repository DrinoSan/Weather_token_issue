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
    assert (
        feelSafeToken.balanceOf(oracle.address)
        == feelSafeToken.totalSupply() - KEEP_FEEL_SAFE_TOKEN
    )

    withdraw_feel_safe_token_tx = oracle.withdraw_feel_safe_token()
    withdraw_feel_safe_token_tx.wait(1)

    print(f"Current amount of feelSafeToken: {feelSafeToken.balanceOf(oracle.address)}")
    assert feelSafeToken.balanceOf(oracle.address) == 0
