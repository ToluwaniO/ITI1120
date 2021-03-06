#Family name: Ogunsanya Toluwani Damilola
# Student number:  8677256
# Course: IT1 1120 
# Assignment Number 3 Question 3
def longest_run(l):
    '''
        (list of numbers) -> number
        
        returns the length of the longest run in the list

        preconditions: l must be a list
    '''
    mLen = 0

    for i in range(len(l)-1):
        count = 1
        for j in range(i+1, len(l)):
            if l[i] == l[j]:
                count += 1
            else:
                break

        if count > mLen:
            mLen = count
    return mLen

#main
a = input('Enter a list of numbers separated by comas: ')
a = a.strip()

l = list(eval(a))

print(longest_run(l))

