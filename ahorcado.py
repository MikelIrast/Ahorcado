import random

alfabeto = "a b c d e f g h i j k l m n ñ o p q r s t u v w x y z"

def seleccionar_palabra():
    with open("frutas_verduras.txt") as archivo:
        lineas = archivo.readlines()
    palabra = random.choice(lineas).strip()  # .strip() para eliminar saltos de línea y espacios
    return palabra

palabra = seleccionar_palabra()
print(palabra)

def entrada_usuario():
    letra = input("Introduzca una letra: ")
    return letra.lower()

def actualizar_jugada(palabra, letra, jugada):
    for i in range(len(palabra)):
        if palabra[i] == letra:
            jugada[i] = letra
    return jugada

jugada = ["_"] * len(palabra)

def actualizar_alfabeto(letra, alfabeto):
    alfabeto = alfabeto.replace(letra, " ")
    return alfabeto

def imprimir_actualizaciones(alfabeto, jugada):
    print(f"Jugada: {' '.join(jugada)}")
    print(f"Letras disponibles: {alfabeto}")

def verificar_jugada(suposicion, palabra):
    return suposicion == palabra

success = False  # Inicializar success antes del bucle

for turno in range(5):
    print(f"\nTurno: {turno + 1}")
    print("-" * 20)

    imprimir_actualizaciones(alfabeto, jugada)

    letra = entrada_usuario()

    jugada = actualizar_jugada(palabra, letra, jugada)
    alfabeto = actualizar_alfabeto(letra, alfabeto)

    imprimir_actualizaciones(alfabeto, jugada)

    check = input("Te la juegas a adivinar (s/n)? ")
    if check.lower() == "s":
        suposicion = input("Introduzca la respuesta: ").lower()
        success = verificar_jugada(suposicion, palabra)

        if success:
            print("+" * 20)
            print("¡GANASTE!")
            print("+" * 20)
            break  # Sale del bucle si el jugador gana
        else:
            print("+" * 20)
            print("Es incorrecto...")
            print("+" * 20)

if not success:  # Solo mostrar el mensaje de pérdida si no se ha ganado
    print("+" * 20)
    print(":() Ahorcado")
    print("+" * 20)