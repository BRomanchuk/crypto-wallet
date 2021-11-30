from flask import render_template, url_for, request, redirect


def start_page():
    return render_template('index.html')


def render_currency(currency):
    address = 'address'
    amount = 0
    data = {
        'currency': currency,
        'address': address,
        'amount': amount
    }
    return render_template('currency.html', data=data)




