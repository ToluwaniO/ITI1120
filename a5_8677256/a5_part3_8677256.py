#Family name: Ogunsanya Toluwani Damilola
# Student number:  8677256
# Course: IT1 1120
# Assignment Number 5 Part 3
def digit_sum(n):
    '''(list of integers) -> integers
        returns the sum of all digits in a given number'''
    if n > 0:

        x = 10*(round(n/10 - n//10,1)) + digit_sum(n//10)
        return int(x)
    return 0

def digital_root(n):
    '''(list of integers) -> integers
        returns the sum of all digits as an integer less than 10'''
    x = n

    if x > 10:
        x = digit_sum(x)

        if x >10:
            x = digital_root(x)

    return x


