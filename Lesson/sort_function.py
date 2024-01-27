"""
sort() method   = used with lists
sort() function = used with iterables
"""

# students = ("Squidward", 'Sandy', 'Patrick', 'Spongebob', 'Mr. Krabs')
# # students.sort()
# # print(students)
# sorted_students = sorted(students, reverse=True)


# for i in sorted_students:
#     print(i)

# Define a tuple of students, where each student is represented by a tuple containing name, grade, and age.
students = (
    ("Squidward", "F", 60),
    ("Sandy", "A", 33),
    ("Patrick", "D", 36),
    ("Spongebob", "B", 20),
    ("Mr. Krabs", "C", 78)
)

# Define a lambda function 'age' that extracts the age (the third element) from each student tuple.
age = lambda student: student[2]

# Use the sorted() function to sort the 'students' tuple based on the 'age' key in ascending order.
sorted_students = sorted(students, key=age)

# Iterate through the sorted list of students and print each student's information.
for student in sorted_students:
    print(student)
