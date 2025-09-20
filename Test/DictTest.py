# Question: Create a dictionary (student data – name, age, marks) and perform:
# Access value using key (get)
# Add/update key-value pair (update)
# Delete key-value pair (pop)
# Print all keys and values

student_data = {
    "name" : "Tania",
    "age" : 20,
    "marks" : 99
}

print(student_data.get("name"))

student_data.update({"city": 90})
student_data.update({"marks":99.5})
print(student_data)

student_data.pop("age")
print(student_data)

print("All keys: ",student_data.keys())
print("All values: ",student_data.values())

# ------------------------------------------------------------------------------------------------

# Use dictionary comprehension to create a dictionary where keys = numbers (1–5) and values = their squares

squares = {x: x**2 for x in range (1, 6)}
print("Squares : ",squares)