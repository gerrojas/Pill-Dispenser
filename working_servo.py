import string
import time
import RPi.GPIO as GPIO 
localtime = time.asctime (time.localtime(time.time()))


servo1= 11
servo2= 13
led1 = 12
led2 = 18
GPIO.setwarnings(False)
print()
print()
print()

print ("WELCOME TO THE PILL DISPENSER :")
print ("PROYECTO FINAL MICROS")
print ("Gerson Campos - Ignacio Morales")
print()
print (localtime)

#Caledario del Mes actual
import calendar
cal= calendar.month (2018,12)
print (cal)
print()
print("Iniciando Pill Dispenser")
time.sleep(1)
nombre = input ("Ingrese su nombre")
print ("Bienvenido")
print (nombre)
print()
time.sleep(2)

def medic1 ():
                    GPIO.setmode(GPIO.BOARD)
                    GPIO.setup(led1,GPIO.OUT)
                    GPIO.setup(servo1,GPIO.OUT)
                    GPIO.output(servo1,1)
                    pwm1=GPIO.PWM(servo1,50)
                    pwm1.start(12)
                    GPIO.output(led1, True)
                    time.sleep(0.5)
                    pwm1.ChangeDutyCycle(3)
                    time.sleep(1)
                    pwm1.ChangeDutyCycle(12)
                    time.sleep(1)
                    GPIO.output(led1, False)
                    
            
                    pwm1.stop()

   
def medic2 ():
                    GPIO.setmode(GPIO.BOARD)
                    GPIO.setup(led2,GPIO.OUT)
                    GPIO.setup(servo2,GPIO.OUT)
                    GPIO.output(servo2,1)
                    pwm2=GPIO.PWM(servo2,50)
                    pwm2.start(10.5)
                    GPIO.output(led2, True)
                    time.sleep(0.5)
                    pwm2.ChangeDutyCycle(2.5)
                    time.sleep(1)
                    pwm2.ChangeDutyCycle(10.5)
                    time.sleep(1)
                    GPIO.output(led2, False)

                    pwm2.stop() 


    
print("Responda S o N a las preguntas")

while True:
  
    question = input ("Desea algun medicamento?")
    if question == "S" :
        pregunta = int(input("1: Pastilla1  2: Pastilla2"))
        if pregunta==1:
            print ("Elegiste Pastilla 1")
            print ()
            Pastilla1 = int (input("Elija la cantidad "))
            if Pastilla1 > 6:
                print ("Oh!, Medicamentos insuficientes")
            elif Pastilla1 < 7:

                for i in range (Pastilla1):
                    print ("Entregando medicamento 1")
                    
                    medic1 ()
                    
                    
                    

            
        elif pregunta==2:
            print ("Elegiste Pastilla 2")
            print ()
            Pastilla2 = int (input("Elija la cantidad "))
            if Pastilla2 > 6:
                print ("Oh!, Medicamentos insuficientes")
            elif Pastilla2 < 7:
                
                for i in range (Pastilla2):
                    print ("Entregando medicamento 2")
                    
                    medic2 ()
                    
                    
                   
                    
        else:
            print("Opcion invalida, favor elija de nuevo")
            time.sleep(2)
     
    elif question == "N" :
        GPIO.cleanup()
        print ("Buen dia!")
        exit ()
    
    
    
    
    
    
#FALTA
#Try sirve para detectar errores dependiendo de la condicion que tenga el codigo

