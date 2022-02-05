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





if __name__ == "__main__":
    run()
