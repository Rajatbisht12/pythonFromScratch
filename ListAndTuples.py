marks = [94.5, 99.5, 98.5, 99.5, 99.5]
# Strings are Immutable List are Mutable
# Tuples are immuatable
# ----------------------------------Slicing-----------------------------------------
student = marks[1:]

# ----------------------------------Methods-----------------------------------------
marks.append(56)
# marks.sort()
# marks.sort(reverse=True)
marks.insert(2, 56)

# ----------------------------------Tuples-------------------------------------------

tup = (87, 98, 99, 100, 101, 87)
# tup[0] = 33  --> Not allowed
ind =tup.index(87)
count = tup.count(87)
