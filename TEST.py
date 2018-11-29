
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

#Funcionamiento LED Accionarlo con los sensores infrarrojo 

import Rpi.GPIO as GPIO 
GPIO.setmode(GPIO.BOARD)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)
GPIO.ouput(11,True)
time.sleep(1)
GPIO.output(11,False)
time.sleep(1) 


#Código basico servos servo 2 helices
import Rpi.GPIO as GPIO 
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)
pwm=GPIO.PWM(11,50)
pwm.start(7) #posion inicial
pwm.ChangeDutyCycle(3) #0 grados totalmente derecho
pwm.ChangeDutyCycle(12) #180 grados totalmente izquierdo
pwm.stop()
GPIO.cleanup()


#Código basico servos servo 4 helices
import Rpi.GPIO as GPIO 
GPIO.setmode(GPIO.BOARD)
GPIO.setup(13,GPIO.OUT)
pwm=GPIO.PWM(13,50)
pwm.start(6) #posion inicial
pwm.ChangeDutyCycle(2.5) #0 grados totalmente derecho
pwm.ChangeDutyCycle(10.5 #180 grados totalmente izquierdo
pwm.stop()
GPIO.cleanup()



