# COPYRIGHT 2016, Vida Dujmovic. All rights reserved.
# Any unauthorised distribution will constitute an infringement of copyright.

# Family name: Vida Dujmovic 
# Student number:  123456
# Course: IT1 1120 
# Assignment Number 1

import turtle

###################################################################
# Question 1
###################################################################

def lbs2kg(w):
    ''' (number)->number
    Returns the weight w expressed in pounds as killograms'''

    return 0.453592*w


###################################################################
# Question 2
###################################################################
def id_formater(fn, ln, appelation, city, year):
    ''' (str, str, str, str, int)->str
    Return ID info'''

    return appelation + ". " + ln + ", " + fn + " (" + city + ", " + str(year) + ")"


###################################################################
# Question 3
###################################################################
def limerick_maker():
    ''' (None)->None
    Print a customized limerick'''
    
    name = input("Enter your name: ")
    city = input("Enter your city of birth: ")

    print()
    print(name, "had funny funny hair")
    print("With tons and tons to spare") 
    print(name + "'s clippings made a wig") 
    print("It was very big") 
    print("And caused the townsfolk of", city, "to stare")


###################################################################
# Question 4
###################################################################
def id_formater_display():
    '''(None)->None
    Print an ID as formated'''

    first = input("What is your first name? ")
    last = input("What is your last name? ")
    ap = input("What is your appellation? ")
    place = input("Where were you born? ")
    year = int(input("What is your year of birth? "))

    s = id_formater(first, last, ap, place, year)
    print()
    print(s)



###################################################################
# Question 5
###################################################################

def l2loz(w):
    '''(number)->(int, number)
    Convertes weight w given in lbs expressed as lbs and oz'''

    l = int(w)
    o = (w-l) * 16
    return (l, o)

###################################################################
# Question 6
###################################################################
# solution by Ashwin Panchapakesan

def draw_soccer_field():
    '''
    (None)->None
    Draws a soccer_field with turtle graphics
    '''

    # to be done (or left up to the students)


    s = turtle.Screen()

    # set canvas size and bgcolor
    s.bgcolor('green')

    t = turtle.Turtle()
    t.speed(11)


    # draw stripes
    t.pensize(1)
    t.penup()
    t.goto(-250, 150)
    for _ in range(16):
        t.setheading(270)
        t.color('green', 'green')
        t.pendown()
        t.begin_fill()
        t.forward(300)
        t.left(90)
        t.forward(15)
        t.left(90)
        t.forward(300)
        t.left(90)
        t.forward(15)
        t.end_fill()
        
        t.left(180)
        t.forward(15)
        t.setheading(270)
        t.color('darkgreen', 'darkgreen')
        t.begin_fill()
        t.pendown()
        t.forward(300)
        t.left(90)
        t.forward(15)
        t.left(90)
        t.forward(300)
        t.left(90)
        t.forward(15)
        t.end_fill()
        t.backward(15)


    t.color('white')
    t.pensize(4)
    # go to top-left corner
    t.penup()
    t.goto(-250, -150)
    
    # draw rectangular field
    t.pendown()
    t.setheading(0)
    t.forward(500)
    t.left(90)
    t.forward(300)
    t.left(90)
    t.forward(500)
    t.left(90)
    t.forward(300)
    t.left(90)


    # draw center line and circle
    t.forward(250)
    t.left(90)
    t.forward(150)
    t.dot()
    t.forward(150)

    t.backward(200)
    t.right(90)
    t.circle(50)


    # draw corners
    t.penup()
    t.goto(-250, 150)
    t.setheading(270)
    t.forward(10)
    t.left(90)
    t.pendown()
    t.circle(10, 90)

    t.penup()
    t.goto(-250, -150)
    t.setheading(0)
    t.forward(10)
    t.left(90)
    t.pendown()
    t.circle(10, 90)

    t.penup()
    t.goto(250, -140)
    t.setheading(180)
    t.pendown()
    t.circle(10, 90)

    t.penup()
    t.goto(240, 150)
    t.setheading(270)
    t.pendown()
    t.circle(10, 90)

    
    # draw goalie zones
    t.penup()
    t.goto(-250, -100)
    t.pendown()
    t.setheading(0)
    t.forward(90)
    t.left(90)
    t.forward(200)
    t.left(90)
    t.forward(90)
    t.left(90)
    t.forward(50)
    t.left(90)
    t.forward(30)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(30)

    t.penup()
    t.goto(-190, 0)
    t.pendown()
    t.dot()


    t.penup()
    t.goto(250, 100)
    t.pendown()
    t.setheading(180)
    t.forward(90)
    t.left(90)
    t.forward(200)
    t.left(90)
    t.forward(90)
    t.left(90)
    t.forward(50)
    t.left(90)
    t.forward(30)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(30)
    t.penup()
    t.goto(190, 0)
    t.pendown()
    t.dot()
    

    # draw goalie circles
    t.penup()
    t.goto(-160, -30)
    t.pendown()
    t.setheading(0)
    t.circle(30, 180)


    t.penup()
    t.goto(160,30)
    t.pendown()
    t.setheading(180)
    t.circle(30, 180)
    

    input("Hit <ENTER> to quit... ")
    s.bye()
    


###################################################################
# Question 7
###################################################################

def median3(num1,num2,num3):
    '''(number, number, number)->(None)
    Displays message about medians of three numbers'''

    print(num1, "is a median. That is ", num3 >= num1 >= num2 or num2 >= num1 >= num3);
    print(num2, "is a median. That is ", num3 >= num2 >= num1 or num1 >= num2 >= num3)
    print(num3, "is a median. That is ", num2 >= num3 >= num1 or num1 >= num3 >= num2)

###################################################################
# Question 8
###################################################################

def below_parabola(a,b,p,q):
    '''(number, number, number, number)->bool
       Returns True if point (p,q) is below or on the parabola y=ax^2+b
       Precondition: a is a positive numbers'''
       
    return q <= a * p**2 + b 

###################################################################
# Question 9
###################################################################
def projected_grade(a1,A1,a2,A2,m,M):
    '''(int, int, int, int, int, int)->number
    Returns projected final course grade'''

    return 5 * (a1/A1 + a2/A2 +  (a1/A1+a2/A2)/2 ) + (m/M)*35 + (m/M)*50

###################################################################
# Question 10
###################################################################
def projected_grade_v2():
    '''(None)->None
    Prints info about projected final course grade'''

    a1 = int(input("How many points did you get in Assignment 1? "))
    A1 = int(input("What was the maximum possible number of points for Assignment 1? "))
    a2 = int(input("How many points did you get in Assignment 2? "))
    A2 = int(input("What was the maximum possible number of points for Assignment 2? "))
    m = int(input("How many points did you get on the midterm? "))
    M = int(input("What was the maximum possible number of points for the midterm? "))

    if m/M < 50:
        print("Your predicted final grade is", min(100*m/M, projected_grade(a1,A1,a2,A2,m,M)), "%")
    else:
        print("Your predicted final grade is", projected_grade(a1,A1,a2,A2,m,M), "%")
        



###################################################################
# Question 11
###################################################################
def change_to_coins(amount):
    '''
       (number)->Tuple
       Returns the minimum number of quarters, dimes, nickels,
       and pennies that sum up to amount 
       Precondtion: amount is a positive number 
    '''

    cents = round(amount*100) 
    quarters = cents//25
    cents %= 25    #this computes remaining number of cents after quarters are removed

    dimes = cents//10
    cents %= 10

    nickels = cents//5
    pennies %= 5
    
    return (quarters, dimes, nickels, pennies)
