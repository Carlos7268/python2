x = input("Digite um numero: ")
y = input("digite mais 1 valor: ")
z = input("digite um ultimo valor: ")
x = int(x)
y = int(y)
z = int(z)
if(x>y):
    if(x>z):
        print(x + "é o maior")
    else:
        print(z + "é o maior")
else:
    if(y>z):
        print(y + "é o maior")
    else:
        print(z + "é o maior")
                        