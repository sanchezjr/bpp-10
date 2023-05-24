class ValorMinimo(Exception):
    
    def __init__(self,mensaje):
        self.mensaje=mensaje
    
    
    def __str__(self):
        return "Error de valor minimo: {} {}".format(self.mensaje, self.mensaje)



minimo = 20

try:
    numero = int(input("Introduce un número"))
    if numero < minimo:
        raise ValorMinimo("Se ha introducido un valor menor a {}".format(minimo)) 

except ValueError:
    print("Introduce un valor numérico")
except ValorMinimo as e:
    print("Error: ",e)

