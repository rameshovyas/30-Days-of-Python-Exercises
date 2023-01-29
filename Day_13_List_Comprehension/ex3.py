# Using list comprehension create the following list of tuples
lst = [(a,b,a,a**2,a**3,a**4,a**5) 
        for a in range(0,11)
        for b in [1]
      ]

print(lst)
