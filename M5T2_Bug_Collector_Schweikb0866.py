# M5T1B: Bug Collector
# CTI - 110
# Schweikb0866
# 10/21/17

def main():
	total = 0
	# 7 days
	for day in range(1, 8):
		
		# Prompt the user
		print("Enter the bugs collected on day:", day)
		
		# Input the number of bugs
		bugs = int(input())
		total += bugs
		
		print("You have collected a total of", total,"bugs")
	
	
main()