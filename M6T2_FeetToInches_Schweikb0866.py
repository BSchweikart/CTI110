# Feet to Inches
# 10/3/2017
# CTI-110 M6T2_FeetToInches
# Brian Schweikart
#

INCHES_PER_FOOT = 12

def main():
	# Get a number of feet from the user.
	feet = int(input("Enter a number of feet: "))
	
	# Convert that to inches
	print(feet, "equals", feet_to_inches(feet), "inches")
	
	
def feet_to_inches(feet):
	return feet * INCHES_PER_FOOT
	
# Call the mian function
main() 	