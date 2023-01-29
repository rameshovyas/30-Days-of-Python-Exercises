# Quadratic equation is calculated as follows: ax² + bx + c = 0. Write a function which calculates 
# solution set of a quadratic equation, solve_quadratic_eqn.
import math
def solve_quadratic_eqn(a,b,c):
    roots = None    
    if(a>0):
        dis = b**2-4*a*c
        if(dis > 0): # There are two real roots
            root1 = (-b+ math.sqrt(dis)) / 2*a
            root2 = (-b- math.sqrt(dis)) / 2*a
            roots = (root1,root2)
        elif (dis == 0):  # Only on real root
            roots = (-b/(2*a))
        else: # Both roots are imaginary
            roots = ("Roots are imaginary")    
    return(roots)

# x2+−8x+5=0
a = 1
b = -8 
c = 5
print("Two real Roots : ", solve_quadratic_eqn(a,b,c))

# 5x2+20x+32=0
a = 5
b = 20 
c = 32
print(solve_quadratic_eqn(a,b,c))
