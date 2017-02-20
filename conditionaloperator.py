#conditional operation in python

#bitwise operator

#logical operator fizz buzz
def myLogicalOperator(number):
	if((number % 5 == 0) and (number % 3 == 0)):
		print 'fizz buzz'
	elif ((number % 5 == 0) or (number % 3 == 0)):
		print 'buzz'
	else:
		print 'you are not fizz buzz team'


#ternary operation
def myTernaryFunc(number):
	return ('genap','ganjil') [number % 2 == 1]

#simple if--else if with else condition
def isPositifOrNegatifNumber(number):
	if number > 0:
		print("%d is positif number" %number)
	elif number < 0:
		print("%d is negatif number" %number)
	else:
		print("%d is neutral number" %number)


#simple if condition
def isEvenNumber(number):
	if(number % 2 == 0):
		print("your number %d is even" %number)


#drive your function here
a = 5
b = 8
isEvenNumber(4)
isPositifOrNegatifNumber(-5)
isPositifOrNegatifNumber(10)
isPositifOrNegatifNumber(0)
print("%d is... %s" % (a,myTernaryFunc(5)))
print("%d is... %s" % (b,myTernaryFunc(8)))
myLogicalOperator(15)
myLogicalOperator(10)
myLogicalOperator(9)
myLogicalOperator(4)
