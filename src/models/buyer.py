import uuid
from src.common.database import Database
import src.common.errors as Errors


class Buyer(object):
    def __init__(self, name, email, cpf, _id=None):
        self.name = name,
        self.email = email,
        self.cpf = cpf,
        self._id = uuid.uuid4().hex if _id is None else _id

    def save(self):
        Database.insert(collection='buyers', 
                        data=self.json())

    def json(self):
        return {
            'name': self.name,
            'email': self.email,
            'cpf': self.cpf,
            '_id': self._id
        }

    @classmethod
    def check_buyers(cls, name, email, cpf):
        if cpf is False:
            raise Errors.InvalidCpfError("The informed CPF is not valid.")
        elif email is False:
            raise Errors.InvalidEmailError("The informed email is not valid.")

        if Buyer.find_by_cpf(cpf):
            buyer = Buyer.find_by_cpf(cpf)
            return buyer
        else:
            buyer = Buyer(name, email, cpf)
            buyer.save()
            return buyer

    @classmethod
    def find_by_cpf(cls, cpf):
        buyer_data = Database.find_one(collection='buyers', query={'cpf': cpf})
        if buyer_data:
            return cls(**buyer_data)
        else:
            return None

    @staticmethod
    def list_all(id):
        return [buyer for buyer in Database.find(collection='buyers', query={'buyer_id': id})]