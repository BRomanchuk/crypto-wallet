from web3 import Web3
from config import infura_url, currencies


class Ethereum:
    def __init__(self):
        self.web = Web3(Web3.HTTPProvider(infura_url))

    def get_balance(self, address):
        balance = self.web.eth.get_balance(address)
        return self.web.fromWei(balance, 'ether')

    def validate_address(self, address):
        address = self.web.toChecksumAddress(address)
        return address

    def transfer(self, receiver, amount):
        sender = currencies['eth']['address']
        receiver = self.validate_address(receiver)
        nonce = self.web.eth.get_transaction_count(sender)
        tx = {
            'nonce': nonce,
            'to': receiver,
            'value': self.web.toWei(amount, 'ether'),
            'gas': 21000,
            'gasPrice': self.web.toWei(40, 'gwei')
        }
        signed_tx = self.web.eth.account.signTransaction(tx, currencies['eth']['private'])
        tx_hash = self.web.eth.sendRawTransaction(signed_tx.rawTransaction)
        tx_dict = dict(self.web.eth.get_transaction(tx_hash))
        return bytes.hex(tx_dict['hash'])