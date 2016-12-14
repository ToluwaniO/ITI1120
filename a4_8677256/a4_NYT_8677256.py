#Family name: Ogunsanya Toluwani Damilola
# Student number:  8677256
# Course: IT1 1120 
# Assignment Number 4 Question NYT
def validateInteger(question, number):
    '''(int,int)->int
    returns valid user input as an integer'''
    report = 'PLEASE ENTER ' + str(number) + ' INTEGER VALUES. '
    value = None
    times = 0

    if number == 4:
        while value == None:
            try:
                value = int(input(question))

                if value < 1000 or value > 9999:
                    value = None

            except:
                print(report)


    elif number == 0:
        while value == None:
            try:
                value = int(input(question))

                if value < 1:
                    value = None


            except:
                print(report)
                


    elif number == 2:
        
        while value == None  :
            try:
                value = int(input(question))
                
                if value < 1 or value > 12:
                    value = None
                    
                     

                

            except ValueError:
                value = None
                print(report)        

    return value

def print_book(book):
    '''(2D-LIst)->None
    prints book in special format'''
    date = book[3].split('/')
    day = date[1]
    month = date[0]
    year = date[2]
    
    date_string = day + '-' + month + '-' + year
    
    print(book[0] + ', ' + book[1] + " (" + date_string + ")")
    
def read_from_file():
    '''()->2D-list
    Reads data from txt file and returns as list'''
    x = open('NYT-bestsellers.txt', 'r').read().splitlines()
    
    y = []

    for i in x:
        y.append(i.split('\t'))

    return y

def year_range(books):
    '''(2D-List)->None
    finds best sellers in a particular year'''
    begin = str(validateInteger('ENTER STARTING YEAR: ', 4))
    end = str(validateInteger('ENTER ENDING YEAR: ', 4))

    for i in books:
        year = i[3].split('/')[2]

        if year >= begin and year <= end:
            print_book(i)

def month_year_range(books):
    '''(2D-list)->None
    finds book withing a specific month in a year'''
    month = str(validateInteger('ENTER MONTH (Integer between 1-12): ', 2))
    year = str(validateInteger('ENTER YEAR: ', 4))

    time = month + "/" + year
    #print(time)

    for i in books:
        current_time = i[3].split('/')[0] + "/" + i[3].split('/')[2]
        #print(current_time)

        if current_time == time:
            print_book(i)

def find_author(books):
    '''(2D-List)->None
    finds an author in bestsellers list'''
    author = input('Enter search text: ').lower()
    c=0

    for i in books:
        if author in i[1].lower():
            print_book(i)
            c+=1

    if c == 0:
        print('NO AUTHOR FOUND!')

def find_title(books):
    '''(2D-List)->None
    finds a book title in bestsellers list'''
    title = input('Enter search term: ').lower()
    c=0

    for i in books:
        if title in i[0].lower():
            print_book(i)
            c+=1

    if c == 0:
        print("NO BOOK FOUND!")
            

def find_bestseller_ranking(books):
    '''(2D-List)->None
    finds authors with at least n bestsellers'''
    rank = validateInteger("ENTER NUMBER OF BESTSELLERS: ", 0)
    
    authors = []
    scores = []

    for i in frequency(books):
        if i[1] >= rank:
            print(i[0], 'with', i[1], 'bestsellers')

def y_bestsellers(books):
    '''(2D-List)->None
    finds top n authors'''
    rank = validateInteger('ENTER Y value: ', 0)

    authors = []
    scores = []

    for i in frequency(books):
        authors.append(i[0])
        scores.append(i[1])

    for i in range(rank):
        index = scores.index(max(scores))
        print(authors[index] + ": " + str(scores[index]))
        scores[index] = 0

def frequency(books):
    '''(2D-List)->2D-List
    returns 2D-List of authors and frequency of occurence'''
    authors_scores = []

    for i in books:
        if [i[1].strip(),0] not in  authors_scores:
            authors_scores.append([i[1].strip(), 0])

    for i in range(len(authors_scores)):
        for j in books:
            if authors_scores[i][0] == j[1].strip():
                authors_scores[i][1]+=1

    return authors_scores
        


def end_program():
    '''()->None
    end program'''
    print('GOOD-BYE!')
        
            

def print_options():
    '''()->None
    display options'''
    print(30*'=')
    print('What would you like to do? Enter 1, 2, 3, 4, 5, 6 or Q for answer.')
    print('1: Look up year range')
    print('2: Look up month/year')
    print('3: Search for author')
    print('4: Search for title')
    print('5: Numbers of authors with at least x bestsellers')
    print('6: List y authors with the most bestsellers')
    print('Q: Quit')
    print(30*'=')

    #choice = input('Answer (1, 2, 3, 4, 5, 6, Q or q): ')

def function_caller(choice, books):
    '''(str,2D-List)->None
    calls functions'''
    if choice == '1':
        year_range(books)
    elif choice == '2':
        month_year_range(books)
    elif choice == '3':
        find_author(books)
    elif choice == '4':
        find_title(books)
    elif choice == '5':
        find_bestseller_ranking(books)
    elif choice == '6':
        y_bestsellers(books)
    elif choice == 'Q' or choice == 'q':
        end_program()
    

#main
books = read_from_file()
cont = True

frequency(books)

while cont:
    print_options()
    choice = input('Answer (1, 2, 3, 4, 5, 6, Q or q): ').strip()
    if choice.lower() != 'q':
        function_caller(choice, books)
        print(3*'\n')
    else:
        end_program()
        cont = False
