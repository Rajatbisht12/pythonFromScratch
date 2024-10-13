# The dictonary is mutable and unodrerd

info = {
  "name": "Rajat",
  "age": 22,
  "eligible": True,
  "marks":7
}
new_dict = {"name" : "Rajat Bisht"}
info.update(new_dict)


# ---------------------------------Set-----------------------------------------------

# set is unordered collection of data items
# elements are unique and immutable

# set is enclosed in {}

collection = {1,2,3,4,5,6,7,8,9,10}
collec = {1,1,2,3,3,4}
empty_Set  = set()

# ---------------------------------Set Methods---------------------------------------

empty_Set.add(1)
empty_Set.add(2)
empty_Set.remove(1)
empty_Set.add((1,2,3))

# empty_Set.add([4,5,6])
# List values are mutable which leads to the change in the hash value while the time of 
# insertion in the list which leads inconsistency in the hash value
# empty_Set.clear()
# empty_Set.pop()

# set.union(set2)
# set.intersection(set2)