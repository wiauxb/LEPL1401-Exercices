import time
import turtle as t

count = [0,0,0]

def fibo(n):
	global count
	count[0] += 1
	if n <= 1:
		return n 
	return fibo(n-2)+fibo(n-1)
		
def fibonacci(n):
	global count
	count[1] += 1
	rep = [0,1]
	if n >= 2:
		for i in range(n-1):
			rep.append(rep[-1]+rep[-2])
	else:
		return n
	return rep[-1]

def chrono_abs():
	temps = 0
	n = 0
	try:
		while temps < 10:
			n += 1
			time.clock()
			fibonacci(n)
			temps = time.clock()
	finally:
		return (temps,n)
		

def chrono(fct,n):
	tp = time.clock()
	fct(n)
	return time.clock()-tp

def draw_bar(t, height,echelle = 1):
    """ Get turtle t to draw one bar, of height. """
    t.begin_fill()           # Added this line
    t.left(90)
    t.forward(height*echelle)
    t.write("  "+ str(float(height)))
    t.right(90)
    t.forward(25)
    t.right(90)
    t.forward(height*echelle)
    t.left(90)
    t.end_fill()             # Added this line
    t.forward(3)	

wn = t.Screen()
tess = t.Turtle()
tess.speed("fastest")
tess.hideturtle()
tess.pu()
tess.goto(-850,-450)
tess.pd()
alex = tess.clone()
alex.color("red")
	
for n in range(31):
	count = [0,0,0]
	tess.color("black")
	fibo(n)
	draw_bar(tess,count[0],1/2500)
	fibonacci(n)
	draw_bar(alex,count[1])

tess.color("green")
tess.pu()
tess.goto(50,-450)
tess.pd()

for n in range(31):
	draw_bar(tess,fibo(n),1/1000)

tess.color("black")
tess.pu()
alex.pu()
tess.goto(50,0)
alex.goto(50,20)
tess.pd()
alex.pd()

for n in range(31):
	a = chrono(fibo,n)
	b = chrono(fibonacci,n)
	draw_bar(tess,a)
	draw_bar(alex,b)
	print(a,"\t",b)

wn.mainloop()