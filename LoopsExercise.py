#Find Second Largest Number in a List
nums = [12, 35, 1, 10, 34, 40]

first_largest = second_largest = float('-inf')

for num in nums:
    if num > first_largest:
        second_largest = first_largest
        first_largest = num
    elif num > second_largest and num != first_largest:
        second_largest = num

print("The largest number is:", first_largest)
print("The second largest number is:", second_largest)