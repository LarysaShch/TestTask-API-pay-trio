import datetime
import json
from flask import Flask, request, render_template
import hashlib
import logging
from logging.handlers import RotatingFileHandler
import requests

from production import SHOP_ID, SHOP_SECRET_KEY

app = Flask(__name__)

def get_resource_as_string(name, charset='utf-8'):
    with app.open_resource(name) as f:
        return f.read().decode(charset)

app.jinja_env.globals['get_resource_as_string'] = get_resource_as_string

SHOP_INVOICE_ID = 0

def generate_sign(params):
    plain_text = ''
    for key in sorted(params):
        if plain_text:
            plain_text += ':'
        plain_text += str(params[key])

    return hashlib.md5(plain_text.encode('utf-8')).hexdigest()

def init_log_handler():
    # initialize the log handler
    logHandler = RotatingFileHandler('log.log', maxBytes=1000, backupCount=1)
    
    # set the log handler level
    logHandler.setLevel(logging.INFO)

    # set the app logger level
    app.logger.setLevel(logging.INFO)

    app.logger.addHandler(logHandler)

def log_transaction(currency, amount, datetime, description, SHOP_INVOICE_ID):    
    app.logger.info(
        json.dumps(str({'currency': currency, 'amount': amount, 'datetime': datetime, 
            'description': description, 'shop_invoice_id': SHOP_INVOICE_ID})))

@app.route('/')
@app.route('/index')
def index():
    init_log_handler()
    return render_template('index.html')

def make_payment_usd(amount, currency, SHOP_INVOICE_ID, description):
    # TIP
    currency_id = 840
    sign = generate_sign({'amount': amount, 'currency': currency_id, 'shop_id': SHOP_ID, \
        'shop_invoice_id': SHOP_INVOICE_ID})
    try:
        r = requests.post('https://tip.pay-trio.com/en/', data = 
            {'amount': amount, 'currency': currency_id, 'shop_id': SHOP_ID, 'sign': sign, \
            'shop_invoice_id': SHOP_INVOICE_ID, 'description': description})

        if r.status_code == requests.codes.ok:
            log_transaction(currency, amount, str(datetime.datetime.now()), description, SHOP_INVOICE_ID)
            res = 'Successful payment in USD'
        else:
            res = 'Error occurs during payment in USD'
    except Exception:
        res = 'Error occurs during payment in USD'

    return res

def make_payment_eur(amount, currency, SHOP_INVOICE_ID, description):
    # Invoice
    currency_id = 978
    payway = 'payeer_eur'

    sign = generate_sign({'amount': amount, 'currency': currency_id, 'payway': payway, 'shop_id': SHOP_ID, \
        'shop_invoice_id': SHOP_INVOICE_ID})
    try:
        r = requests.post('​https://central.pay-trio.com/invoice', data = 
            {'amount': amount, 'currency': currency_id, 'payway': payway, 'shop_id': SHOP_ID, 'sign': sign, \
            'shop_invoice_id': SHOP_INVOICE_ID, 'description': description})

        if r.status_code == requests.codes.ok:
            log_transaction(currency, amount, str(datetime.datetime.now()), description, SHOP_INVOICE_ID)
            res = 'Successful payment in EUR'
        else:
            res = 'Error occurs during payment in EUR'
    except:
        res = 'Error occurs during payment in EUR'

    return res


@app.route('/pay', methods=['GET', 'POST'])
def pay():
    if request.method == 'POST':
        amount  = float(request.form.get('amount', None))
        currency  = request.form.get('currency', None)
        description  = request.form.get('description', None)

        if not amount:
            return 'Empty payment'

        global SHOP_INVOICE_ID
        SHOP_INVOICE_ID += 1

        if currency == 'usd':
            return make_payment_usd(amount, currency, SHOP_INVOICE_ID, description)
        if currency == 'eur':
            return make_payment_eur(amount, currency, SHOP_INVOICE_ID, description)
