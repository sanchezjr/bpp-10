# a=5
# b=1
# try:
#     a/b
#     d = 2 + "Hola"
# except ZeroDivisionError as e:
#     print("División entre 0")
# except TypeError:
#     print("Error en el tipo de dato")
# except (ZeroDivisionError,TypeError):
#     print ("Error ")
# except Exception as e:
#     print ("Error ",e)
# else:
#     print("Entra en este bloque si no ha ocurrido ninguna excepción")
# finally:
#     print("Este bloque se ejecuta siempre")

#raise
# edad=17
# a=1
# b=0
# try:
#     if type(b) != int:
#         raise Exception
#     else:
#         a/b
# except Exception:
#     print("No es mayor de edad")

#assert

#assert 1==2, "Información del assert" 

def calcular_media(lista):
    return sum(lista)/len(lista)

assert(calcular_media([5,5,5]) == 5)
assert(calcular_media([5]) == 5)


def suma(a,b): 
    assert(type(a) == int)
    assert(type(b) == int)
    return a+b

suma(2,3)

class Mi_1:
    pass
class Mi_2:
    pass

m1 = Mi_1()
m2 = Mi_2()

assert(isinstance(m1,Mi_1))

# utilizando -O ( o mayuscula) se deshabilitan los assert

class miExcepcion(Exception):
    def __init__(self,param1,param2):
        self.mensaje=param1
        self.informacion=param2
        
        
try:         
    raise miExcepcion("Este es mi mensaje ","y aquí la info")
except miExcepcion as ex:
    p1,p2 = ex.args
    print(p1,p2)




print("Fin")