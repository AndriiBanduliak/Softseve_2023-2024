import math


def extract_coordinates(s, point):
    # Find the coordinates for the given point in the string
    index = s.find(point)
    x = int(s[index + len(point):s.find(':', index)])
    y = int(s[s.find(':', index) + 1:s.find('#', index + len(point))]
            ) if '#' in s[s.find(':', index):] else int(s[s.find(':', index) + 1:])
    return (x, y)


def distance(p1, p2):
    # Calculate the Euclidean distance between two points
    return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)


def figure_perimetr(s):
    # Extract coordinates for each point
    lb = extract_coordinates(s, 'LB')
    rb = extract_coordinates(s, 'RB')
    lt = extract_coordinates(s, 'LT')
    rt = extract_coordinates(s, 'RT')

    # Calculate the perimeter as the sum of distances between adjacent points
    perimeter = (distance(lb, rb) + distance(rb, rt) +
                 distance(rt, lt) + distance(lt, lb))

    return perimeter
