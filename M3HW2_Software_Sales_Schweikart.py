# CTI-110
# M3HW2 - Software Sales
# Schweikart, Brian 0866
# 09/16/2017
# This is to show what what bulk discount pricing would be

# Retail = 99

def main():
	
	print('Retail price $99')
	print('ORDER QUANTITY DISCOUNT')
	print('10 - 19 = 10% off')
	print('20 - 49 = 20% off')
	print('50 - 99 = 30% off')
	print('100 or more = 40% off')

	price = 99.00
	
	# user inputs quanity of product
	quanity = int(input('Enter the quanity you would like: '))
	
	if quanity < 10:
		print("We're sorry but your quanity does not qualfy for a discount")
		discount = 0
		
	if quanity >= 10 < 19:
		print("You qualfied for a discount")
		discount = float(99 * 0.1) * quanity 

	if quanity >= 20 < 49:
		discount = float(99 * 0.2) * quanity

	if quanity >= 50 < 99:
		discount = float(99 * 0.3) * quanity

	if quanity >= 100:
		discount = float(99 * 0.4) * quanity
			
	total = quanity * price - discount

	base = quanity * price 

	print("Your sub total is ${:,.2f}" .format(base))
	print("Your discount is ${:,.2f}" .format(discount))
	print("Your total is ${:,.2f}" .format(total))
					
main()



			
	