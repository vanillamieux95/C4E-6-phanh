##n = input("Nom:")
##print ('hey', n, 'come and play')

# Drawing and color filling
from turtle import *

colormode(255) #he mau 8bit á in rgb and hex

for n in range (7, 2, -1): #start, stop, step jump
    color((148, 186, 137), (50 + n * 20, 30, 30)) #gradian color as drawing
    begin_fill()
    for _ in range (n):
        forward (121)
        left (360/n)
    end_fill()
