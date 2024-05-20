import random

def main():
    proyecto()
    

def proyecto():
    print("¡Bienvenido al juego!¿Será capáz de adivinar el número misterioso por un premio secreto? Eso lo veremos, primero ingrese el rango númerico al que te vas a enfrentar.")
    generar_numero_random_y_comparar()



def generar_numero_random_y_comparar():

    n1=int(input("Ingrese el primer numero: "))
    n2=int(input("Ingrese el segundo numero: "))
    numero_random = random.randint(n1,n2) 
    print("Muy bien pequeño, ¿esta preparado para adivinar el numero misterioso?")
    es_mismo_numero(numero_random)


def es_mismo_numero(numero_random):
    numero_propio=0
    while numero_random!=numero_propio:
        numero_propio=int(input("Ingrese el supuesto número misterioso: "))
        if numero_random!=numero_propio: print("Incorrecto, vuelva a intentar.")
    print(f"Felicidades!{numero_propio} era el numero correcto")

    
