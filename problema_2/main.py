import time
from Builder import Builder
from PizzaBuilder import PizzaBuilder

if __name__ == "__main__":
    ingredientes = {'peperoni':['Peperoni',200],'queso':['Queso',100],'pina':['Piña',300],'champinon':['Champiñones',300],'jamon':['Jamon',500],'cebolla':['Cebolla',100],'aceitunas':['Aceitunas',100],'pimientos':['Pimientos',100]}
    tamanos = {'mediana':['Mediana',1000],'pequena':['Pequeña',800],'grande':['Grande',1500]}
    masa = {'delgada':['Delgada'],'gruesa':['Gruesa'],'integral':['Integral']} 
    
    builder = PizzaBuilder()
    builder.agregarTamano(tamanos['pequena'][0],tamanos['pequena'][1])
    builder.agregarMasa(masa['delgada'][0])
    builder.agregarIngredientes(ingredientes['queso'][0],ingredientes['queso'][1],2)
    builder.agregarIngredientes(ingredientes['peperoni'][0],ingredientes['peperoni'][1],1)
    builder.agregarIngredientes(ingredientes['pina'][0],ingredientes['pina'][1],3)
    time.sleep(5)
    builder.listarPedido()
    time.sleep(5)
    builder.realizarPedido()