s1={1,2,3,4,5,6,7,8,9}
s2={5,6,7,8,9,10,11,12}


print(s1.union(s2))
print(s1.intersection(s2))
print(s1.difference(s2))#it will print the values which are in s1 but not in s2
print(s2.difference(s1))#it will print the values which are in s2 but not in s1
print(s1.issubset(s2))#it will check if s1 is subset of s2 or not
print(s2.issubset(s1))#it will check if s2 is subset of s1 or not

        