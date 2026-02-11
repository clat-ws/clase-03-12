#Clase del 11/2/2026
#1.Pedir un número al usuario
num = int(input("Ingresa un número: "))
#usar condiciones (if,elif,else) para decir si es positivo, cero o negativo
if num > 0:
    print("Tu número es positivo", num)
elif num == 0:
    print("Tu número es", num)
else:
    print("Tu número es negativo", num)