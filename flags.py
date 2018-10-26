#Bastien Wiaux et Max Wiberg, 10/10/18

import turtle
import math

wn = turtle.Screen()
wn.title("The Flag Man")
wn.bgcolor("black")
tortue = turtle.Turtle()
tortue.speed("fastest")
tortue.hideturtle()

def square(size, color):
    """Trace un carré plein de taille `size` et de couleur `color`.

    pre: `color` spécifie une couleur.
         La tortue `tortue` est initialisée.
         La tortue est placée à un sommet et orientée en direction d'un
         côté du carré.
    post: Le carré a été tracé sur la droite du premier côté.
          La tortue est à la même position et orientation qu'au départ.
    """
    tortue.color(color)
    tortue.pendown()
    tortue.begin_fill()
    for i in range(4):
        tortue.forward(size)
        tortue.left(90)
    tortue.end_fill()
    tortue.penup()

def etoile(size, color):
    """Trace une étoile pleine de taille `size` et de couleur `color`.

    pre: `color` spécifie une couleur.
         La tortue `tortue` est initialisée.
         La tortue est placée à un sommet et orientée en direction
         du bord supérieur de la branche gauche de l'étoile .
    post: La tortue est à la même position et orientation qu'au départ.
    """
    tortue.color(color)
    tortue.pendown()
    tortue.begin_fill()
    for i in range(5):
        tortue.forward(size)
        tortue.right(180-36)
    tortue.end_fill()
    tortue.penup()

def rectangle(width, height, color):
    """Trace un rectangle plein de dimensions width x height et de couleur `color`.

    pre: `color` spécifie une couleur.
         La tortue `tortue` est initialisée.
         La tortue est placée à un sommet et orientée en direction d'une
         longueur du rectangle.
    post: Le rectangle a été tracé au dessus du premier côté.
          La tortue est à la même position et orientation qu'au départ.
    """
    tortue.color(color)
    tortue.pendown()
    tortue.begin_fill()
    for i in range(2):
        tortue.forward(height)
        tortue.left(90)
        tortue.forward(width)
        tortue.left(90)
    tortue.end_fill()
    tortue.penup()

def cross(size, color):
    """Trace une croix pleine de taille `size` et de couleur `color`.

    pre: `color` spécifie une couleur.
         La tortue `tortue` est initialisée.
         La tortue est placée à un sommet et orientée en direction
         du bord inférieur de la branche gauche de la croix .
    post: La tortue est à la même position et orientation qu'au départ.
    """
    rectangle(size/4,size,color)
    tortue.forward(size*3/8)
    tortue.right(90)
    tortue.forward(size*3/8)
    tortue.left(90)
    rectangle(size,size/4,color)
    tortue.left(90)
    tortue.forward(size*3/8)
    tortue.right(90)
    tortue.backward(size*3/8)
    

def three_band_flag(width, color1, color2, color3, orientation = "vertical"):
    """Trace un drapeau trois bandes de dimensions width x 3/2*width.

    pre: La tortue `tortue` est initialisée.
         La tortue est placée à un sommet et orientée en direction d'une
         longueur du drapeau.
    post: Le drapeau a été tracé sur la droite du premier côté.
          La tortue est à la même position et orientation qu'au départ.
    """
    if orientation == "vertical":
        tortue.right(90)
        for color in [color1, color2, color3]:
            rectangle(width/2,width,color)
            tortue.left(90)
            tortue.forward(width/2)
            tortue.right(90)
        tortue.left(90)
        tortue.backward(3/2*width)
    else:
        tortue.right(90)
        tortue.forward(width/3)
        tortue.left(90)
        for color in [color1, color2, color3]:
            rectangle(width/3,3/2*width,color)
            tortue.right(90)
            tortue.forward(width/3)
            tortue.left(90)
        tortue.right(90)
        tortue.backward(4/3*width)
        tortue.left(90)
    
def belgian_flag(width):
    """Trace un drapeau belge de dimensions width x 3/2*width.

    pre: La tortue `tortue` est initialisée.
         La tortue est placée à un sommet et orientée en direction d'une
         longueur du drapeau.
    post: Le drapeau a été tracé sur la droite du premier côté.
          La tortue est à la même position et orientation qu'au départ.
    """
    three_band_flag(width,"black","yellow","red")

def european_flag(width):
    """Trace un drapeau européen de dimensions width x 3/2*width.

    pre: La tortue `tortue` est initialisée.
         La tortue est placée à un sommet et orientée en direction d'un
         côté du drapeau.
    post: Le drapeau a été tracé sur la droite du premier côté.
          La tortue est à la même position et orientation qu'au départ.
    """
    rectangle(width,width*3/2,"blue")
    tortue.left(math.degrees(math.atan(2/3)))
    tortue.forward(math.sqrt(width**2+(width*3/2)**2)/2)
    tortue.right(math.degrees(math.atan(2/3))+90)
    tortue.forward(width/3)
    tortue.left(90)
    for i in range(12):
        tortue.circle(width/3,extent=30)
        tortue.right((30*(i+1))%360)
        etoile(width/18,"yellow")
        tortue.left((30*(i+1))%360)

