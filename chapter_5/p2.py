s={
    12,'harry'
}
# print(s)

s=set()
s.add(12)
s.add('harry')
s.add("abd")
s.add(12.5)
s.add(12)   # set does not allow duplicates
s.add((1,2,3))  # set allows tuples
# print(s)
S=set()
S.add(12)
S.add('harry')
S.add(12.0)
print(S)
print(len(S))