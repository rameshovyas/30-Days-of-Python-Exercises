# Write a function named rgb_color_gen. It will generate rgb colors (3 values ranging from 0 to 255 each).
import random

def rgb_color_gen():
    r = random.randrange(255)
    g = random.randrange(255)
    b = random.randrange(255)
    str = "rgb({},{},{})".format(r,g,b)
    return(str)


print(rgb_color_gen())
