from flask import current_app as app
from controllers import start_page, render_currency


@app.route("/", methods=['GET'])
def index():
    return start_page(), 200


@app.route("/eth", methods=['GET'])
def eth():
    return render_currency('ETH'), 200


@app.route("/<string:currency>/send", methods=['GET'])
def send_currency(currency):
    return "render_send_currency(currency)", 200