#iterative operation in python

def continueMyLoop():
	for i in range(1,6):
		if i % 2 == 0:
			continue
		print('my number is.. %d ' %i)
		pass

def breakMyLoop():
	i = 10
	while i > 0:
		if(i % 3 == 0):
			print("breaking my loop in %d" %i)
			break
		print("continue... %d " %i)
		i -= 1
		pass

def customYourLoop():
	for i in range(2,10,3):
		print("jump up to %d " % i)

def whileMyLoop():
	i = 5
	while i > 0:
		print("go my .. %d" %i)
		i -= 1
		pass

def forMyLoop():
	for i in range(1,5):
		print("go.. %d" %i)



#drive your function here
forMyLoop()
whileMyLoop()
customYourLoop()
breakMyLoop()
continueMyLoop()