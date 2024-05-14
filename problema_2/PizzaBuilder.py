from Builder import Builder
from Pizza import Pizza


class PizzaBuilder(Builder):
    def __init__(self):
        self.pizza = Pizza()

    def agregarIngredientes(self, ingrediente,costo,cantidad):
        self.pizza.ingredientes.append(ingrediente)
        self.pizza.costo = self.pizza.costo + cantidad * costo
        print(f"Ingrediente agregado: {ingrediente} costo: {cantidad * costo}\n", end="")
        
    def agregarTamano(self, tamano,costo):
        self.pizza.tamano = tamano
        self.pizza.costo += costo
        print(f"Tamaño escogido: {tamano} costo: {costo}\n", end="")
        
    def agregarMasa(self, masa):
        self.pizza.masa = masa
        print(f"Masa escogida: {masa}\n", end="")
    
    def agregarBorde(self, borde,costo):
        if borde:
            self.pizza.costo += costo
            self.pizza.borde = True
        print(f"Borde de queso agregado: {borde} costo: {costo}\n", end="")

    def realizarPedido(self):
        print("Pedido realizado")

    def listarPedido(self):
        print(f"Su pizza contiene lo siguiente:\n Tamaño: {self.pizza.tamano}\n Masa: {self.pizza.masa}\n Ingredientes: {', '.join(self.pizza.ingredientes)}\n Extra Borde de queso:{self.pizza.borde}\n Costo Total: {self.pizza.costo}\n", end="")