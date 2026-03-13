x = input("escreva seu nome: ")
y = 0
z = 0
for char in x:
    y += 1
    if char == 'a' or char == "A":
        z += 1
print("Letras:",y)
print("Letras a:",z)     