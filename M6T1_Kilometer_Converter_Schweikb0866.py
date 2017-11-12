# CTI-110
# M6T1 - Software Sales
# Schweikart, Brian 0866
# 10/1/2017

CONVERSION_FACTOR = 0.6214

def main():
	# Get the distance in kilometers
	kilometers = float(input("Enter the distance in kilometers: "))
	
	# Display the distance converted to miles
	show_miles(kilometers)
	
	
def show_miles(km):
	# Calculate miles	
	miles = km * CONVERSION_FACTOR

	# Display the miles
	print(km, 'kilometers equals',miles, 'miles')
	
main()