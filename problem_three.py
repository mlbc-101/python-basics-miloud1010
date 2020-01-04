"""Write a program that solves second degree equation of the form ax^2 +bx + c = 0."""
import math as mt # the Math Library

a = int(input('Enter a : '))
b = int(input('Enter b : '))
c = int(input('Enter c : '))

delta = b**2 - 4*a*c

if delta < 0 :
    print("the equation has not a solutions")
elif delta == 0 :
    print("the equation have one solution which is :", -b/2 * a)
else:
    print("the equation have two solution wich are: \n")
    print("1st Solution is:",(-b -mt.sqrt(delta)) / 2* a)
    print("2nd Solution is:",(-b +mt.sqrt(delta)) / 2* a)    

