print("GENERADOR DE LISTAS")

n_list=int(input("¿Cuantas listas quiere escribir? ", ))

listas_palabras=[]
for i in range(n_list):
    
    n_pala=int(input("Digite el número de palabras que posee la lista "+format(i+1)+": ", ))
    palabras=[]

    for j in range(n_pala):
        palabras.append(input("Escriba la palabra "+format(j+1)+": ", ))
    
    listas_palabras.append(palabras)
    
for i in range(n_list):
    print("La lista", i+1,"es :",listas_palabras[i])