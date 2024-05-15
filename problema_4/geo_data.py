import abc

class IntGeoData(abc.ABC):
    @abc.abstractmethod
    def load_data(self,data):
        raise NotImplementedError
    
    
    @abc.abstractmethod
    def display_map(self):
        raise NotImplementedError