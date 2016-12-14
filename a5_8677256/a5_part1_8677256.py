#Family name: Ogunsanya Toluwani Damilola
# Student number:  8677256
# Course: IT1 1120
# Assignment Number 5 Part 1
def largest_34(a):
    '''(list of integers) -> integers
    returns the 3rd and 4th largest numbers in the list'''
    l = sorted(a)
    return l[-4] + l[-3]

def largest_third(a):
    '''(list of integers) -> integers
        returns the len(a)//3 largest numbers in the list'''
    l = sorted(a)
    return sum(l[-(len(a)//3):len(l)])

def third_at_least(a):
    '''(list of integers) -> bool
        returns true if a number occurs at least thrice'''
    l = sorted(a)

    for i in range(len(l)-3):
        if l[i] == l[i+2]:
            return l[i]

def sum_tri(a,x):
    '''(list of integers) -> bool
        returns true if 3 elements in the list add up to x'''

    for i in range(len(a)):
        y = x-a[i]
        for j in range(len(a)-1):
            if a[j] + a[j+1] == y:
                return True
            elif a[j] + a[j] == y:
                return True

    return False




