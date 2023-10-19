import random

def generar_palabra_secreta():
  return random.choice(lista_lenguajes).lower()

def mostrar_dibujo(turno):
  return print(AHORCADO[turno-1])

def mostrar_progreso(palabra, letras_adivinadas):
    progreso = ""
    for letra in palabra:
        if letra in letras_adivinadas:
            progreso += letra
        else:
            progreso += "_"
    return progreso

def jugar_ahorcado():
    palabra_secreta = generar_palabra_secreta()
    intentos_restantes = 6
    letras_adivinadas = []

    print("¡Bienvenido al Juego del Ahorcado!")
    print("Palabra secreta:", mostrar_progreso(palabra_secreta, letras_adivinadas))
    print(mostrar_dibujo(intentos_restantes))
        
    while intentos_restantes > 0:
        letra = input("Adivina una letra: ").lower()
        if len(letra) != 1 or not letra.isalpha():
            print("Ingresa una sola letra válida.")
            continue

        if letra in letras_adivinadas:
            print("Ya has adivinado esa letra antes.")
        elif letra in palabra_secreta:
            letras_adivinadas.append(letra)
            progreso_actual = mostrar_progreso(palabra_secreta, letras_adivinadas)
            print("Correcto! Palabra secreta:", progreso_actual)
            if progreso_actual == palabra_secreta:
                print("¡Has ganado! La palabra secreta era:", palabra_secreta)
                break
        else:
            intentos_restantes -= 1
            print("¡Incorrecto! Te quedan", intentos_restantes, "intentos.")

    if intentos_restantes == 0:
        print("¡Has perdido! La palabra secreta era:", palabra_secreta)


# Main

AHORCADO = ['''
      +---+
      |   |
          |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========''']

lista_lenguajes = ["Java", "Python", "C", "Go", "JavaScript", "PHP"]

jugar_ahorcado()