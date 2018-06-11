from flask import Blueprint, request, url_for
from werkzeug.utils import redirect

from src.models.buyer import Buyer
from src.models.card import Card
from src.models.payments.payment import Payment

payment_blueprint = Blueprint('payments', __name__)


@payment_blueprint.route('/payment', methods=['POST'])
def payment():
    if request.method == 'POST':

        # client_id = session['client_id']

        buyer_name = request.form['name']
        buyer_email = request.form['email']
        buyer_cpf = request.form['cpf']

        buyer = Buyer.check_buyers(buyer_name, buyer_email, buyer_cpf)

        payment_amount = request.form['amount']
        payment_type = request.form['type']

        if payment_type == 'Boleto':
            return redirect(url_for(".boleto_payment"))
        elif payment_type == 'Card':
            card_holder_name = request.form['holder_name']
            card_number = request.form['number']
            card_expiration_date = request.form['expiration_date']
            card_cvv = request.form['card_cvv']

            card = Card.check_cards(card_holder_name, card_number, card_expiration_date, card_cvv)

            payment_status = Payment.register_payment(buyer, payment_type, payment_amount, card)

            return redirect(url_for(".card_payment", status=payment_status))


@payment_blueprint.route('/boleto')
def boleto_payment():
    boleto_number = Payment.boleto_payment()

    return boleto_number


@payment_blueprint.route('/card/<status>')
def card_payment(status):
    return status;


