lista = []

while true:
    numero = int(input("digite um número (0 para parar): "))
    if numero == 0:
     break
    lista.append(numero)
x = 0
y = 0
for z in lista:
   if z > 5:
      x = x + 1
      if z % 2 == 0:
         y = y + 1
print("--- Resultado ---")
print("Lista:", lista)
print("Maiores que 5:", x)
print("Pares", y)