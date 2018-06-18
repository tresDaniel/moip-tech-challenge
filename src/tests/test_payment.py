from unittest import TestCase
from src.models.payment import Payment
from src.models.buyer import Buyer
from src.models.card import Card


class TestPayment(TestCase):
    def test_register(self):
        buyer = Buyer('Daniel Silva', 'daniel@test.com', '760.531.464-71')
        card_1 = Card('DANIEL S OLIVEIRA', '4111 1111 1111 1111', '11/23', '777')
        card_2 = Card('DANIEL S OLIVEIRA', '5555 5555 5555 4444', '11/23', '777')
        payment_1 = Payment('0x4D3EfAb6C', 'Card', '75.00', buyer, card_1)
        payment_2 = Payment('0x4D3EfAb6C', 'Card', '75.00', buyer, card_2)

        self.assertEqual(Payment.register(payment_1), 'fail')
        self.assertEqual(Payment.register(payment_2), 'success')

    def test_boleto_payment(self):
        pass
