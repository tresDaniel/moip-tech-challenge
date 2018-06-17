import uuid
from src.common.database import Database
import src.common.errors as Errors


class Buyer(object):
    def __init__(self, name, email, cpf, _id=None):
        self.name = name,
        self.email = email,
        self.cpf = cpf,
        self._id = uuid.uuid4().hex if _id is None else _id

    def __save(self):
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
    def check_buyers(cls, temp_buyer):
        if temp_buyer.cpf is False:
            raise Errors.InvalidCpfError("The informed CPF is not valid.")
        elif temp_buyer.email is False:
            raise Errors.InvalidEmailError("The informed email is not valid.")

        if Buyer.__find_by_cpf(temp_buyer.cpf):
            buyer = Buyer.__find_by_cpf(temp_buyer.cpf)
            return buyer
        else:
            buyer = Buyer.__register(temp_buyer)
            return buyer

    def __register(self):
        buyer = Buyer(self.name, self.email, self.cpf)
        buyer.__save()
        return buyer

    @classmethod
    def __find_by_cpf(cls, cpf):
        buyer_data = Database.find_one(collection='buyers', query={'cpf': cpf})
        if buyer_data:
            return cls(**buyer_data)
        else:
            return None
