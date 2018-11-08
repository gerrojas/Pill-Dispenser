#Horario de funcionamiento
import schedule
#El reloj me registra la hora actual
import time
localtime = time.asctime (time.localtime(time.time()))
print ("Fecha y hora actual:")
print (localtime)
def job ():
   print ("Trabajando...")
schedule.every(1).minute.do(job)
schedule.every(1).hour.do(job)
schedule.every(1).day.at("20:28").do(job)
schedule.every(5).to(10).days.do(job)
schedule.every(1).monday.do(job)
schedule.every(1).wednesday.at("19:08").do(job)
#Condicion de Trabajando
while True:
      schedule.run_pending()
      time.sleep(1)
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
