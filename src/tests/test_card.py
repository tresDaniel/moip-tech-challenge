from unittest import TestCase
from src.models.card import Card


class TestCard(TestCase):
    def test_check_cards(self):
        card = Card('DANIEL S OLIVEIRA', '4111 1111 1111 1111', '11/23', '777')
        self.assertEqual(Card.check_cards(card), card)
