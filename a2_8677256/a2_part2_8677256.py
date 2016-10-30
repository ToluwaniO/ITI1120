#Family name: Ogunsanya Toluwani Damilola
# Student number:  8677256
# Course: IT1 1120 
# Assignment Number 2 PART 2

import random

########################
# Question 1
########################
def size_format(b):
    '''
       (number)->string

       gets a byte value and converts to either kilobytes, megabytes or gogabytes
    '''
    if b < 0:
        return 'buy a new hard disk'
    elif b < 1000:
        return str(round(b,1)) + 'B'
    elif b < 1000000:
        return str(b/1000,1) + 'KB'
    elif b < 1000000000:
        return str(round(b/1000000,1)) + 'MB'
    elif b < 1000000000000:
        return str(round(b/1000000000,1)) + 'TB'

########################
# Question 2
########################
def add_article(x):
    '''
        (string)->string
        takes as string as a an argument and returns it with an article added (either le or la or l')
    
    '''
    vowel_exceptions = ['Belize', 'Cambodge', 'Mexique', 'Mozambique', 'Zaire', 'Zimbabwe', 'belize', 'cambodge', 'mexique', 'mozambique', 'zaire', 'zimbabwe']
    plural_exceptions = ['Etats-unis', 'Pay-bas', 'Etats-Unis', 'Pay-Bas', 'etats-unis', 'pay-bas']
    x = x[0] + x.strip(x[0])

    if x in vowel_exceptions:
        return 'le ' + x
    elif x in plural_exceptions:
        return 'les ' + x
    elif x[0] in 'AEIOUaeiou':
        return "l'" + x
    elif x[len(x)-1] in 'Ee':
        return 'la ' + x
    else:
        return 'le ' + x


########################
# Question 3
########################
def factorial(x):
    '''
        (number)-> number
        returns the factorial of the argument
    
    '''
    y = 1
    if x == 1:
         return x

    for i in range(2, x+1):
        y = y * i

    return y


########################
# Question 4
########################
def special_count(x):
    '''
        (list,list)-> bool
        returns the True if the odd elements of each list are equal and vice versa
    
    '''
    y = 0

    for i in x:
        if (i%4) == 0 and i >= 0:
            if (i%100)==0 and (i%400)==0:
                y += 1
            elif (i%100)>0:
                y += 1

    return y


########################
# Question 5
########################
def vote():

    '''
        (None)->None
        prints the result of a voting process gotten from user input
    
    '''
    
    x = input("ENTER VOTES? ")
    x = x.lower().strip()
    votes = x.count('y')
    y = votes + x.count('n') - x.count('ned')

    if (votes / y) == 1:
        print("proposal passes unanimously")
    elif (votes / y) >= 2/3:
        print("proposal passes with super majority")
    elif(votes/y) >= 0.5:
        print("proposal passes with simple majority")
    else:
        print("proposal fails")
                
########################
# Question 6
########################
def stats_v1(c):
    '''
        (number)-> None
        prints the sum and average of a list of random numbers between -100 and 100. It also prints the list of numbers
    
    '''
    num = []

    for i in range (0, c):
        x = random.randrange(-100,100)
        num.append(x)
        print(x, end=" ")

    average = sum(num)/len(num)
    maxN = min(num)

    print('\naverage:', average)
    print('max:', maxN)


def stats_v2(c):
    
    '''
        (number)-> None
        prints the sum and average of a set of random numbers between -100 and 100. It also prints the set of numbers
    
    '''

    sumN = 0
    y = 0

    for i in range(0,c):
        x = random.randrange(-100,100)
        sumN += x
        print(x, end=" ")
    

        if i == 0:
            y = x
        elif x < y:
            y = x

    print('\naverage:', sumN/c)
    print('min:', y)

########################
# Question 7
########################
def emphasize(c):

    '''
        (string)-> string
        returns a string with spaces in between all characters in the argument
    
    '''
    
    text = ""

    if len(c) == 1:
        return c
    else:
        for i in range(0, len(c)):
            if i != len(c)-1:
                text += c[i] + " "
            else:
                text += c[i]
    return text

########################
# Question 8
########################
def crypto(c):
    '''
        (string)-> string
        returns an encrypted version of the argument
    
    '''
    a = 0
    b = len(c)-1

    text = ""

    for i in range(0, len(c)//2):
        text += c[b] + c[a]
        a+=1
        b-=1

    if len(c)%2 != 0:
        text+= c[(len(c)//2)]
    return text


########################
# Question 9
########################
def stranger_things(l1,l2):
    
    '''
        (list, list)-> bool
        compares the elementsand lengths of the two lists
    
    '''

    if len(l1) == len(l2):
        for i in range(0, len(l1)):
            if i%2 == 0:
                if (l1[i]!=l2[i]):
                    return False
            else:
                if (l1[i]==l2[i]):
                    return False
            
    else:
        return False

    return True

