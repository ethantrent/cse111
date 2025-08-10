# key-value pairs
student = {'name': 'John', 'age': 25, 'courses': ['Programming', 'Math']}
print(student['name']) # access value with key
print(student.get('phone')) # .get returns get instead of error

student['phone'] = '555-5555'
print(student.get('phone'))

student['name'] = 'Ethan' # update value from key
print(student)

age = student.pop('age') # remove age from dict
print(student)
print(age) # saved age w/ variable

print(student.keys()) # returns all keys
print(student.values()) # returns all values
print(student.items()) # returns both key and value

for key, value in student.items():
    print(key, value) # loops through to print key and value