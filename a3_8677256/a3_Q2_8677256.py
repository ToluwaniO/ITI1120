#Family name: Ogunsanya Toluwani Damilola
# Student number:  8677256
# Course: IT1 1120 
# Assignment Number 3 Question 2
def two_length_run(l):
    '''
        (list of numbers) -> bool

        returns True if an element appears two or more times consecutively
        and false if not
    '''
    for i in range(len(l)-1):
        if(l[i] == l[i+1]):
            return True

    return False

#main
l = input('Please input a list of numbers separated by commas: ')
li = list(eval(l))

print(two_length_run(li))
