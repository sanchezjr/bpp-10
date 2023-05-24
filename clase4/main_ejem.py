import pdb
pdb.set_trace()

def sumaCuadrados(n):
    sumaCuadrados = 0
    while(n):
        sumaCuadrados += 1
        n = n // 10
    return sumaCuadrados

v1 = 0
v2 = "fsss"
result = sumaCuadrados(70)
print(result)
print("Fin")