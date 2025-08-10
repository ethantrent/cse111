# for
nums = [1, 2, 3, 4, 5]

for num in nums: # goes through each value
    print(num)

print()

nums2 = [1, 2, '.', 3, 4, 5]
for num in nums2:
    if num == '.':
        continue
    elif num == 4:
        break
    print(num)

print()

for num in nums:
    for letter in 'abc': # nested loop
        print(num, letter)

print ()

for i in range(1, 11): # loop through certain number of times
    print(i)

print ()

# while
x = 0
while x < 10:
    print(x)
    x += 1 # increment until condition

