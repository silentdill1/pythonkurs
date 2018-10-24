class Rectangle(object):
    """Rectangle object defined by opposite """
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.a = x2 - x1
        self.b = y2 - y1

    def area(self):
        return self.a*self.b

    def circumference(self):
        return 2*self.a+2*self.b

    def check_inner(self, x, y):
        is_inner_point = True
        if x < self.x1 or x > self.x2:
            is_inner_point = False
        if y < self.y1 or y > self.y2:
            is_inner_point = False
        return is_inner_point

    def intersects(self, rectangle):
        if self.check_inner(rectangle.x1, rectangle.y1):
            return True
        elif self.check_inner(rectangle.x1, rectangle.y2):
            return True
        elif self.check_inner(rectangle.x2, rectangle.y1):
            return True
        elif self.check_inner(rectangle.x2, rectangle.y2):
            return True
        else:
            return False
