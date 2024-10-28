from abc import ABC, abstractmethod

class dataAccessDAO(ABC):
    
    @abstractmethod
    def create(self, entity):
        pass

    @abstractmethod
    def read(self, entity_id):
        pass

    @abstractmethod
    def read_all(self):
        pass

    @abstractmethod
    def update(self, entity):
        pass

    @abstractmethod
    def delete(self, entity_id):
        pass