#import C style for division 
from __future__ import division

#decrement
def decrement():
	x = 6
	y = 6

	x -= 1
	y -= 1

	print("this is x: %d" %x)
	print("this is y: %d" %y)

#python doesn't process ++ and -- as inc opt
def increment():
	x = 5
	y = 5

	x += 1
	y += 1

	print("this is x: %d" %x)
	print("this is y: %d" %y)

def moduloAB(a,b):
	return a % b

def divideAB(a,b):
	return float(a / b)

def productAB(a,b):
	return a * b

def minusAB(a,b):
	return a - b

def sumAB(a,b):
	return a + b

def haloDuniaKombinasi(nama, umur):
	print("halo %s , umur kamu sekarang %d" %(nama, umur))

def haloDuniaWithParam(param):
	print("halo %s apa kabar...?" % param)

def haloDunia():
	print("halo dunia")


#drive your function here

haloDunia()
haloDuniaWithParam('ekoman')
haloDuniaKombinasi('eko',23)
print("sum a and b is... %d" %(sumAB(5,10)))
print("min a and b is... %d" %(minusAB(5,7)))
print("product a and b is... %d" %(productAB(3,6)))
print("divide a and b is... %f" %(divideAB(4,6)))
print("modulo a and b is... %d" %(moduloAB(20,9)))
print("increment me.. ")
increment()
print("decrement me.. ")
decrement()