import uuid
from src.common.database import Database


class Client(object):
    def __init__(self, _id=None):
        self._id = uuid.uuid4().hex if _id is None else _id

    def __save(self):
        Database.insert(collection='clients', 
                        data=self.__json())

    def __json(self):
        return {
            '_id': self._id
        }

    def register(self):
        client = Client(self._id)
        client.__save()
        return client
