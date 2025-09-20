car = {
    "Model" : "Ford",
    "Year" : 2019
}

print(car.keys())
print(car.values())

print("name of model :", car["Model"])


# make dict from 2 tuples
tuple1 = ('bba', 'bca','btech')
tuple2 = (45, 56, 67)
thisdict = dict.fromkeys(tuple1, tuple2)
print(thisdict)