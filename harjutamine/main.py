#first_name = "Marten"
#last_name = "Keldrima"
#full_name = first_name +"  "+ last_name
#print("Hello " +full_name)
#age = 14
#print(age)
#height = 173.8
#print("Your height is " + str(height) + "cm")
#print(type(height))
#human = False
#print("Are you a human: " + str(human))
#name = "Marten"
#age = 14
#attractive = false
#name, age, attractive = "Marten", 14, False
#print(name)
#print(age)
#print(attractive)
#name = "Marten"
#print(len(name))
#print(name.capitalize())
#print(name.upper())
#(name.lower())
#print(name.isdigit())
#print(name.isalpha())
#print(name.count(a))
#print(name.replace("a", "o"))
#print(name*3)
#name = input("What is your name? ")
#age = int(input("How old are you? "))
#height = float(input("How tall are you? "))
#age = age + 1
#print("Hello " + name)
#print("You are " + str(age) + " years old")
#print("You are " + str(height) + " cm high.")
#pi = 3.1415
#x = 1
#y = 2
#z = 3
#print(max(x, y, z))
#print(min(x, y, z))
#print(round(pi))
#print(math.ceil(pi))
#print(math.floor(pi))
#print(abs(pi))
#print(pow(pi,2))
#print(math.sqrt(420))
#nimi = 'Fc Flora'
#nimi_fc = nimi[3:8]
#slice = slice(3,-1)
#print((nimi)[slice])
#while 1==1:
   # print("Help!")
#for i in range(10):
    #print(i + 1)
#for i in range(50,100+1,2):
    #print(i)
#for i in "Marten Alvin":
    #print(i)
#import time
#for seconds in range(10,0,-1):
    #print(seconds)
    #time.sleep(1)
#print("Happy new year!")
#rows = int(input("How many rows? "))
#column = int(input("How many columns? "))
#symbol = input("Enter a symbol to use: ")
#for i in range(rows):
    #for j in range(column):
       # print(symbol, end="")
    #print()
#while True:
    #klubi = input("Mis klubi sa toetad? ")
    #if klubi !="":
        #break
#klubi = ["Läänemaa jk", "Fc Flora", "Levaadia"]
#print(klubi[1])
#klubi.append("Paide JK")
#klubi.remiove("Levaadia")
#klubi.insert(0, "Pärnu JK")
#klubi.sort()
#klubi.clear()
#for x in klubi:
    #print(x)
#print("Tere!")
# = input("Mis on teie eesnimi? ")
#while True:
    #lemmikklubi = input("Mis on teie lemmikklubi, " + eesnimi + "?")
   # lemmikklubi = lemmikklubi.lower()
   # if lemmikklubi !="":
       # break
#if lemmikklubi == 'fcflora':
   #print("Palju õnne liiga võidu puhul!")
#else: print(lemmikklubi + " on hea klubi!")
#name = "marten ALvin!"
#if(name[0].islower()):
    #name = name.capitalize()
#first_name = name[:6].upper()
#last_name = name[7:].lower()
#last_taht = name[-1]
#print(last_taht)
#def hello(name):
    #print("Hello "+name)
    #print("Have a nice day!")
#hello("Marten")
#def multiply(number1, number2):
   # return number1 * number2
#x = multiply(6,8)
#print(x)
#import messages as msg
#msg.hello()
#from cat import Car
#car_1 = Car("Chevy", "Corvette", 2021, "blue")
#car_2 = Car("Ferrari", "F40", 1987, "red")
#print(car_2.make)
#print(car_2.model)
#print(car_2.year)
#print(car_2.color)
#car_1.drive()
#car_1.stop()
class Animal:

    alive = True
    def eat(self):
        print("This animal is eating")

    def sleep(self):
        print("This animal is sleeping")

class Rabbit(Animal):
    def run(self):
        print("This rabbit is running")

class Fish(Animal):
    def swim(self):
        print("This fish is swimming")

class Hawk(Animal):
    def fly(self):
        print("This hawk is flying")

rabbit = Rabbit()
fish = Fish()
hawk = Hawk()

print(rabbit.alive)
fish.eat()
hawk.sleep()
hawk.fly()

class Team:
    name = ""
    results = []







