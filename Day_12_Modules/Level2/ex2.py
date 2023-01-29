# Write a function list_of_rgb_colors which returns any number of RGB colors in an array

import random 
def list_of_rgb_colors():
    r = lambda: random.randint(0,255)
    str = "rgb({},{},{})".format(r(),r(),r())
    return str

print(list_of_rgb_colors())    