import time as t
import turtle as t

def fibo(n):
	if n <= 1:
		return n 
	return fibo(n-2)+fibo(n-1)
		
def fibonacci(n):
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
			t.clock()
			fibonacci(n)
			temps = t.clock()
	finally:
		return (temps,n)
		

def chrono(n):
	t.clock()
	fibo(n)
	return t.clock()

def draw_bar(t, height):
    """ Get turtle t to draw one bar, of height. """
    t.begin_fill()           # Added this line
    t.left(90)
    t.forward(height)
    t.write("  "+ str(int(height*1000)))
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.end_fill()             # Added this line
    t.forward(5)	

wn = t.Screen()
tess = t.Turtle()
tess.pu()
tess.backward(800)
tess.right(90)
tess.forward(450)
tess.left(90)
tess.pd()
	
for n in range(31):
	draw_bar(tess,fibonacci(n)/1000)

wn.mainloop()