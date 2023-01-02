# The following is a list of 10 students ages:

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# Sort the list and find the min and max age
ages.sort()
min = ages[0]
max = ages[len(ages)-1]
print('Min ages = {} and Max age = {}'.format(min,max))

# Add the min age and the max age again to the list
ages.append(min)
ages.append(max)
print(ages)

# Find the median age (one middle item or two middle items divided by two)
ages.sort()
mid = len(ages) // 2
median = (ages[mid] + ages[~mid]) / 2
print('Median = {}'.format(median))

# Find the average age (sum of all items divided by their number )
avg = sum(ages) / len(ages)
print('Average = {}'.format(avg))

# Find the range of the ages (max minus min)
ages.sort()
print('Range = {}'.format(ages[len(ages)-1] - (ages[0])))

