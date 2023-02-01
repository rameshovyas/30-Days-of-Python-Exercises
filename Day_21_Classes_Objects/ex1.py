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
        print("mean")
    def median(self):
        print("median")
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

print(stat.range())

