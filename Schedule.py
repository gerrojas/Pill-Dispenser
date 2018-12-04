#Proceso inicia
def mensaje ():
    print ("Pill Dispenser")
def job ():
   print ("Entregando...")
def saludo ():
   print ("Iniciando...")

schedule.every
schedule.every(20).minutes.do(mensaje)
schedule.every(1).hour.do(job)
schedule.every(1).day.at("20:55").do(job)
schedule.every(5).to(10).days.do(job)
schedule.every(1).monday.do(job)
schedule.every(1).wednesday.at("19:08").do(saludo)
time.sleep(1)
