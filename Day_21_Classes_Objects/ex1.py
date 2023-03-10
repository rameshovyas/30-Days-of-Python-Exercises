from collections import Counter
import math

class Statistics:
    #constructor
    def __init__(self, data):
        self.data = data

    def count(self):
        if(self.data):
            return len(self.data)
        return None


    def sum(self):
        if(self.data):
            return sum(self.data)
        return None


    def min(self):
        if(self.data):
            return min(self.data)
        return None    


    def max(self):
        if(self.data):
            return max(self.data)
        return None


    def range(self):
        if(self.data):
            return (self.max() - self.min())
        return None

    def mean(self):
        if(len(self.data)>0):
            return (sum(self.data) / len(self.data))    
        return None

    def median(self):
        if((self.data) and (len(self.data)>0)):
            # First sort data in ascending order
            tmp_data = sorted(self.data)
            n = len(tmp_data)
            
            # For odd number of data
            if(n%2 !=0):
                return (tmp_data[(n+1) // 2])
            
            # For even number of data    
            else:
                a = tmp_data[n // 2]
                b = tmp_data[(n // 2) + 1]
                return ((a+b)/2)              
        return None
            
    def mode(self):
        c = Counter(self.data)
        return[k for k, v in c.items() if v == c.most_common(1)[0][1]]
    
    def var(self):
        mean = sum(self.data) / len(self.data)

        # square each item after subtracting mean from it
        squared = list(map(lambda x: (x-mean)**2, self.data))
        
        return sum(squared) / (len(self.data) - 1)


    def std(self):
        if(self.var()):
            return(math.sqrt(self.var()))
        return None

    def freq_dist(self):
        if(self.data):
            return set([(x, self.data.count(x)) for x in self.data])
        return None    
        
        
ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]

lst = [1, 2, 3, 4, 5]
data = Statistics(ages)
print("************Result*************")
print('Count:', data.count()) # 25
print('Sum: ', data.sum()) # 744
print('Min: ', data.min()) # 24
print('Max: ', data.max()) # 38
print('Range: ', data.range()) # 14
print('Mean: ', data.mean()) # 30
print('Median: ', data.median()) # 29
print('Mode: ', data.mode()) # {'mode': 26, 'count': 5}
print('Standard Deviation: ', data.std()) 
print('Variance: ', data.var()) 
print('Frequency Distribution: ', data.freq_dist())

