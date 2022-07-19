filas=int(input("ingresar el número de filas que desee ", ))

def triangulo_numeros(filas):
    for n in range(filas):

        for i in range(filas-n-1):
             print("  ",end="")

        for j in range(n+1):
            print(j+1,end="   ")

        print(" ")
        print(" ")

while filas>9:
    print("El valor ingresado se encentra fuera del intervalo de 1 a 9")
    print("Vuelva a ingresar otro valor dentro del intervalo del 1 al 9")
    filas=int(input("ingresar el número de filas que desee ", ))

triangulo_numeros(filas)