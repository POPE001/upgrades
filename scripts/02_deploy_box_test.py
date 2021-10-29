from brownie import BoxV2, network
from scripts.helpful_scripts import get_account


def main():
    account = get_account()
    print(f"Deploying to {network.show_active()}")
    boxTest = BoxV2.deploy({"from": account})
    print(boxTest.retrieve())
