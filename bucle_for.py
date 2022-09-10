numeros=0
for numeros in range(0,151):
    print(numeros)


multiplos=5
for multiplos in range(5,1001,5):
    print(multiplos)



def operaciones_numericas():
    for enteros in range(1,101):
        print(enteros)
        if  enteros%5==0:
            x="Coding"
            print(x)
        if  enteros%10==0:
            x="Coding Dojo"
            print(x)
        else:
            pass
operaciones_numericas()


def  enteros_impares (lista):
    suma=0
    impares=0
    for x in lista:
        if lista[x]%2==1:
            impares=lista[x]
            print(impares)
            suma=suma+x
            print(suma)
lista=list(range(1,500001))            
enteros_impares(lista)

for num_positivo in range(2018,0,4):
    print("num_positivo")


lownum=20
highnum=24
mult=4
x=lownum
y=highnum
z=mult
while x<=y:
    if x%z==0:
        print(x)
    x=x+1

                
