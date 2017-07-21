import turtle


def triangle(someturtle):
 for i in range(0,3): 
   someturtle.forward(100) 
   someturtle.left(120)
 
def triangle2(someturtle,number):
 for i in range(0,3): 
   someturtle.forward(100-number) 
   someturtle.left(120)



def art():

 window=turtle.Screen()
 window.bgcolor("orange")
 raghu=turtle.Turtle()
 raghu.speed(200)
 raghu.shape("turtle")
 for i in range(0,36):
   triangle(raghu)
   raghu.right(10)
    
 for j in range(0,36):
  triangle2(raghu,5)
  raghu.right(10)
  
 for j in range(0,36):
  triangle2(raghu,10)
  raghu.right(10)
     	
 #raghu.right(60)
 #raghu.forward(100)	
 window.exitonclick()




art()