import turtle
def draw_square(someturtle):
  for food in range(0,4): 
     someturtle.forward(100)
     someturtle.right(90)
  
def art():
 window=turtle.Screen()
 window.bgcolor("red")
 brad=turtle.Turtle()
 brad.color("yellow")
 brad.shape("circle")
 brad.speed(200)
 for i in range(0,36):
   draw_square(brad)
   brad.right(10)
 bhai=turtle.Turtle()
 bhai.shape("arrow")
 bhai.color("blue")
 bhai.circle(100)
  
 window.exitonclick()



art()