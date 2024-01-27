"""
tuple = collection which is ordered and unchangable
        used to group together related data
"""

student = ('Bro', 21, 'male')

print(student.count('Bro'))
print(student.index('Bro'))

for x in student:
    print(x)

if 'Bro' in student:
    print('Bro is here!')