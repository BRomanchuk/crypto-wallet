from flask import current_app as app
from flask import request
from controllers import start_page, render_currency, render_success
from crypto import transfer


@app.route("/", methods=['GET'])
def index():
    return start_page(), 200


@app.route("/<string:curr>", methods=['GET'])
def currency(curr):
    if curr.lower() not in ['btc', 'eth']:
        return 'not found', 404
    return render_currency(curr), 200


@app.route('/eth', methods=['POST'])
def my_form_post():
    receiver = request.form.get('receiver')
    amount = request.form.get('amount')
    tx_hash = transfer('eth', receiver, amount)
    return render_success(tx_hash), 200
