"""

For a given two rectangles, write a the function that will receive only the bottom-left and the upper right coordinates 
and returns the area of their overlap rectangle  

"""

def overlapAreachallenge(points):
    #putting out rect 1 and 2
    rect1 = points[0]
    rect2 = points[1]

    #Taking the uper and lower coordinates to calculate the area 
    area = (rect1[1][0] - rect2[0][0]) * (rect1[1][1] - rect2[0][1])
    return area





print("Area for the given rectangles = {%}", format(overlapAreachallenge([[[1,1], [5,3]], [[2,2], [8,4]]])))