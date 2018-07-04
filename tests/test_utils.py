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


