#bitwise operator

def bitwiseAndOr():
	a = 5
	b = 2

	# 0101 and 0010 = 0000
	print(a & b)
	# 0101 or 0010 = 0110
	#Inclusive Or
	print(a | b)
	#Exclusive Or
	print(a ^ b)

def shiftLeftAndRight():
	a = 5
	b = 2

	#shift left akan menggeser bit sebanyak b kali, simplenya (ingat biner 8 bit)
	# 0000 0101 =>
	# 5 shl 2 = geser 1 kali ke kiri => 0000 1010 = 10
	# 5 shl 2 = geser 1 kali ke kiri => 0001 0100 = 20
	print(a << b)
	# 5 shr 2 = geser 1 kali ke kanan => 0000 0010 = 2
	# 5 shr 2 = geser 1 kali ke kanan => 0000 0001 = 1
	print(a >> b)


#drive your function here
print('shl and shr')
shiftLeftAndRight()
print('bitwise and or')
bitwiseAndOr()