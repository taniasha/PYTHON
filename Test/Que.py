# Question: Create a dictionary where key = student name and value = tuple (marks1, marks2, marks3).

student = {
    "alice": (80,90,70),
    "bob": (70,75,80),
    "char":(98,90,98)
}
average = {name:sum(marks)/len(marks) for name,marks in student.items()}
print(average)