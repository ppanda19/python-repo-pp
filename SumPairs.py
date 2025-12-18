#Find pairs in an array whose sum is equal to a given target value.
nums = [2, 4, 3, 5, 7, 8, 9]
target = 7

seen = set()
pairs = set()

for num in nums:
    complement = target - num
    if complement in seen:
        pairs.add((min(num, complement), max(num, complement)))
    seen.add(num)

print(pairs)