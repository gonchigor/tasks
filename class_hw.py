import math
from copy import copy


class Point:
    def __init__(self, x, y, name = ""):
        self.x = x
        self.y = y
        self.name = name

    def shiftX(self,x_s):
        self.x += x_s

    def shiftY(self,y_s):
        self.y += y_s

    def shiftXY(self, x_s, y_s):
        self.shiftX(x_s)
        self.shiftY(y_s)

    def coordinate(self):
        return "(" + str(self.x) + "," + str(self.y) + ")"

    def __repr__(self):
        return "Point(" + str(self.x) + ", " + str(self.y) + ", \"" + self.name  +"\")"

    def __str__(self):
        return self.name + self.coordinate()

    def __copy__(self):
        return Point(self.x, self.y, self.name)


class Intercept:
    def __init__(self, point1, point2):
        self.point1, self.point2 = copy(point1), copy(point2)

    def length(self):
        return math.sqrt((self.point1.x - self.point2.x) ** 2 + (self.point1.y - self.point2.y) ** 2)

    def shiftX(self,x_s):
        self.point1.shiftX(x_s)
        self.point2.shiftX(x_s)

    def shiftY(self,y_s):
        self.point1.shiftY(y_s)
        self.point2.shiftY(y_s)

    def shiftXY(self,x_s, y_s):
        self.point1.shiftXY(x_s, y_s)
        self.point2.shiftXY(x_s, y_s)

    def angular(self):
        return math.degrees(math.atan2(self.point2.y - self.point1.y, self.point2.x - self.point1.x))

    def __repr__(self):
        return "Intercept(" + repr(self.point1) + ", " + repr(self.point2) +")"

    def __str__(self):
        return self.point1.name + self.point2.name + "[" + self.point1.coordinate() + "," + \
               self.point2.coordinate() + "]"


if __name__ == "__main__":
    p1 = Point(0,0,"A")
    print("Первая точка:",p1)
    print("Ее представление:", repr(p1))
    p2 = Point(2,1,"B")
    print("Вторая точка:",p2)
    intercept = Intercept(p1, p2)
    print("Отрезок:", intercept)
    print("Длина отрезка:", intercept.length())
    print("Угол отрезка(к оси X):", intercept.angular())
    p2.shiftXY(5, 9)
    print("Вторая точка перемещена:", p2)
    print("При этом отрезок не изменился:", intercept)
    intercept.shiftXY(7, 8)
    print("Сдвинули отрезок", intercept)
    print("Точки остались на месте:", p1, p2)
    print("Представление нового отрезка:", repr(intercept))
