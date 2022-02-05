import random

def run():
    menu = int(input( """
    Hola, bienvenido a el juego, para empezar, escoga una dificultad:
    
    
    1) Facil
    
    
    2) Medio
    
    
    3) Dificil
    

    4) Imposible
    
    """))

    if menu == 1:
        print("Haz escogido facil, tienes que adivinar un numero del 1 al 50, tendras 5 intentos.")
        random1 = random.randint(1, 50)
        eleccion1 = int(input("Escoge el numero"))
        vidas1 = 5
        while eleccion1 != random1:
            if eleccion1 < random1:
                print("Este no era el numero correcto, el numero que buscas es MAYOR")
            if eleccion1 > random1:
                print("Este no era el numero correcto, el numero que buscas es MENOR")
            vidas1 -= 1
            eleccion1 = int(input("Intenta con otro numero"))
            if eleccion1 == random1:
                print("FELICIDADES, HAZ GANADO")
            if eleccion1 > 51:
                print("La dificultad elegida no acepta numeros arriba de 50.")
            if vidas1 == 0:
                print("Has perdido, el numero correcto era " + random1)
                break
        
    if menu == 2:
        print("Haz escogido medio, tienes que adivinar un numero del 1 al 100, tendras 5 intentos.")
        random2 = random.randint(1, 100)
        eleccion2 = int(input("Escoge el numero"))
        vidas2 = 5
        while eleccion2 != random2:
            if eleccion2 < random2:
                print("Este no era el numero correcto, el numero que buscas es MAYOR")
            if eleccion2 > random2:
                print("Este no era el numero correcto, el numero que buscas es MENOR")
            vidas2 -= 1
            eleccion2 = int(input("Intenta con otro numero"))
            if eleccion2 == random2:
                print("FELICIDADES, HAZ GANADO")
            if eleccion2 > 101:
                print("La dificultad elegida no acepta numeros arriba de 50.")
            if vidas2 == 0:
                print("Has perdido, el numero correcto era " + random2)
                break
        





if __name__ == "__main__":
    run()
