from collections import Counter
items = ["apple", "banana", "apple", "orange", "banana", "apple"]
frequency = {}
count_items = Counter(items)
print(count_items)

for item in items:
    frequency[item] = frequency.get(item, 0) + 1

print(frequency)

