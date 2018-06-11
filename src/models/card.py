import uuid
from src.common.database import Database


class Card(object):
    def __init__(self, card_holder_name, card_number, card_expiration_date, card_cvv, _id=None):
        self.card_holder_name = card_holder_name
        self.card_number = card_number
        self.card_expiration_date = card_expiration_date
        self.card_cvv = card_cvv
        self._id = uuid.uuid4().hex if _id is None else _id

    def save(self):
        Database.insert(collection='cards',
                        data=self.json())

    def json(self):
        return {
            'card_holder_name': self.card_holder_name,
            'card_number': self.card_number,
            'card_expiration_date': self.card_expiration_date,
            'card_cvv': self.card_cvv,
            '_id': self._id
        }

    @classmethod
    def check_card(cls, card_holder_name, card_number, card_expiration_date, card_cvv):
        if not Card.find_by_card_number(card_number):
            card = Card.find_by_card_number(card_number)
            return card
        else:
            card = Card(card_holder_name, card_number, card_expiration_date, card_cvv)
            return card

    @classmethod
    def find_by_card_number(cls, card_number):
        card_number = Database.find_one(collection='cards', query={'card_number': card_number})
        return cls(**card_number)
