import itertools
n = (eval(input("Digite o número de elementos do conjunto: ")))
lista_conjunto = []
lista_final = [0]


while n > 0:
  elemento = (eval(input("Digite o elemento: ")))
  if elemento in lista_conjunto:
    print("Valor duplicado!")
    print("Digite outro valor!")
  else:
    lista_conjunto.append(elemento)
    n = n -1


for elemento in lista_conjunto:
    lista_final.append([elemento])
def combinacao(s,n):
    return list(itertools.combinations(s,n))
n = 2
while n < len(lista_conjunto):
    lista_final.append([combinacao(lista_conjunto,n)])
    n = n +1

lista_final.append([lista_conjunto])
print(lista_final)
