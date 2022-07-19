print("GENERADOR DE LISTAS")
n_list=int(input("¿Cuantas listas quiere escribir? ", ))

for i in range(n_list):
    i=i+1
    n_pala=int(input("Digite el número de palabras que posee la lista "+format(i)+": ", ))
    palabras=[]
    
    for j in range(n_pala):
        
        palabras[j]=str(input())

print(palabras)