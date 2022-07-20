m = input("Ingrese término deseado: ")

try:
    m = round(float(m))
except:
    print("No ha ingresado un número válido")
    quit()

def fibo(n):
    t0 = 0
    t1 = 1
    for i in range(n):
        c = t0 + t1
        t0 = t1
        t1 = c
    return t1

if m == 0:
    print("0")
else:
    print(fibo(m-1))
