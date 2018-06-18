from flask import Blueprint, request, url_for, session
from werkzeug.utils import redirect

from common.utils import Utils
from models.buyer import Buyer, Errors
from models.card import Card
from models.payment import Payment

payment_blueprint = Blueprint('payments', __name__)


@payment_blueprint.route('/payment', methods=['POST'])
def payment():
    if request.method == 'POST':

        client_id = session['client_id']

        buyer_name = request.form['buyer_name']
        buyer_email = Utils.validate_email(request.form['buyer_email'])
        buyer_cpf = Utils.validate_cpf(request.form['buyer_cpf'])

        try:
            temp_buyer = Buyer(buyer_name, buyer_email, buyer_cpf)
            buyer = Buyer.check_buyers(temp_buyer)
        except Errors.Error as e:
            return e.message

        payment_amount = request.form['payment_amount']
        payment_type = request.form['payment_type']

        if payment_type == 'Boleto':
            return redirect(url_for(".boleto_payment"))
        elif payment_type == 'Card':
            card_holder_name = request.form['card_holder_name']
            card_number = Utils.validate_card(request.form['card_number'])
            card_expiration_date = request.form['card_expiration_date']
            card_cvv = request.form['card_cvv']

            try:
                temp_card = Card(card_holder_name, card_number, card_expiration_date, card_cvv)
                card = Card.check_cards(temp_card)
            except Errors.Error as e:
                return e.message

            payment = Payment(client_id, payment_type, payment_amount, buyer, card)
            payment_status = Payment.register(payment)

            return redirect(url_for(".card_payment", status=payment_status))


@payment_blueprint.route('/boleto')
def boleto_payment():
    boleto_number = Payment.boleto_payment()

    return boleto_number


@payment_blueprint.route('/card/<status>')
def card_payment(status):
    if status == 'success':
        return "Your payment was successful."
    elif status == 'fail':
        return "Your payment has failed."



