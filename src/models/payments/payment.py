import uuid
from src.common.database import Database
from src.common.utils import Utils


class Payment(object):
    def __init__(self, client_id, buyer, amount, payment_type, card, _id=None):
        self.client_id = client_id
        self.buyer = buyer
        self.amount = amount
        self.payment_type = payment_type
        self.card = card
        self._id = uuid.uuid4().hex if _id is None else _id

    def save(self):
        Database.insert(collection='payments', 
                        data=self.json())

    def json(self):
        return {
            'client_id': self.client_id,
            'amount': self.amount,
            'payment_type': self.payment_type,
            '_id': self._id
        }

    def is_payment_valid(self):
        pass

    @staticmethod
    def process_payment(payment_type):
        if(payment_type == ''):
            pass

    @staticmethod
    def boleto_payment():
        boleto_code = Utils.generate_boleto()
        return boleto_code

    def register_payment(self):
        pass

    @classmethod
    def get_by_id(cls, id):
        payment_data = Database.find_one(collection='payments', query={'_id': id})
        return cls(**payment_data)

    @classmethod
    def find_by_client_id(cls, client_id):
        payments = Database.find(collection='payments', query={'client_id' : client_id})
        return [cls(**payment) for payment in payments]