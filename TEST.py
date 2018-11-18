
#Horario de funcionamiento
import schedule
#El reloj me registra la hora actual
import time
localtime = time.asctime (time.localtime(time.time()))
print ("WELCOME TO THE PILL DISPENSER :")
print ("PROYECTO FINAL MICROS")
print (localtime)
#Caledario del Mes actual
import calendar
cal= calendar.month (2018,11)
print (cal)
#Proceso inicia
def mensaje ():
    print ("Pill Dispenser")
def job ():
   print ("Trabajando...")
def saludo ():
   print ("Iniciando...")

schedule.every
schedule.every(1).hour.do(job)
schedule.every(1).day.at("20:55").do(job)
schedule.every(5).to(10).days.do(job)
schedule.every(1).monday.do(job)
schedule.every(1).wednesday.at("19:08").do(job)
time.sleep(1)

print("Iniciando Pill Dispenser")

#Proceso de la Interfaz
time.sleep(1)
nombre = input ("Ingrese su nombre")
print ("Bienvenido")
print (nombre)
pregunta = input ("Desea algún medicamento")
pregunta = int(input("1 : pastilla1  2 : pastilla2"))
if pregunta < 2 :
    print ("Pastilla1")
elif pregunta > 1 :
    print ("Pastilla2")
Pastilla1 = int (input("Elija la cantidad "))
if Pastilla1 > 15 :
   print ("Medicamentos insuficientes")
elif Pastilla1 < 15 :
   print ("Entregando medicamento")
#hace falta pedir una entrada de tiempo de entrega para entregar por medio de un schedule!

pregunta = input ("Desea algún medicamento")
pregunta = int(input("1 : pastilla1  2 : pastilla2"))
if pregunta < 2 :
    print ("Pastilla1")
elif pregunta > 1 :
    print ("Pastilla2")

Pastilla2 = int (input("Elija la cantidad "))
if Pastilla2 > 20 :
    print ("Medicamentos insuficientes")
elif Pastilla2 < 20 :
#hace falta pedir una entrada de tiempo de entrega para entregar por medio de un schedule!
#trabajar en pantalla de confirmacion antes de entregar.
    print ("Entregando medicamento")

#Funcionamiento LED


#Código basico servos
