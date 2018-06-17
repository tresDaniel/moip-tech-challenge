import uuid, re
from src.common.database import Database
from src.common.utils import Utils


class Payment(object):
    def __init__(self, client_id, payment_type, payment_amount, buyer, card, _id=None):
        self.client_id = client_id
        self.payment_type = payment_type
        self.payment_amount = payment_amount
        self.buyer = buyer
        self.card = card
        self._id = uuid.uuid4().hex if _id is None else _id

    def __save(self):
        Database.insert(collection='payments', 
                        data=self.json())

    def json(self):
        return {
            'client_id': self.client_id,
            'payment_type': self.payment_type,
            'payment_amount': self.payment_amount,
            'buyer': self.buyer,
            'card': self.card,
            '_id': self._id
        }

    def register(self):
        if Payment.__is_payment_valid(self.card.card_number):
            payment = Payment(self.client_id, self.payment_type, self.payment_amount, self.buyer.json(), self.card.json())
            payment.__save()
            return "success"
        else:
            return "fail"

    @staticmethod
    def __is_payment_valid(card_number):
        card_number = ''.join(re.findall(r'\d', str(card_number)))
        if int(card_number) % 2 == 0:
            return True
        else:
            return False

    @staticmethod
    def boleto_payment():
        boleto_code = Utils.__generate_boleto()
        return boleto_code

    @classmethod
    def get_by_id(cls, id):
        payment_data = Database.find_one(collection='payments', query={'_id': id})
        return cls(**payment_data)

    @classmethod
    def find_by_client_id(cls, client_id):
        payments = Database.find(collection='payments', query={'client_id': client_id})
        return [cls(**payment) for payment in payments]