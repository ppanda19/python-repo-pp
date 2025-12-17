print("Using Fo Loops in Python.")
data_list = [10, 20, 30, 40, 50]
dict_data = {'a': 1, 'b': 2, 'c': 3}

for item in data_list:
    print(f"Processing item: {item}")

for key,value in dict_data.items():
    print(f"Key: {key}, Value: {value}")

# Using range() in for loop
for i in range(6):
    print(f"Current index: {i}")

# Nested for loop
for i in range(3):
    for j in range(2):
        print(f"i: {i}, j: {j}")

# Using else with for loop
for item in data_list:
    print(f"Item: {item}")  
else:
    print("Finished processing all items.")

# using While Loops in Python.
print("\nUsing While Loops in Python.")
count=0
while count<5:
    print(f"Count is: {count}")
    count+=1
    

