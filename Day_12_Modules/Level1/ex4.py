# Write a function list_of_hexa_colors which returns any number of hexadecimal colors in an array
#  (six hexadecimal numbers written after #. Hexadecimal numeral system is made out of 16 symbols, 
# 0-9 and first 6 letters of the alphabet, a-f
import random 
def list_of_hexa_colors():
    str ="#"
    str = str + "%06x" % random.randint(0, 0xFFFFFF)
    return str

print(list_of_hexa_colors())    