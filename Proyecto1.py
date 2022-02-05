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
        print("Haz escogido facil, tienes que adivinar un numero del 1 al 50, tendras 5 vidas.")
        random1 = random.randint(1, 50)
        eleccion1 = int(input("Escoge el numero"))
        vidas1 = 5
        vidas1 -= 1
        while eleccion1 != random1:
            if eleccion1 < random1:
                vidas1 = str(vidas1)
                print("Este no era el numero correcto, el numero que buscas es MENOR, te quedan " + vidas1 + " vidas ")
                vidas1 = int(vidas1)
            if eleccion1 > random1:
                vidas1 = str(vidas1)
                print("Este no era el numero correcto, el numero que buscas es MENOR, te quedan " + vidas1 + " vidas ")
                vidas1 = int(vidas1)
            vidas1 -= 1
            eleccion1 = int(input("Intenta con otro numero"))
            if eleccion1 == random1:
                print("FELICIDADES, HAZ GANADO")
            if eleccion1 > 50:
                print("La dificultad elegida no acepta numeros arriba de 50.")
            if vidas1 == 0:
                random1 = str(random1)
                print("Has perdido, el numero correcto era " + random1)
                break
        
    if menu == 2:
        print("Haz escogido medio, tienes que adivinar un numero del 1 al 100, tendras 5 intentos. ")
        random2 = random.randint(1, 100)
        eleccion2 = int(input("Escoge el numero "))
        vidas2 = 5
        vidas2 -= 1
        while eleccion2 != random2:
            if eleccion2 < random2:
                vidas2 = str(vidas2)
                print("Este no era el numero correcto, el numero que buscas es MENOR, te quedan " + vidas2 + " vidas ")
                vidas2 = int(vidas2)
            if eleccion2 > random2:
                vidas2 = str(vidas2)
                print("Este no era el numero correcto, el numero que buscas es MENOR, te quedan " + vidas2 + " vidas ")
                vidas2 = int(vidas2)
            vidas2 -= 1
            eleccion2 = int(input("Intenta con otro numero"))
            if eleccion2 == random2:
                print("FELICIDADES, HAZ GANADO")
                break
            if eleccion2 > 100:
                print("La dificultad elegida no acepta numeros arriba de 100.")
            if vidas2 == 0:
                random2 = str(random2)
                print("Has perdido, el numero correcto era " + random2)
                break
        
    if menu == 3:
        print("Haz escogido medio, tienes que adivinar un numero del 1 al 1000, tendras 5 intentos. ")
        random3 = random.randint(1, 1000)
        eleccion3 = int(input("Escoge el numero "))
        vidas3 = 5
        vidas3 -= 1
        while eleccion3 != random3:
            if eleccion3 < random3:
                vidas3 = str(vidas3)
                print("Este no era el numero correcto, el numero que buscas es MAYOR, te quedan " + vidas3 + "vidas ")
                vidas3 = int(vidas3)
            if eleccion3 > random3:
                vidas3 = str(vidas3)
                print("Este no era el numero correcto, el numero que buscas es MENOR, te quedan " + vidas3 + "vidas ")
                vidas3 = int(vidas3)
            vidas3 -= 1
            eleccion3 = int(input("Intenta con otro numero "))
            if eleccion3 == random3:
                print("FELICIDADES, HAZ GANADO")
                break
            if eleccion3 > 1000:
                print("La dificultad elegida no acepta numeros arriba de 1000.")
            if vidas3 == 0:
                random3 = str(random3)
                print("Has perdido, el numero correcto era " + random3)
                break
        

    if menu == 4:
            print("Haz escogido medio, tienes que adivinar un numero del 1 al 1000000, tendras 5 intentos. ")
            random4 = random.randint(1, 1000000)
            eleccion4 = int(input("Escoge el numero "))
            vidas4 = 5
            vidas4 -= 1
            while eleccion4 != random4:
                if eleccion4 < random4:
                    vidas4 = str(vidas4)
                    print("Este no era el numero correcto, el numero que buscas es MAYOR, te quedan " + vidas4 + " vidas ")
                    vidas4 = int(vidas4)
                if eleccion4 > random4:
                    vidas4 = str(vidas4)
                    print("Este no era el numero correcto, el numero que buscas es MENOR, te quedan " + vidas4 + " vidas ")
                    vidas4 = int(vidas4)
                vidas4 -= 1
                eleccion4 = int(input("Intenta con otro numero "))
                if eleccion4 == random4:
                    print("FELICIDADES, HAZ GANADO")
                    break
                if eleccion4 > 1000000:
                    print("La dificultad elegida no acepta numeros arriba de 1000000.")
                if vidas4 == 0:
                    random4 = str(random4)
                    print("Has perdido, el numero correcto era " + random4)
                    break
            



if __name__ == "__main__":
    run()
