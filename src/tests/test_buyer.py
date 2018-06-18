from unittest import TestCase
from src.models.buyer import Buyer


class TestBuyer(TestCase):
    def test_check_buyers(self):
        buyer = Buyer('Daniel Silva', 'daniel@test.com', '760.531.464-71')
        self.assertEqual(Buyer.check_buyers(buyer), buyer)