def usa_flag(width):
    """Trace un drapeau americain de dimensions width x 1.9*width.

    pre: La tortue `tortue` est initialisée.
         La tortue est placée à un sommet et orientée en direction d'un
         côté du drapeau.
    post: Le drapeau a été tracé sur la droite du premier côté.
          La tortue est à la même position et orientation qu'au départ.
    """
    tortue.right(90)
    tortue.forward(width/13)
    tortue.left(90)
    rectangle(width/13,width*1.9,"red")
    for i in range(6):
        for color in ["white","red"]:
            tortue.right(90)
            tortue.forward(width/13)
            tortue.left(90)
            rectangle(width/13,width*1.9,color)
    tortue.left(90)
    tortue.forward(width*6/13)
    tortue.right(90)
    rectangle(width*7/13,width*3.8/5,"blue")
    tortue.left(90)
    tortue.forward(width*7/130)
    tortue.right(90)
    tortue.backward(width/13*4/10)
    for i in range(5):
        for j in range(6):
            tortue.forward(width*3.8/60)
            etoile(width/13*4/5,"white")
            tortue.forward(width*3.8/60)
        if i != 4:
            tortue.left(90)
            tortue.forward(width*7/130)
            tortue.right(90)
            for j in range(5):
                tortue.backward(width*3.8/60*2)
                etoile(width/13*4/5,"white")
            tortue.backward(width*3.8/60*2)
            tortue.left(90)
            tortue.forward(width*7/130)
            tortue.right(90)

def greek_flag(width):
    """Trace un drapeau grec de dimensions width x 3/2*width.

    pre: La tortue `tortue` est initialisée.
         La tortue est placée à un sommet et orientée en direction d'un
         côté du drapeau.
    post: Le drapeau a été tracé sur la droite du premier côté.
          La tortue est à la même position et orientation qu'au départ.
    """
    tortue.right(90)
    tortue.forward(width/9)
    tortue.left(90)
    rectangle(width/9,width*3/2,"blue")
    for i in range(4):
        for color in ["white","blue"]:
            tortue.right(90)
            tortue.forward(width/9)
            tortue.left(90)
            rectangle(width/9,width*3/2,color)
    tortue.left(90)
    tortue.forward(width*4/9)
    tortue.right(90)
    square(width*5/9,"blue")
    tortue.left(90)
    tortue.forward(width*2/9)
    tortue.right(90)
    rectangle(width/9,width*5/9,"white")
    tortue.forward(width*2/9)
    tortue.right(90)
    tortue.forward(width*2/9)
    tortue.left(90)
    rectangle(width*5/9,width/9,"white")
    tortue.backward(width*2/9)
    tortue.left(90)
    tortue.forward(width*5/9)
    tortue.right(90)

def suisse_flag(width):
    """Trace un drapeau georgien de dimensions width x 13/8*width.

    pre: La tortue `tortue` est initialisée.
         La tortue est placée à un sommet et orientée en direction d'un
         côté du drapeau.
    post: Le drapeau a été tracé sur la droite du premier côté.
          La tortue est sur le bord gauche de la croix du coin droite-bas.
    """
    
    rectangle(width,width*13/8,"white")
    tortue.forward(width*9/16)
    tortue.left(90)
    tortue.forward(width*7/16)
    tortue.right(90)
    cross(width/2,"red")

def georgia_flag(width):
    """Trace un drapeau georgien de dimensions width x 3/2*width.

    pre: La tortue `tortue` est initialisée.
         La tortue est placée à un sommet et orientée en direction d'un
         côté du drapeau.
    post: Le drapeau a été tracé sur la droite du premier côté.
          La tortue est à la même position et orientation qu'au départ.
    """
    tortue.right(90)
    tortue.forward(width)
    tortue.left(90)
    rectangle(width,width*3/2,"red")
    
    suisse_flag(width*2/5)
    
    tortue.backward(width*9/40)
    tortue.left(90)
    tortue.forward(width*17/40)
    tortue.right(90)
    
    suisse_flag(width*2/5)

    tortue.forward(width*5/8)
    tortue.right(90)
    tortue.forward(width*7/40)
    tortue.left(90)
    
    suisse_flag(width*2/5)
    
    tortue.backward(width*9/40)
    tortue.right(90)
    tortue.forward(width*31/40)
    tortue.left(90)
    
    suisse_flag(width*2/5)

def japan_flag(width):
    """Trace un drapeau japonais de dimensions width x 3/2*width.

    pre: La tortue `tortue` est initialisée.
         La tortue est placée à un sommet et orientée en direction d'un
         côté du drapeau.
    post: Le drapeau a été tracé sur la droite du premier côté.
          La tortue est à la même position et orientation qu'au départ.
    """
    tortue.right(90)
    tortue.forward(width)
    tortue.left(90)
    rectangle(width,width*3/2,"white")
    tortue.left(math.degrees(math.atan(2/3)))
    tortue.forward(math.sqrt(width**2+(width*3/2)**2)/2)
    tortue.right(math.degrees(math.atan(2/3))+90)
    tortue.forward(width*3/10)
    tortue.left(90)
    tortue.color("red")
    tortue.begin_fill()
    tortue.circle(width*3/10)
    tortue.end_fill()

#permet de voir les parties noires
tortue.goto(-228,-203)
rectangle(106,156,"white")
tortue.goto(72,-203)
rectangle(106,156,"white")

#dessine le "bonhomme"
tortue.goto(-150,-100)
european_flag(200)
tortue.goto(-225,-100)
belgian_flag(100)
tortue.goto(-300,-200)
three_band_flag(100,"blue","white","red")
tortue.goto(75,-100)
three_band_flag(100,"black","red","yellow","horizontal")
tortue.goto(150,-200)
three_band_flag(100,"blue","white","red","horizontal")
tortue.goto(150,150)
three_band_flag(100,"red","white","light blue","horizontal")
tortue.goto(225,250)
greek_flag(100)
tortue.goto(-300,100)
georgia_flag(100)
tortue.goto(-375,0)
japan_flag(100)
tortue.goto(-95,225)
usa_flag(100)

wn.mainloop()
