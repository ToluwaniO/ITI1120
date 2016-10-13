#Family name: Ogunsanya Toluwani Damilola
# Student number:  8677256
# Course: IT1 1120 
# Assignment Number 1

import turtle 

########################
# Question 1
########################
def  lbs2kg(w):
    kg = w/2.2046226218

    return kg


########################
# Question 2
########################
def id_formater(fn, ln, appelation, city, year):
    details = appelation + ". " + ln + ", " + fn + " (" + city + ", " + str(year) + ")"
    return details


########################
# Question 3
########################
def limerick_maker():
    name = input('Enter your fullname --> ')
    city = input('Enter cirth city --> ')
    limerick = name + " the boy who lives in the crane\nsays " + city + " city is his domain\nAlthough I used to think he's \\from Spain\nI was wrong\nNow I have to sing him a song"
    print(limerick)

########################
# Question 4
########################
def id_formater_display():
    appelation = input('ENTER APPELATION --> ')
    fn = input('ENTER FIRST NAME --> ')
    ln = input('ENTER LAST NAME --> ')
    city = input('ENTER BIRTH CITY --> ')
    year = input('ENTER BIRTH YEAR --> ')

    details = id_formater(fn, ln, appelation, city, year)
    print(details)


    
########################
# Question 5
########################
def l2loz(w):
    if w < 0:
        print('NUMBER MUST BE GREATER THAN OR EQUAL TO 0')

    else:
        return (int(w), (w-int(w))*16)

########################
# Question 6
########################
def draw_soccer_field():
    w = turtle.Screen()
    w.bgcolor('green')

    a = turtle.Turtle()

    a.speed(10)
    a.pensize(7)

    a.penup()
    
    a.goto(-600,-300)
    a.pendown()
    a.pencolor('white')
    for i in range(0,2):
        a.forward(1200)
        a.left(90)
        a.forward(600)
        a.left(90)

    a.forward(20)
    a.left(90)
    a.circle(20,90)
    
    a.penup()
    a.goto(-600,-300)
    a.right(180)
    a.goto(-600,300)
    a.pendown()

    a.forward(20)
    a.right(-90)
    a.circle(20,-90)

    a.penup()
    a.goto(600,-300)
    a.right(180)
    a.pendown()

    a.forward(20)
    a.right(-90)
    a.circle(20,-90)

    a.penup()
    a.goto(600,300)
    #a.right(180)
    a.pendown()

    a.forward(20)
    a.right(-90)
    a.circle(20,90)

    a.penup()
    a.goto(0,-300)
    a.left(90)
    a.pendown()
    a.forward(600)

    a.penup()
    a.goto(0,-100)
    a.right(90)
    a.pendown()
    a.circle(100,360)

    a.penup()
    a.goto(0,-10)
    #a.right(90)
    a.pendown()
    a.circle(10,360)

    a.penup()
    a.goto(-600,-150)
    a.pendown()

    a.forward(150)
    a.left(90)
    a.forward(300)
    a.left(90)
    a.forward(150)
    a.left(90)
    a.forward(50)
    a.left(90)
    a.forward(100)
    a.right(90)
    a.forward(200)
    a.right(90)
    a.forward(100)

    a.penup()
    a.goto(-450,-50)
    a.right(180)
    a.pendown()
    a.circle(50,180)

    a.penup()
    a.goto(600,-150)
    a.pendown()

    a.forward(150)
    a.right(90)
    a.forward(300)
    a.right(90)
    a.forward(150)
    a.right(90)
    a.forward(50)
    a.right(90)
    a.forward(100)
    a.left(90)
    a.forward(200)
    a.left(90)
    a.forward(100)

    a.penup()
    a.goto(450,-50)
    a.left(0)
    a.pendown()
    a.circle(50,-180)

    
    
    a.penup()
    a.goto(-480,0)
    a.pensize(15)
    a.pendown()
    a.circle(2)

    a.penup()
    a.goto(480,0)
    a.pensize(15)
    a.pendown()
    a.circle(2)

    w.exitonclick()
    

########################
# Question 7
########################
def median3(num1, num2, num3):
    print(num1, "is a median. This is", (num1>=num2 and num1<=num3) or (num1<=num2 and num1>=num3))
    print(num2, "is a median. This is", (num2>=num1 and num2<=num3) or (num2<=num1 and num2>=num3))
    print(num3, "is a median. This is", (num3>=num1 and num3<=num2) or (num3<=num1 and num3>=num2))

########################
# Question 8
########################
def below_parabola(a,b,p,q):
    return (((a*(p**2)) + b) == q)

########################
# Question 9
########################
def projected_grade(a1,A1,a2,A2,m,M):
    assn1 = (a1/A1)*100
    assn2 = (a2/A2)*100
    assn3 = (assn1 + assn2)/2

    midterm = (m/M)*100

    fExam = midterm

    finalGrade = ((assn1/100)*5) + ((assn2/100)*5) + ((assn3/100)*5) +((midterm/100)*35) + ((fExam/100)*50)

    return finalGrade

########################
# Question 10
########################
def projected_grade_v2():
    a1 = float(input('Enter mark for assignment 1 --> '))
    A1 = float(input('Enter mark obtainable for assignment 1 --> '))
    a2 = float(input('Enter mark for assignment 2 --> '))
    A2 = float(input('Enter mark obtainable for assignment 2 --> '))
    m = float(input('Enter mark for midterm --> '))
    M = float(input('Enter mark obtainable for midterm --> '))

    fExam = (m/M)*100

    if(fExam > 50):
        print(projected_grade(a1,A1,a2,A2,m,M), '%')
    else:
        if(projected_grade(a1,A1,a2,A2,m,M) < fExam):
            print('Your final grade is', projected_grade(a1,A1,a2,A2,m,M), '%')
        else:
            print('Your final grade is', fExam, '%')
    

########################
# Question 11
########################   
def change_to_coins(amount):
    decimal = round(amount*100)
    quarters = decimal // 25
    x = quarters * 25
    dimes = (decimal - x) // 10
    x = x + dimes*10
    nickels = (decimal - x) // 5
    x = x + nickels*5
    pennies = (decimal - x)

    return (quarters, dimes, nickels, pennies)
    

