# CTI - 110
# M3HW1 : Age Classifier
# Schweikart, Brian
# 09/14/2017

def main():
    print('Please enter whole number, round up or down')
# This is to have user input age and then classify infant, child,...
# Age listing

    Age_a = 1 
    Age_b = 13
    Age_c = 20
    
# 1 year or less = infant
# 1 year less then 13 = child
# 13 years - 19 = teenager
# 20 + = Adult

# user input for age
    age =int(input('Enter age'))

    if age <= Age_a:
        print('Infant')
    elif age > Age_a and age < Age_b:
        print('Child')
    elif age >= Age_b and age < Age_c:
        print('Teenager')
    else:
        print('Adult')
   


# program start
main()

        
        

    
