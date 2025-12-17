nums = [1, 2, 4, 5, 6]

def FindMissingNumber(nums):
    n = len(nums) + 1  # Since one number is missing
    total_sum = n * (n + 1) // 2  # Sum of first n natural numbers
    actual_sum = sum(nums)  # Sum of numbers in the list
    missing_number = total_sum - actual_sum  # The missing number
    return missing_number

print("Missing Number:", FindMissingNumber(nums))