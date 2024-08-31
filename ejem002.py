#Frecuenecia de aparicion
cadena = input("Introduce una palabra: ")

caracteres = {}

for caracter in cadena:
    if caracter in caracteres.keys():
        caracteres[caracter] += 1
    else:
        caracteres[caracter] =1
        
    print(caracteres)