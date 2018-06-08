import uuid
from src.common.database import Database


class Buyer(object):
    def __init__(self, client_id, name, email, cpf, _id=None):
        self.client_id = client_id,
        self.name = name,
        self.email = email,
        self.cpf = cpf,
        self._id = uuid.uuid4().hex if _id is None else _id

    def save(self):
        Database.insert(collection='buyers', 
                        data=self.json())

    def json(self):
        return {
            'client_id': self.client_id,
            'name': self.name,
            'email': self.email,
            'cpf': self.cpf,
            '_id': self._id
        }
    
    @classmethod
    def from_db(cls, id):
        client_data = Database.find_one(collection='buyers', query={'_id': id})
        return cls(**client_data)

    @classmethod
    def from_client(cls, id):
        buyer_data = Database.find_one(collection='buyers', query={'client_id': id})
        return cls(**buyer_data)

    @staticmethod
    def list_all(id):
        return [client for client in Database.find(collection='buyers', query={'buyer_id' : id})]