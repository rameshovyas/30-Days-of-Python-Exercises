# Given sets
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

# Join A and B
C = A.union(B)
print(C)

# Find A intersection B
C = A.intersection(B)
print(C)

# Is A subset of B
print("Is A subset of B : ", A.issubset(B))

# Are A and B disjoint sets
print("Are A and B disjoint sets : ", A.isdisjoint(B))

# Join A with B and B with A
C = A.union(B)
D = B.union(A)
print("A U B" , C)
print("B U A", D)

# What is the symmetric difference between A and B
C = A.symmetric_difference(B)
print("Symmetric difference between A and B", C)

# Delete the sets completely
del A
del B
