#Family name: Ogunsanya Toluwani Damilola
# Student number:  8677256
# Course: IT1 1120
# Assignment Number 5 Part 2
class Point:
    'class that represents a point in the plane'

    def __init__(self, xcoord=0, ycoord=0):
        ''' (Point,number, number) -> None
        initialize point coordinates to (xcoord, ycoord)'''
        self.x = xcoord
        self.y = ycoord

    def setx(self, xcoord):
        ''' (Point,number)->None
        Sets x coordinate of point to xcoord'''
        self.x = xcoord

    def sety(self, ycoord):
        ''' (Point,number)->None
        Sets y coordinate of point to ycoord'''
        self.y = ycoord

    def get(self):
        '''(Point)->tuple
        Returns a tuple with x and y coordinates of the point'''
        return (self.x, self.y)

    def move(self, dx, dy):
        '''(Point,number,number)->None
        changes the x and y coordinates by dx and dy'''
        self.x += dx
        self.y += dy

    def __eq__(self, other):
        '''(Point,Point)->bool
        Returns True if self and other have the same coordinates'''
        return self.x == other.x and self.y == other.y
    def __repr__(self):
        '''(Point)->str
        Returns canonical string representation Point(x, y)'''
        return 'Point('+str(self.x)+','+str(self.y)+')'
    def __str__(self):
        '''(Point)->str
        Returns nice string representation Point(x, y).
        In this case we chose the same representation as in __repr__'''
        return 'Point('+str(self.x)+','+str(self.y)+')'


class Rectangle(Point):

    def __init__(self, pointA, pointB, color):

        self.pointA = pointA
        self.pointB = pointB
        self.color = color

    def get_bottom_left(self):
        '''()-> object
            returns point object with bottom-left coordinates'''
        return self.pointA

    def get_top_right(self):
        '''()-> object
            returns point object with top-right coordinates'''
        return self.pointB

    def get_color(self):
        '''()-> String
            returns color of the rectangle'''
        return self.color

    def reset_color(self, color):
        '''(string)-> None
           changes color of the rectangle'''
        self.color = color

    def get_perimeter(self):
        '''() -> integer
        returns perimeter of the rectangle'''
        return 2*((self.pointB.get()[0] - self.pointA.get()[0]) + (self.pointB.get()[1] - self.pointA.get()[1]))

    def get_area(self):
        '''()-> integer
           returns area of the rectangle'''
        return (self.pointB.get()[0] - self.pointA.get()[0]) * (self.pointB.get()[1] - self.pointA.get()[1])

    def __repr__(self):
        '''()-> string
           returns a representation of the Rectangle object'''
        return 'Rectangle(' + self.pointA.__repr__() + ', ' + self.pointB.__repr__() + ', "' + self.color + '")'

    def __eq__(self, other):
        '''(other) -> bool
           returns True if two rectangle objects intersects, false otherwise'''
        if self.pointA == other.pointA and self.pointB == other.pointB and self.color == other.color:
            return True
        else:
            return False

    def move(self, dx, dy):
        '''(number, number) -> None
           changes the coordinates the points'''
        self.pointA.move(dx, dy)
        self.pointB.move(dx, dy)

    def intersects(self, other):
        '''(object) -> bool
            returns true if two rectangle objects intersect, false otherwise'''

        x1s = self.pointA.get()[0]
        x2s = self.pointB.get()[0]

        y1s = self.pointA.get()[1]
        y2s = self.pointB.get()[1]

        x1o = other.pointA.get()[0]
        x2o = other.pointB.get()[0]

        y1o = other.pointA.get()[1]
        y2o = other.pointB.get()[1]

        x = None

        if (x1s<=x1o<=x2s and y1s<=y1o<=y2s) or (x1o<=x1s<=x2o and y1o<=y1s<=y2o):
            x= True
        elif (x1s<=x2o<=x2s and y1s<=y2o<=y2s) or (x1o<=x2s<=x2o and y1o<=y2s<=y2o):
            x= True
        elif (x1o<=x1s<=x2o and y1o<=y1s<=y2o) or (x1o<=x1s<=x2o and y1o<=y1s<=y2o):
            x= True
        elif (x1o<=x2s<=x2o and y1o<=y2s<=y2o) or (x1o<=x2s<=x2o and y1o<=y2s<=y2o):
            x= True
        elif(y1s<=y1o<=y2s or y1s<=y2o<=y2s) and (x1o<=x1s<=x1o or x1o<=x1s<=x2o):
            x = True
        elif (y1o <= y1s <= y2o or y1o <= y2s <= y2o) and (x1s <= x1o <= x1s or x1s <= x1o <= x2s):
            x = True
        else:
            x= False
        print(x)

    def contains(self, x,y):
        '''(number, number) -> bool
            returns true if the rectangle contains a point with x,y co-ordinates. False otherwise'''
        if (x >= self.pointA.get()[0] and x <= self.pointB.get()[0]) and (y >= self.pointA.get()[1] and y <= self.pointB.get()[1]):
            return True
        else:
            return False

class Canvas:

    def __init__(self):
        self.rectangles = []

    def add_one_rectangle(self, rect):
        '''(object) -> None
           adds rectangle to the canvas object'''
        self.rectangles.append(rect)

    def total_perimeter(self):
        '''()->number
           returns total perimeter of all rectangles'''
        perimeter = 0

        for i in self.rectangles:
            perimeter += i.get_perimeter()

        return perimeter

    def min_enclosing_rectangle(self):
        '''()->object
           returns the rectangle object for the minimum ecnloing rectangle'''
        min_x = self.rectangles[0].get_bottom_left().get()[0]
        min_y = self.rectangles[0].get_bottom_left().get()[1]

        max_x = self.rectangles[0].get_top_right().get()[0]
        max_y = self.rectangles[0].get_top_right().get()[1]

        for i in self.rectangles:
            j = i.get_bottom_left().get()

            if j[0] < min_x:
                min_x = j[0]

            if j[1] < min_y:
                min_y = j[1]

            j = i.get_top_right().get()

            if j[0] > max_x:
                max_x = j[0]

            if j[1] > max_y:
                max_y = j[1]

        return Rectangle(Point(min_x, min_y), Point(max_x, max_y), "red")

    def common_point(self):
        '''()->bool
           returns true if all rectangles have a common point, false otherwise'''
        for i in range(len(self.rectangles)-1):
            rect = self.rectangles[i]

            for j in range(i+1, len(self.rectangles)):
                if(rect.intersects(self.rectangles[j]) == False):
                    return False

        return True

    def __repr__(self):
        '''() -> String
           returns string representation of the canvas object'''
        return 'Canvas(' + str(self.rectangles) + ')'

    def __len__(self):
        '''()->integer
           returns integer value of the length of the list of rectangles in the canvas object'''
        return len(self.rectangles)

