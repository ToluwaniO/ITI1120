#Family name: Ogunsanya Toluwani Damilola
# Student number:  8677256
# Course: IT1 1120 
# Assignment Number 4 Question ap4
def getHorizontal(array, row):
    n = len(array[row])
    seq = []
    b = 0
    i = 0

    
    if n > 4:
        
        while i < n-4:
            
            a = array[row][i]
            d = array[row][i+1] - a
            seq = [[row, i], [row, i +1]]
            b = i

            x = 3
            i+=1
            print(i)
            for j in range(i+2, i+4):
                if array[row][j] == a + (x - 1)*d:
                    
                    seq.append([row,j])
                x+=1
                

            if len(seq):
                return (seq, b)
            
    elif n == 4:
        a = array[row][0]
        #print(a)
        d = array[row][1] - a
        #print(d)
        seq = [[row, 0], [row, 1]]

        x = 3

        for j in range(2, 4):
            if array[row][j] == a + (x - 1)*d:
               seq.append([row,j])
            x+=1

        if len(seq):
            return (seq, 0)
    

    return (seq, b)

def getVertical(array, col):
    s = 0
    seq = []
    for i in range(len(array)-3):
        a = array[i][col]
        d = array[1][col]-a

        seq = [[0, col],[1,col]] 

        x = 3
        for j in range(i+2, i+4):
            #print(j)
            if array[j][col] == a + (x-1)*d:
                seq.append([j, col])
            s = j

            x+=1

        if(len(seq) ==4):
            return(seq,s)

    return (seq,s)


def getDiagonal(array):
    hor = []
    indexes = []

    i = len(array)
    j = len(array[0])
    y = 0
    seq = []
    
    for k in range(j-1):
        x = 0
        y = k
        seq = []
        ff = []
        while y < j and x < i:
            ff.append([x,y])
            #print(x,y)
            seq.append(array[x][y])

            
            x += 1
            y += 1
        hor.append(seq)
        indexes.append(ff)



    i = len(array)
    j = 0
    h = 0
    seq = []


    for m in range(i-1, 0, -1):
        x = m
        j += 1
        y = 0
        seq = []
        ff = []
        while y < j:
            ff.append([x,y])
            seq.append(array[x][y])
            x+=1
            y += 1
        hor.append(seq)
        indexes.append(ff)


        h += 1


    ##########################################

    i = len(array)
    j = len(array[0])
    y = 0
    seq = []
    h = i-1
    
    for k in range(j-1, -1, -1):
        x = 0
        y = k
        
        seq = []
        ff = []
        while x <= h:
            ff.append([x,y])
            seq.append(array[x][y])

            x+=1
            y -= 1
        hor.append(seq)
        indexes.append(ff)

        h-=1


    i = len(array)
    j = len(array[0])
    
    
    seq = []


    h = j-1
    for m in range(i-1,0,-1):
        a = m
        y = j-1
        x = m

        ff = []        
        
        seq = []
        while x <= i - 1:
            ff.append([x,y])
            seq.append(array[x][y])

            x+=1
            if(y >h):
                y -= 1
        hor.append(seq)
        indexes.append(ff)


        h -= 1

    #print(hor)
    return (hor, indexes)
        
                       

    

def ap4(two_D):

    v = True
    diagonals = getDiagonal(two_D)[0]
    indexes = getDiagonal(two_D)[1]

    if v:
        for i in range(len(diagonals)):
            array = getHorizontal(diagonals, i)[0]
            

            if (len(array) == 4):            
                print(indexes[i])
                v = False

    if v:
        for i in range(len(two_D)):
            array = getHorizontal(two_D, i)[0]
            

            if (len(array) == 4):
                c = getHorizontal(two_D, i)[1]
                l = [[i, c], [i+1, c+1], [i+2, c+2], [i+3, c+3]]
                print(l)
                v = False


    if v:
        for i in range(len(two_D[0])):
            array = getVertical(two_D, i)[0]

            if(len(array) == 4):
                c = getVertical(two_D, i)[1]
                l = [[i, c], [i+1, c+1], [i+2, c+2], [i+3, c+3]]
                print(l)
                v = False
                           

            
        
    
