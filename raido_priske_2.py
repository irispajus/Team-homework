#Programm, et lisada ja eemaldada automarke loendist
#Defineerin clear funktsiooni, et puhastada terminali
from os import system, name 
def clear(): 
  if name == 'nt': 
      x = system('cls') 
  else: 
      x = system('clear') 

def run():
    import time
    
    #Sätistan algsed andmed
    state = 0
    array_cars = ['audi', 'bmw', 'volkswagen', 'toyota', 'kia', 'lamborghini', 'porsche', 'lexus', 'ford', 'mazda']
    userinput = input("Sisesta automark\n")
    
    #Eemaldan sisestatud margi loendist
    while state == 0:
      if userinput in array_cars:
          clear()
          try:
            array_cars.remove(userinput)
            pass
          except:
            print('Error')
            pass

          #Prindin välja alles olevad autod
          print ('\nAlles on jaanud:\n')
          array_i = 0
          
          while array_i < len(array_cars):
            print(array_cars[array_i])
            array_i = array_i + 1
            
          state = 1
          
          time.sleep(2)
          clear()

          #Uus funktsioon, et lisada automark loendisse
          def addBrand():
            clear()
            brand = str(input('\nSisesta automark, kui ei taha rohkem sisestada, kirjuta "exit"\n'))
            if (brand == 'exit'):
              length = len(array_cars)
              i = 0
              while i < length:
                print (array_cars[i])
                i = i + 1
            else:
              array_cars.append(brand)
              print ('\nSisestasid: ' + str(brand))
              time.sleep(1)
              addBrand()
              
          addBrand()
          
      else:
        #Kontroll, et kui sisestatud automarki ei ole, siis sisestab kasutaja uuesti
          clear()
          print (userinput + ' meil ei ole')
          userinput = input("Sisesta automark\n")
run()