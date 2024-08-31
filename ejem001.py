#detecccion de paindromoss

cadena = input("Introduce una cadena: ")

cadena =cadena.lower()

l_cadena = list(cadena)


l_cadena_alrevez = list(cadena)
l_cadena_alrevez.reverse()

while "" in l_cadena:
    l_cadena.remove(" ")
while "" in l_cadena_alrevez:
    l_cadena_alrevez.remove(" ")

if l_cadena == l_cadena_alrevez:
    print("La palabra "+ cadena+ " es unpalindromo")
else:
    print("la palabra "+cadena+ " NO es un palindromo")
    