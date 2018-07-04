from flask import Blueprint, request, url_for, session
from werkzeug.utils import redirect

from common.utils import Utils
from common.utils import CardValidators
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
            buyer = Buyer.check_buyers(buyer_name, buyer_email, buyer_cpf)
        except Errors.Error as e:
            return e.message

        payment_amount = request.form['payment_amount']
        payment_type = request.form['payment_type']

        if payment_type == 'Boleto':
            return redirect(url_for(".boleto_payment"))
        elif payment_type == 'Card':
            card_holder_name = request.form['card_holder_name']
            card_number = CardValidators.validate_card(request.form['card_number'])
            card_expiration_date = request.form['card_expiration_date']
            card_cvv = request.form['card_cvv']

            try:
                card = Card.check_cards(card_holder_name, card_number, card_expiration_date, card_cvv)
            except Errors.Error as e:
                return e.message

            payment = Payment(client_id, payment_type, payment_amount, buyer, card)
            payment_status = Payment.register(payment)

            card_issuer = CardValidators.get_card_issuer(card_number)

            return redirect(url_for(".card_payment", status=payment_status, issuer=card_issuer))


@payment_blueprint.route('/boleto')
def boleto_payment():
    boleto_number = Payment.boleto_payment()

    return boleto_number


@payment_blueprint.route('/card/<status>/<issuer>')
def card_payment(status, issuer):
    if status == 'success':
        return "Your payment was successful using a {} card".format(issuer)
    elif status == 'fail':
        return "Your payment has failed."



