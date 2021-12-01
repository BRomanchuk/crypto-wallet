from crypto.currencies import ethereum, bitcoin


currencies = {
    'eth': ethereum.Ethereum(),
    'btc': bitcoin.Bitcoin()
}


def get_balance(curr, address):
    return currencies[curr].get_balance(address)


def validate_address(curr, address):
    return currencies[curr].validate_address(address)


def transfer(curr, receiver, amount):
    return currencies[curr].transfer(receiver, amount)
