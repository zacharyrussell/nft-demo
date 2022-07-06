from brownie import network, AdvancedCollectible
import pytest
from scripts.helpful_scripts import LOCAL_BLOCKCHAIN_ENVIROMENTS
from scripts.advanced_collectible.deploy_and_create import (
    deploy_and_create,
    get_contract,
    get_account,
)
import time


def test_can_create_advanced_collectible_integration():
    # deploy, create NFT, get random breed back
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIROMENTS:
        pytest.skip("only for integration testing")

    account = get_account()
    advanced_collectible, creation_transaction = deploy_and_create()
    time.sleep(180)
    assert advanced_collectible.tokenCounter() == 1
