import math

class Dimentions(object):
    def __init__(self, size, center_x, center_y):
        self.size = size
        self.x = center_x
        self.y = center_y
        self.half = size/2.0
        self.radius = (2*(size/2.0)**2)**0.5
        self.offset = size/2.0 - self.radius * (1 - math.cos(math.pi/4))  # distance between center and edge of circle
 
    def top_left(self):
        x = self.x - self.half
        y = self.y - self.half
        return x, y

    def top_right(self):
        x = self.x + self.half
        y = self.y - self.half
        return x, y

    def bottom_right(self):
        x = self.x + self.half
        y = self.y + self.half
        return x, y

    def bottom_left(self):
        x = self.x - self.half
        y = self.y + self.half
        return x, y

def degrees(angle):
    return angle*180/math.pi

def calculate_arc(start_angle, end_angle, center_x, center_y, radius, num_points):
    points = []
    angle = start_angle
    diff = (end_angle - start_angle)/(num_points-1)
    for i in range(num_points):
        x = radius*math.cos(angle)
        y = radius*math.sin(angle)
        x += center_x
        y += center_y
        points.append(x)
        points.append(y)
        angle += diff
    return points

def top_arc(dimentions):
    radius = dimentions.radius
    start = math.pi/4
    end = math.pi*3/4.0
    x = dimentions.x 
    y = dimentions.y - dimentions.size
    return calculate_arc(start, end, x, y, radius, 20)

def bottom_arc(dimentions):
    radius = dimentions.radius
    start = math.pi*5/4.0
    end = math.pi*7/4.0
    x = dimentions.x 
    y = dimentions.y + dimentions.size
    return calculate_arc(start, end, x, y, radius, 20)

def left_arc(dimentions):
    radius = dimentions.radius
    start = math.pi*7/4.0
    end = math.pi*9/4.0
    x = dimentions.x - dimentions.size
    y = dimentions.y
    return calculate_arc(start, end, x, y, radius, 20)

def right_arc(dimentions):
    radius = dimentions.radius
    start = math.pi*3/4.0
    end = math.pi*5/4.0
    x = dimentions.x + dimentions.size
    y = dimentions.y
    return calculate_arc(start, end, x, y, radius, 10)

def vertical_center(dimentions):
    start_x = dimentions.x 
    start_y = dimentions.y + dimentions.offset
    end_x = dimentions.x
    end_y = dimentions.y - dimentions.offset
    return start_x, start_y, end_x, end_y

def horizontal_center(dimentions):
    start_x = dimentions.x + dimentions.offset
    start_y = dimentions.y 
    end_x = dimentions.x - dimentions.offset
    end_y = dimentions.y 
    return start_x, start_y, end_x, end_y

def top_right_angle(dimentions):
    start_x = dimentions.x - dimentions.offset
    start_y = dimentions.y 
    end_x = dimentions.x + dimentions.half
    end_y = dimentions.y - dimentions.half
    return start_x, start_y, end_x, end_y

def top_left_angle(dimentions):
    start_x = dimentions.x + dimentions.offset
    start_y = dimentions.y 
    end_x = dimentions.x - dimentions.half
    end_y = dimentions.y - dimentions.half
    return start_x, start_y, end_x, end_y

def bottom_left_angle(dimentions):
    start_x = dimentions.x + dimentions.offset
    start_y = dimentions.y 
    end_x = dimentions.x - dimentions.half
    end_y = dimentions.y + dimentions.half
    return start_x, start_y, end_x, end_y

def bottom_right_angle(dimentions):
    start_x = dimentions.x - dimentions.offset
    start_y = dimentions.y 
    end_x = dimentions.x + dimentions.half
    end_y = dimentions.y + dimentions.half
    return start_x, start_y, end_x, end_y

def up_diagonal(dimentions):
    start_x = dimentions.x - dimentions.half
    start_y = dimentions.y + dimentions.half
    end_x = dimentions.x + dimentions.half
    end_y = dimentions.y - dimentions.half
    return start_x, start_y, end_x, end_y

def down_diagonal(dimentions):
    start_x = dimentions.x - dimentions.half
    start_y = dimentions.y - dimentions.half
    end_x = dimentions.x + dimentions.half
    end_y = dimentions.y + dimentions.half
    return start_x, start_y, end_x, end_y

def notch(dimentions):
    start_x = dimentions.x
    start_y = dimentions.y
    end_x = dimentions.x + dimentions.half
    end_y = dimentions.y + dimentions.half
    return start_x, start_y, end_x, end_y

def long_vertical(dimentions):
    start_x = dimentions.x
    start_y = dimentions.y - dimentions.offset
    end_x = dimentions.x
    end_y = dimentions.y + dimentions.half
    return start_x, start_y, end_x, end_y

def high_bottom_right(dimentions):
    start_x = dimentions.x
    start_y = dimentions.y - dimentions.offset
    end_x = dimentions.x + dimentions.half
    end_y = dimentions.y + dimentions.half
    return start_x, start_y, end_x, end_y

def high_bottom_left(dimentions):
    start_x = dimentions.x
    start_y = dimentions.y - dimentions.offset
    end_x = dimentions.x - dimentions.half
    end_y = dimentions.y + dimentions.half
    return start_x, start_y, end_x, end_y