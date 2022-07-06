from brownie import network, AdvancedCollectible
import pytest
from scripts.helpful_scripts import LOCAL_BLOCKCHAIN_ENVIROMENTS
from scripts.advanced_collectible.deploy_and_create import (
    deploy_and_create,
    get_contract,
    get_account,
)


def test_can_create_advanced_collectible():
    # deploy, create NFT, get random breed back
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIROMENTS:
        pytest.skip("only for local testing")

    account = get_account()
    advanced_collectible, creation_transaction = deploy_and_create()
    requestId = creation_transaction.events["requestedCollectible"]["requestId"]
    random_number = 777
    get_contract("vrf_coordinator").callBackWithRandomness(
        requestId, random_number, advanced_collectible.address, {"from": account}
    )

    assert advanced_collectible.tokenCounter() == 1
    assert advanced_collectible.tokenIdToBreed(0) == random_number % 3
