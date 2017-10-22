# M5HW1
# CTI - 110
# Schweikb0866
# 10/10/17

def main():
	
# User inputs information for values
	speed = int(input('What is the speed of the vehicle in mph?: '))

	time = int(input('How many hours traveled? '))
	
	if speed <= 0 and time <= 0:
		print('Please enter a value for speed and hours greater than 0')
	
	print ('Hours \t Distance Traveled')
	
	print ('-----------------------------------------------')

#Calculate Distance Traveled
	for time in range(1, 1 + time):
		distance = speed * time
		print (time, '\t' ,distance, 'miles')
	
	
main()