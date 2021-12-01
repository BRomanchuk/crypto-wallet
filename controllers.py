from flask import render_template, url_for, request, redirect
from config import currencies
from crypto import get_balance, validate_address


def start_page():
    return render_template('index.html')


def render_currency(currency):
    address = validate_address(currency, currencies[currency]['address'])
    amount = float(get_balance(currency, address))
    data = {
        'currency': currency.upper(),
        'address': address,
        'amount': amount
    }
    return render_template('currency.html', data=data)


def render_success(tx_hash):
    data = str(tx_hash)
    return render_template('transaction.html', data=data)
