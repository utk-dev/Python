##dictionary is a collection of key-value pairs.Dictonary is mutable.

#for eg:- we have to store marks of some students out of 30 with their names, so we can save it as dictionary
marks = {"lavanya":24,
         "Rohit":12,
         "Rajat":19,
         "Vaishnavi":30}
print(marks)  #will print a dictionary of names(keys) with their marks(values)

## METHODS OF DICTIONARY

# 1. .items()-returns a list of (key,value) tuples
print(marks.items())


# 2. .keys()-will print a list of key values only(same applies for values(.values()))
print(marks.keys())


# 3. .update()-update the dictionary with the supplied key-values pairs
marks.update({"Rohit":11})
print(marks)

# 4. .get(key/value)-returns the value of the specified key
print(marks.get("Rajat"))

