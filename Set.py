# collection = {1,2,3,4,"Subhashis"}
# print(collection)
# print(type(collection))
collection = set()
collection.add(1)
collection.add(2)
collection.add("Subhashis")
collection.add((1,2,3))

collection.remove(1) # remove any item
print(collection)