def valid_triangle(sides):
    return sides[0]+sides[1] >= sides[2] and sides[0]+sides[2] >= sides[1] and sides[2]+sides[1] >= sides[0]
    
def equilateral(sides):
    if sides[0] == sides[1] == sides[2] > 0 and valid_triangle(sides):
        return True
    return False

def isosceles(sides):
    if (sides[0] == sides[1] or sides[1] == sides[2] or sides[0] == sides[2]) and valid_triangle(sides):
        return True
    return False


def scalene(sides):
    if sides[0] != sides[1] != sides[2] != sides[0] and valid_triangle(sides):
        return True
    return False
