import uuid
from src.common.database import Database


class Client(object):
    def __init__(self, _id=None):
        self._id = uuid.uuid4().hex if _id is None else _id

    def __save(self):
        Database.insert(collection='clients', 
                        data=self.json())

    def __json(self):
        return {
            '_id': self._id
        }
    
    @classmethod
    def __from_db(cls, id):
        client_data = Database.find_one(collection='clients', query={'_id': id})
        return cls(**client_data)

    @staticmethod
    def __list_all(id):
        return [client for client in Database.find(collection='clients', query={'client_id': id})]
