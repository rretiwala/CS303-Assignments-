import math

class Point(object):

    #Primary Constructor
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    #get distance
    def dist(self, other):
        return math.hypot(self.x - other.x, self.y - other.y)

    #string of point
    def __str__(self):
        return '(' + str(self.x) + ", " + str(self.y) + ")"

    #test equality
    def __eq__(self, other):
        tol = 1.0e-16
        return ((abs (self.x - other.x) < tol) and (abs(self.y - other.y) < tol))

class Circle(object):
    #constructor
    def __init__(self, x = 0, y = 0, radius = 1):
        self.radius = radius
        self.center = Point(x,y)

    #circumference
    def circumference(self):
        return 2.0*math.pi*self.radius

    #compute
    def area(self):
        return math.pi*(self.radius*self.radius)

    #determine if point is inside of radius
    def point_inside(self, p):
        return (self.center.dist(p) < self.radius)

    #determine if circle is inside another
    def circle_inside(self, c):
        distance = self.center.dist(c.center)
        return (distance + c.radius) < self.radius

    #edge overlap, intersection only
    def does_interest(self, c):
        distance = self.center.dist(c.center)
        return (distance - c.radius) < self.radius


    def circle_circumscribes(self, r):
        radius = math.sqrt(r.width()*r.width() + r.length()*r.length())
        radius = radius / 2
        center_x = (r.lr.x + r.ul.x) / 2
        center_y = (r.ul.y + r.lr.y) / 2
        circum_circle = Circle(center_x, center_y, radius)
        return circum_circle

    #prints center and radius of circle
    def __str__(self):
        return "Center:"+ str(self.center) +", Radius: " + str(self.radius)

    # test for equality of radius
    def __eq__(self, other):
        return self.radius == other.radius

class Rectangle(object):

    #initiate
    def __init__(self, ul_x = 0, ul_y = 1, lr_x = 1, lr_y = 0):
        #checks if input is possible, otherwise it'll give it a default
        if ((ul_x < lr_x) and (ul_y > lr_y)):
            self.ul = Point(ul_x, ul_y)
            self.lr = Point(lr_x, lr_y)
        else:
            self.ul = Point(0, 1)
            self.lr = Point(1, 0)

    #length of rectangle
    def length(self):
        return self.lr.x - self.ul.x

    #width of rectangle
    def width(self):
        return self.ul.y - self.lr.y

    #Determine the perimeter
    def perimeter(self):
        return 2*self.width() + 2*self.length()

    def area(self):
        return self.width()*self.length()

    #returns true if point is inside of rectangle
    def point_inside(self, p):
        return ((p.x > self.ul.x) and (p.x < self.lr.x) and (p.y > self.lr.y) and (p.y < self.lr.x))

    #checks if a rectangle is inside of the main rectangle
    def rectangle_inside(self, r):
        return ((r.ul.x > self.ul.x) and (r.ul.x < self.lr.x) and (r.lr.y < self.ul.y) and (r.lr.y > self.lr.y))


    #determine if two rectangles overlap
    def does_intersect(self, other):
        self_ll = Point(self.ul.x, self.lr.y)
        self_ur = Point(self.lr.x, self.ul.y)

        other_ll = Point(other.ul.x, other.lr.y)
        other_ur = Point(other.lr.x, other.ul.y)


        if self.rectangle_inside(other):
            return True
        elif other.rectangle_inside(self):
            return  True
        elif self.point_inside(other.ul):
            return True
        elif self.point_inside(other.lr):
            return True
        elif self.point_inside(other_ll):
            return True
        elif self.point_inside(other_ur):
            return True
        elif other.point_inside(self.ul):
            return True
        elif other.point_inside(self.lr):
            return True
        elif other.point_inside(self_ll):
            return True
        elif other.point_inside(self_ur):
            return True
        else:
            return False

    #smallest rectangle that can circumscribe a circle
    def rect_circumscribe(self, other):
        radius = other.radius
        center_x = other.center.x
        center_y = other.center.y

        lower_right_x = center_x + radius
        lower_right_y = center_y - radius
        upper_left_x = center_x - radius
        upper_left_y = center_y + radius

        return Rectangle(upper_left_x, upper_left_y, lower_right_x, lower_right_y)

    #string rep of a rectangle
    def __str__(self):
        return str(self.ul) + "," + str(self.lr)

    #determine two rectangles have the same length and width
    def __eq__(self, other):
        return (other.length() == self.length()) and (other.width() == self.width())



