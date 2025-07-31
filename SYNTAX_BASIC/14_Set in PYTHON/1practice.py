

setA = set()

setA.add(1)
setA.add(2)
setA.add(1)

setA.discard(1)
print(setA)

setA.update({1, 23, 3})
print(setA)

print(1 in setA)