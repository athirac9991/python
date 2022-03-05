lista=[11,22,33,44,55]
print("original list:")
print(lista)

for i in lista:
    if(i%2==0):
        lista.remove(i)
        print("list after removing EVEN numbers:")
        print(lista)