def main():
    inputs = []
    infile = open("geom.txt", "r")

    random_circle = Circle()
    random_rectangle = Rectangle()

    for line in infile:
        line = line.strip()
        line = line.split()
        inputs.append(line)

    for i in range(2):
        inputs[i] = inputs[i][0:2]

    for i in range(2,4):
        inputs[i] = inputs[i][0:3]

    for i in range(4,6):
        inputs[i] = inputs[i][0:4]

    for i in range(len(inputs)):
        for k in range(len(inputs[i])):
            inputs[i][k] = float(inputs[i][k])

    p = Point(inputs[0][0], inputs[0][1])
    q = Point(inputs[1][0], inputs[1][1])

    circle_c = Circle(inputs[2][0], inputs[2][1], inputs[2][2])
    circle_d = Circle(inputs[3][0], inputs[3][1], inputs[3][2])

    rectangle_g = Rectangle(inputs[4][0], inputs[4][1], inputs[4][2], inputs[4][3])
    rectangle_h = Rectangle(inputs[5][0], inputs[5][1], inputs[5][2], inputs[5][3])

    # print the coordinates of the points P and Q

    print ("Coordinates of P:", p)
    print ("Coordinates of Q:", q)

    # find the distance between the points P and Q
    print ('Distance between P and Q:', p.dist(q))

    # print C and D
    print ('Circle C:', circle_c)
    print ('Circle D:', circle_d)

    # compute the circumference of C
    print ('Circumference of C:', circle_c.circumference())

    # compute the area of D
    print ('Area of D:', circle_d.area())
    # determine if P is strictly inside C
    if circle_c.point_inside(p):
        print ('P is inside C')
    else:
        print ('P is not inside C')

    # determine if C is strictly inside D
    if circle_d.circle_inside(circle_c):
        print ('C is inside D')
    else:
        print ('C is not inside D')

    # determine if C and D intersect (non zero area of intersection)
    if circle_d.does_interest(circle_c):
        print ('C does intersect D')
    else:
        print ('C does not intersect D')
    # determine if C and D are equal (have the same radius)
    if circle_d == circle_c:
        print ('C is equal to D')
    else:
        print ('C is not equal to D')

    # print the two rectangles G and H
    print ('Rectangle G:', rectangle_g)
    print ('Rectangle H:', rectangle_h)

    # determine the length of G (distance along x axis)
    print ('Length of G:', rectangle_g.length())
    # determine the width of H (distance along y axis)
    print ('Width of H:', rectangle_h.width())

    # determine the perimeter of G
    print ('Perimeter of G:', rectangle_g.perimeter())
    # determine the area of H
    print ('Area of H:', rectangle_h.area())
    # determine if point P is strictly inside rectangle G
    if rectangle_g.point_inside(p):
        print ("P is inside G")
    else:
        print ('P is not inside G')

    # determine if rectangle G is strictly inside rectangle H
    if rectangle_h.rectangle_inside(rectangle_g):
        print ('G is inside H')
    else:
        print ('G is not inside H')

    # determine if rectangles G and H overlap (non-zero area of overlap)
    if rectangle_g.does_intersect(rectangle_h):
        print ('G does overlaps H')
    else:
        print ('G does not overlap H')

    # find the smallest circle that circumscribes rectangle G
    print ('Circle that circumscribes G:', random_circle.circle_circumscribes(rectangle_g) )

    # goes through the four vertices of the rectangle

    # find the smallest rectangle that circumscribes circle D
    print("Rectangle that circumscribes D:", random_rectangle.rect_circumscribe(circle_d))
    # all four sides of the rectangle are tangents to the circle

    # determine if the two rectangles have the same length and width
    if rectangle_g == rectangle_h:
        print ('G is equal to H')
    else:
        print ('G is not equal to H')

    # close the file geom.txt
    infile.close()

main()