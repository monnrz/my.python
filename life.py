# project created on the 26th april 2023

import math

username = input("What is your name? ")
salary = input("What is your annual salary? ")
hoursworked = input("How many hours a week do you work? ")

# maths to work out how much you earn per hour

weeklysalary = int(salary) / 52
hourlysalary = int(weeklysalary) / int(hoursworked)

# maths to work out bi weekly hours

twoweekhours = int(hoursworked) * 2

print ("Thank you for providing this information " + (username) + ".")

x = input ("What is the name of the item you would like to buy? ")
y = input ("How much does this cost in GBP? £")
 
# math for how many hours item will take to pay

hourcost = int(y) / int(hourlysalary)

hourcostround = round(hourcost, 2)

if int(hourcostround) < int(hoursworked):
    print ((username) + ", you will have to work for " + str(hourcostround) + " hours to pay for an " + (x) + "... is it really worth it?")
elif int(hourcostround) > int(twoweekhours):
    print ((username) + ", you will have to work for " + str(hourcostround) + " hours to pay for an " + (x) + "... NO... just NO!") 
else:
    print ((username) + ", you will have to work for " + str(hourcostround) + " hours to pay for an " + (x) + "... that is over a weeks work?!")

