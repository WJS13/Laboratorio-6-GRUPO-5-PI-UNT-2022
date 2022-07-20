print("BASE DE DATOS SEGÚN LA EDAD")
print("---------------------------------------------")

n=int(input("Ingrese el número de personas a registrar: "))
datos=["Nombre","DNI","Edad"]
obt_datos = []
print("")
for i in range (n):
    nombre=str(input("Ingrese su nombre: "))
    dni=str(input("Ingrese su número de dni: "))
    edad=int(input("Ingrese su edad: "))
    print('************')
    obt_datos.append([nombre,dni,edad])

print ("DATOS ORDENADOS SEGÚN EDAD")
print("")


edades=[]

for i in range(n):
    edades.append(obt_datos[i][2])

edades.sort()

for i in range(n):
    for j in range(n):
        if obt_datos[j][2]==edades[i]:
            obt_datos.append(obt_datos[j])

for i in range(n):
   del obt_datos[0]

for i in range(n):
    diccionario=dict(zip(datos,obt_datos[i]))
    print(diccionario)