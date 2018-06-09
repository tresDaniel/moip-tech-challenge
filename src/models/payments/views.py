from flask import Blueprint, request, session, url_for
from werkzeug.utils import redirect

payment_blueprint = Blueprint('payments', __name__)

@payment_blueprint.route('/payment', methods=['POST'])
def payment():
    if request.method == 'POST':

        # buyer_name = request.form['name']
        # buyer_email = request.form['email']
        # buyer_cpf = request.form['cpf']

        payment_type = request.form['type']

        if payment_type == 'Boleto':
            return redirect(url_for(".boleto_payment"))
        elif payment_type == 'Card':
            return redirect(url_for(".card_payment"))

@payment_blueprint.route('/boleto')
def boleto_payment():
    return "12323424242342442"

@payment_blueprint.route('/card')
def card_payment():
    return "Card Payment"

