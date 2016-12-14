#Family name: Ogunsanya Toluwani Damilola
# Student number:  8677256
# Course: IT1 1120 
# Assignment Number 3 Question 1
def count_pos(u):
    '''
    (list of numbers) -> number

    returns the number of positive values in the list

    preconditions: u must be a list of numbers 
    '''
    x = []

    for i in u:
        if i > 0:
            x.append(i)

    return len(x)


#main
a = input('Enter a list of numbers separated by comas: ')
a = a.strip()

l = list(eval(a))

count = count_pos(l)

print('There are', count, 'positive numbers in your list')
