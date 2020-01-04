"""Write a program which can compute the factorial of a given numbers."""

num = int(input("enter the Number: "))

if(num < 0):
	print("Error can't calculate the factorial of this number !!")
else:
	fact = 1
	counter = num
	while counter > 0:
		fact *= counter
		counter -= 1 # this is because N! = N * (N-1)!
	
	print(num, '! = ', fact)