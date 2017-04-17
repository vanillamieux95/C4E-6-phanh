###Calcul8 ircle area
##r = int(input("Circle radius: "))
##
##area = 3.14 * (r**2)
##
##print (area)
##print ("Area = ", area)
##
###Converting Celcius to Fahrenheit
##c = int(input("Enter the temperature in Celcius? "))
##f = c * 9/5 +32
##
##print (f)
##print (c, "(C) = ", f, "(F)")
##
###Drawing w Turtle
##
from turtle import *

speed(-1)
##
##color("Green","Yellow")
##begin_fill()
##for _ in range (4):
##    forward (121)
##    right (90)
##    
##for _ in range (3):
##    forward (121)
##    left (360/3)
##end_fill()

#Drawing circle w Turtle
import turtle

color ("green", "white")
begin_fill()
for _ in range (25):
    turtle.circle(70)
    turtle.left (15)
end_fill()
