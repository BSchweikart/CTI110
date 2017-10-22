# M5T1B: Initials
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
	
	kriina.setheading(90)
	kriina.forward(200)
	kriina.setheading(0)
	kriina.circle(-50,180)
	kriina.setheading(0)
	kriina.circle(-50,180)
						
	kriina.penup()
	kriina.forward(-100)
	kriina.pendown()
						
	kriina.setheading(0)
	kriina.forward(50)
	kriina.circle(50,180)
	kriina.circle(-50,180)
	kriina.forward(50)
		
		
	return main()
			
main()