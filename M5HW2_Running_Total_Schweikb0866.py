# M5HW2
# CTI - 110
# Schweikb0866
# 10/19/17

def main():
	sum = 0
	
	while True:
		num = input("Please enter a number: ")
		
		while float(num) >= 0:
			sum += float(num)
			break
		
		else:
			print("Your total is:",sum)
			break
main()