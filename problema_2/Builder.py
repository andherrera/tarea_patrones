
from abc import ABC, abstractmethod


class Builder(ABC):
    @abstractmethod
    def agregarIngredientes():
        pass  

    @abstractmethod
    def agregarTamano():
        pass

    @abstractmethod
    def agregarMasa():
        pass

    @abstractmethod
    def agregarBorde():
        pass 

    @abstractmethod
    def realizarPedido():
        pass 
