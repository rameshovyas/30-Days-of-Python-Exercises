# Write a function called calculate_slope which return the slope of a linear equation
# slope using two pint formula : m = (y2-y1)/(x2-x1)

def calculate_slope(p1 : tuple, p2 : tuple):
    slope = (p2[1]-p1[1])/(p2[0]-p1[0])
    return slope

p1 =(12,3)
p2 = (4,5)

print("Slope : ", calculate_slope(p1,p2))