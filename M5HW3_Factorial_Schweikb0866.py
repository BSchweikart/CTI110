# M5HW3
# CTI - 110
# Schweikb0866
# 10/10/17

def main():
	
	num = int(input("Please enter a number to find the factorial "))

	factorial = 1

	if num < 0:
		print("Please enter a positive number")

	elif num == 0:
		print("The Factorial of 0 is 1")

	else:
		for i in range(1, num + 1):
			factorial *= i
	print("The factorial of", num, "is", factorial)
	
main()