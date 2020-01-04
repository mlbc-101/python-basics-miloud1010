"""
Write a program which will find and display all such numbers which are divisible by 7 but are not a multiple of 5,
between 2000 and 3200 (both included).
"""

number = 2000
while number <= 3200:
	if number % 7 == 0 and number % 5 != 0:
		print(number)
	number+=1