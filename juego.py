import random
number = random.randint(10,20)
print("Hola, bienvenido, ¿quieres jugar?")
choice = input("Escribe tu respuesta:")
print(choice)
if choice == "Si":
    print("Bien!, adivina el número al azar, el rango es de 10-20")
    while True:
        answer = int(input("Escribe el número:"))
        if answer<number:
            print("Muy bajo")
        elif answer>number:
            print("Muy alto")
        elif answer == number:
            print("Felicidades! haz acertado, ganaste")
            break
else:
    print("Entendido, hasta pronto!")
    
