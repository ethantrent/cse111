# List
empty_list = []
courses = ['Math', 'Algebra', 'History', 'Spanish']
print(courses)
print(len(courses))
print(courses[0]) # beginning
print(courses[-1]) # end

courses.append("Programming") # append to end
print(courses)
courses[0] = "Physical Education" # replace value at index
print(courses)

courses.insert(1, "Physics") # insert at specific index
print(courses)

courses.remove("History") # remove from specific index
print(courses)
courses.pop() # remove last value
print(courses)

courses.reverse() # reversed
print(courses)

courses.sort() # sorts
print(courses)

print(courses.index("Spanish")) # find index with argument

for course in courses:
    print(course)

for index, course in enumerate(courses): # access index and value
    print(index, course)

course_str = ', '.join(courses) # turn list into strings with comma
print(course_str)
new_list = course_str.split(', ') # convert strings to list based on comma
print(new_list)

# Tuples - immutable
empty_tuple = ()
tuple1 = ("Ethan", "Jake", "Chris", "Bob")

# Sets - unordered and don't contain duplicates
empty_set = set()
cs_courses = {'Frontend', 'Backend', 'Moblie', 'Cloud'}
print(cs_courses)
cs_courses.add('Frontend') # will not add due to duplicate



