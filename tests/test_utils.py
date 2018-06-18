from unittest import TestCase
from src.common.utils import Utils


class TestUtils(TestCase):
    def test_validate_cpf(self):
        self.assertEqual(Utils.validate_cpf('760.531.464-71'), '760.531.464-71')
        self.assertEqual(Utils.validate_cpf('76053146471'), '760.531.464-71')
        self.assertEqual(Utils.validate_cpf('760.53146471'), '760.531.464-71')
        self.assertEqual(Utils.validate_cpf('760531464-71'), '760.531.464-71')
        self.assertEqual(Utils.validate_cpf('760.531.464-71x'), '760.531.464-71')
        self.assertEqual(Utils.validate_cpf('760.531.464--71'), '760.531.464-71')
        self.assertEqual(Utils.validate_cpf('1760.531.464-71'), False)
        self.assertEqual(Utils.validate_cpf('7605314647'), False)

    def test_validate_email(self):
        self.assertEqual(Utils.validate_email('daniel@test.com'), 'daniel@test.com')
        self.assertEqual(Utils.validate_email('daniel.silva@test.com'), 'daniel.silva@test.com')
        self.assertEqual(Utils.validate_email('daniel-silva@test.com'), 'daniel-silva@test.com')
        self.assertEqual(Utils.validate_email('daniel-silva.1@test.com'), 'daniel-silva.1@test.com')
        self.assertEqual(Utils.validate_email('daniel@test.com.br'), 'daniel@test.com.br')
        self.assertEqual(Utils.validate_email('daniel@test-1.com'), 'daniel@test-1.com')
        self.assertEqual(Utils.validate_email('daniel@test@com'), False)

    def test_validate_card(self):
        self.assertEqual(Utils.validate_card('4111 1111 1111 1111'), '4111111111111111')
        self.assertEqual(Utils.validate_card('4111111111111111'), '4111111111111111')
        self.assertEqual(Utils.validate_card('4111 1111 111'), False)
        self.assertEqual(Utils.validate_card('4111 1111 1111 1111 1'), False)
        self.assertEqual(Utils.validate_card('4111 1111 1111 111a'), False)

    def test_get_card_issuer(self):
        self.assertEqual(Utils.get_card_issuer('4111 1111 1111 1111'), 'Visa')
        self.assertEqual(Utils.get_card_issuer('4111111111111111'), 'Visa')
        self.assertEqual(Utils.get_card_issuer('5555555555554444'), 'Mastercard')
        self.assertEqual(Utils.get_card_issuer('30569309025904'), 'Others')
        self.assertEqual(Utils.validate_card('4111 1111 111'), False)
        self.assertEqual(Utils.validate_card('4111 1111 1111 1111 1'), False)
        self.assertEqual(Utils.validate_card('4111 1111 1111 111a'), False)

