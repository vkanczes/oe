# Veronica Kanczes - Assignment 1321

# Part I:

# This program will ask user for temperature in Fahrenheit and convert and print the temperature in celsius

# get the Fahrenheit temp and convert to an integer
f = int(input("Enter temperature in Fahrenheit: "))

# convert to celsius
c = (5/9) * (f - 32)

# print the result 
print ("The temperature in Celsius:  ", c)


# Part II

# This program will calculate the area of a trapezoid

# get the height, bottom length and top length of the trapezoid
height = int(input("Enter height of the trapezoid: "))
bottomLength = int(input("Enter bottom base length of the trapezoid: "))
topLength = int(input("Enter top base length of the trapezoid: "))

# calculate the area of the trapezoid
area = 1/2 * (bottomLength + topLength) * height

# print the result 
print ("The area of the trapezoid is:  ", area)

