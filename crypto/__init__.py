from web3 import Web3
from config import infura_url, currencies


def get_balance(address):
    web = Web3(Web3.HTTPProvider(infura_url))
    balance = web.eth.get_balance(address)
    return web.fromWei(balance, 'ether')


def validate_address(address):
    web = Web3(Web3.HTTPProvider(infura_url))
    address = web.toChecksumAddress(address)
    return address


def transfer(receiver, amount):
    web = Web3(Web3.HTTPProvider(infura_url))
    sender = currencies['eth']['address']
    receiver = validate_address(receiver)
    nonce = web.eth.get_transaction_count(sender)
    tx = {
        'nonce': nonce,
        'to': receiver,
        'value': web.toWei(amount, 'ether'),
        'gas': 21000,
        'gasPrice': web.toWei(40, 'gwei')
    }
    signed_tx = web.eth.account.signTransaction(tx, currencies['eth']['private'])
    tx_hash = web.eth.sendRawTransaction(signed_tx.rawTransaction)
    return 'Success', 200