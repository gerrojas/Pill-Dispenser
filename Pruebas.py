import time
print("Conteste S (sí) o N (no) a las preguntas")
#Try sirve para detectar errores dependiendo de la condicion que tenga el codigo
while True:
    question = input ("Desea algun medicamento?")
    if question == "S" :
        pregunta = int(input("1: Pastilla1  2: Pastilla2"))
        if pregunta==1:
            print ("Pastilla1")
            Pastilla1 = int (input("Elija la cantidad "))
            if Pastilla1 > 15:
                print ("Medicamentos insuficientes")
            elif Pastilla1 < 15:
                print ("Entregando medicamento")
        elif pregunta==2:
            print ("Pastilla2")
            Pastilla2 = int (input("Elija la cantidad "))
            if Pastilla2 >15:
                print ("Medicamentos insuficientes")
            elif Pastilla2<15:
                print ("Entregando medicamento")

    elif question == "N" :
        print ("Buen dia!")
        time.sleep(5)
    print ()
