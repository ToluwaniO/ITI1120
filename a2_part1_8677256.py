#Family name: Ogunsanya Toluwani Damilola
# Student number:  8677256
# Course: IT1 1120 
# Assignment Number 2 PART 1
import random

def perform_test(a, n):
    
    '''
        (number, number)-> None
        asks a set of questions and computes the average
    
    '''

    z = ''
    if a == 0:
        z = '+'
        print('PLEASE ANSWER THE FOLLOWING ADDITION QUESTIONS')
    elif a == 1:
        z = '*'
        print('PLEASE ANSWER THE FOLLOWING MULTIPLICATION QUESTIONS')

    correct = 0

    for i in range(0,n):
        x = random.randint(0,10)
        y = random.randint(0,10)

        ans = int(input('ENTER ' + str(x) + z + str(y) + ': '))

        if a == 1:
            if ans == x*y:
                correct+=1
        elif a == 0:
            if ans == x+y:
                correct+=1

    average = (correct/n) * 100

    print(average)

    if average >= 80:
        print("Well done! Congratulations.")
    elif average >= 60:
        print("Not too bad but please study and practice some more.")
    else:
        print("Please study more and ask your teacher for help.")

print('WELCOME TO ADDITION/MULTIPLICATION TEST\n\n')
number = int(input('ENTER NUMBER OF QUESTIONS YOU WANT TO ANSWER: '))


print('THIS SOFTWARE TESTS YOU WITH', number, 'QUESTIONS...')
print('0) ADDITION \n1) MULTIPLICATION')
choice = int(input('PLEASE MAKE A SELECTION (0 or 1): '))




perform_test(choice,number)
