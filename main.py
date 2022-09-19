print("Hola soy EL CHAVITO, ¿Puedo hacerte una pregunta?")
pregunta = str(input("Escribe tu respuesta (SI o NO): "))
if pregunta == "SI" or pregunta == "Si" or pregunta == "si":
    intento = 1
    while intento == 1:
        print("1. ¿Cual es la capital histórica del Perú")
        print("A: Lima")
        print("B: Tarapoto")
        print("C: Cusco")
        print("D: Arequipa")

        respuesta = str(input("Escribe tu respuesta: "))
        if respuesta == "C":
            intento = 0
            print("Correcto, es Cusco, gracias por jugar conmigo, adiós !")
        else:
            print("Tu respuesta es incorrecta")
            pregunta = str(input("Deseas jugar de nuevo (SI o NO): "))
            if pregunta == "SI" or pregunta == "Si" or pregunta == "si":
                intento = 1
            else:
                intento = 0
                print("Ok, muchas gracias, adiós !")
else:
    print("Ok, muchas gracias, adiós !")
