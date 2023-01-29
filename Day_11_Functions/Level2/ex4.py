# Write different functions which take lists. 
# They should calculate_mean, calculate_median, calculate_mode, calculate_range, 
# calculate_variance, calculate_std (standard deviation).

# Mean
def calculate_mean(nums):
   
    if(len(nums)>0):       
        mean = sum(nums) / len(nums)
    else: mean = None         

    return mean    

# Mode
from collections import Counter
def calculate_mode(data):
    c = Counter(data)
    return [k for k, v in c.items() if v == c.most_common(1)[0][1]]


# Median 
def calculate_median(data):
    n = len(data)
    idx = n // 2

    if(n % 2 != 0 ): # Even number samples
        return sorted(data)[idx]
    return sum(sorted(data)[idx - 1:idx + 1]) / 2

data = [4, 8, 6, 5, 3, 2, 8, 9, 2, 5]

print("Mean : ", calculate_mean(data))      

print("Mode : " , calculate_mode(data))

print("Median : ", calculate_median(data) )