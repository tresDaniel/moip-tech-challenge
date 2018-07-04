from unittest import TestCase
from src.common.card_validators import CardValidators


class TestCardValidators(TestCase):

    def test_validate_card(self):
        self.assertEqual(CardValidators.validate_card('4111 1111 1111 1111'), '4111111111111111')
        self.assertEqual(CardValidators.validate_card('4111111111111111'), '4111111111111111')
        self.assertEqual(CardValidators.validate_card('4111 1111 111'), False)
        self.assertEqual(CardValidators.validate_card('4111 1111 1111 1111 1'), False)
        self.assertEqual(CardValidators.validate_card('4111 1111 1111 111a'), False)

    def test_get_card_issuer(self):
        self.assertEqual(CardValidators.get_card_issuer('4111 1111 1111 1111'), 'Visa')
        self.assertEqual(CardValidators.get_card_issuer('4111111111111111'), 'Visa')
        self.assertEqual(CardValidators.get_card_issuer('5555555555554444'), 'Mastercard')
        self.assertEqual(CardValidators.get_card_issuer('30569309025904'), 'Others')
        self.assertEqual(CardValidators.validate_card('4111 1111 111'), False)
        self.assertEqual(CardValidators.validate_card('4111 1111 1111 1111 1'), False)
        self.assertEqual(CardValidators.validate_card('4111 1111 1111 111a'), False)

