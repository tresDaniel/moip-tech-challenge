from unittest import TestCase
from src.common.utils import Utils


class TestUtils(TestCase):
    def test_validate_cpf(self):
        self.assertEqual(Utils.validate_cpf('760.531.464-71'), '760.531.464-71')
        self.assertEqual(Utils.validate_cpf('760.531.464-71x'), '760.531.464-71')
        self.assertEqual(Utils.validate_cpf('760.531.464--71'), '760.531.464-71')
        self.assertEqual(Utils.validate_cpf('1760.531.464-71'), False)
        self.assertEqual(Utils.validate_cpf('000.000.000-00'), False)

    def test_validate_email(self):
        self.fail()

    def test_validate_card(self):
        self.fail()

    def test_get_card_issuer(self):
        self.fail()
