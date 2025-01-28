from datetime import datetime

#function to print date and time
def print_time():
    print('task completed')
    print(datetime.now())
    print()

# print timestamps to see how long sections of code take to run

first_name = 'Susan'
print_time()

for x in range(0,10):
    print(x)
    print_time()
