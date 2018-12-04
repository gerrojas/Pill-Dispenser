<<<<<<< HEAD
#Horario de funcionamiento
import schedule
#El reloj me registra la hora actual
import time
localtime = time.asctime (time.localtime(time.time()))
print ("Fecha y hora actual:")
print (localtime)

#El reloj me registra la hora actual
import time
localtime = time.asctime (time.localtime(time.time()))
print ("WELCOME TO THE PILL DISPENSER :")
print ("PROYECTO FINAL MICROS")
print (localtime)
#Caledario del Mes actual
import calendar
cal= calendar.month (2018,12)
print (cal)
print("Iniciando Pill Dispenser")
#Proceso de la Interfaz
time.sleep(1)
nombre = input ("Ingrese su nombre")
print ("Bienvenido")
print (nombre)
print ()
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

#Funcionamiento LED


#Código basico servos
