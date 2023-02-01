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
                

            


    def mode(self):
        print("mode")
    def std(self):
        print("std")
    def var(self):
        print("var")
    def freq_dist(self):
        print("freq_dist")
        
        
ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]

stat = Statistics(ages)

print(stat.median())

