# Flatten the following list of lists of lists to a one dimensional list :
list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
one_dimensional = [x for lst in list_of_lists for l in lst for x in l]
print(one_dimensional)