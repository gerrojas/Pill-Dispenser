#El reloj me registra la hora actual
import time
localtime = time.asctime (time.localtime(time.time()))
print ("Local current time:")
print (localtime)
#Caledario del Mes actual
import calendar
cal= calendar.month (2018,10)
print ("Calendario del Mes")
print (cal)
#Proceso de la Interfaz
nombre = input ("Ingrese su nombre")
requisito1 = input ("Ingrese opcion")
print ("Bienvenido")
print (nombre)
print ("Elegiste la siguiente opcion")
print (requisito1)
Pastilla1 = int (input("Elija la cantidad 1"))
if Pastilla1 > 15 :
   print ("Medicamentos insuficientes")
elif Pastilla1 < 15 :
   print ("Entregando medicamento")
Pastilla2 = int (input("Elija la cantidad 2"))
if Pastilla2 > 20 :
    print ("Medicamentos insuficientes")
elif Pastilla2 < 20 :
    print ("Entregando medicamento")
Pastilla3 = int (input("Elija la cantidad 3"))
if Pastilla3 > 17 :
    print ("Medicamentos insuficientes")
elif Pastilla3 < 17 :
    print ("Entregando medicamento")
