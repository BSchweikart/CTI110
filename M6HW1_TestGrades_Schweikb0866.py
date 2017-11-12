# Feet to Inches
# 10/3/2017
# CTI-110 M6HW1_Test Average and Grade
# Brian Schweikart
#



def main():
	# user inputs the score of each test
	score1 = int(input("Please enter a score for test 1: "))
	print(" That\'s a(n): ", determine_grade(score1))
	score2 = int(input("Please enter a score for test 2: "))
	print(" That\'s a(n): ", determine_grade(score2))
	score3 = int(input("Please enter a score for test 3: "))
	print(" That\'s a(n): ", determine_grade(score3))
	score4 = int(input("Please enter a score for test 4: "))
	print(" That\'s a(n): ", determine_grade(score4))
	score5 = int(input("Please enter a score for test 5: "))
	print(" That\'s a(n): ", determine_grade(score5))	
	# Over all value of test scores and input calc
	total = (score1 + score2 + score3 + score4 + score5)
	avg = cal_average(total)
	letter_grade = determine_grade(avg)
	
	# Out put of user input information
	print("Your average grade is: ", cal_average(total))
	print("That/'s a(n) ", letter_grade)
	
	
# find average of value of tests scores	
def cal_average(total):
	return total /5
	
	
# Take average total to find letter grade	
def determine_grade(grade):
	if 90 <= grade <=100:
		return 'A'
	elif 80 <= grade <= 89:
		return 'B'	
	elif 70 <= grade <= 79:
		return 'C'	
	elif 60 <= grade <= 69:
		return 'D'		
	else:
		return 'F'
	
	
main()	
	

