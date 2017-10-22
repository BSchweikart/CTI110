# M5T1a
# CTI - 110
# Schweikb0866
# 10/19/17

def main():

	import turtle
	wn = turtle.Screen()
	wn.bgcolor("black")
	wn.title("Kriina & Norgana")

	kriina = turtle.Turtle()
	kriina.color("pink")
	kriina.pensize(5)

	norgana = turtle.Turtle()
	norgana.color("green")
	norgana.pensize(4)
	
	i = 0
	while i < 8:
		kriina.forward(150)
		kriina.left(120)	
		
		norgana.forward(50)
		norgana.left(90)
		
		i = i+1	
	
main()
		
	
	

