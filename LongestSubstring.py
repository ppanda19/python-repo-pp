# Find longest substring without repeating characters
def longestSubstring(s: str) -> int:
    seen = set()
    left = 0
    max_length = 0

    for right in range(len(s)):
        # If character already in window, shrink window
        print("Value in Set:",seen)
        print("Window Value:",s[right])
        while s[right] in seen:
            print("left:",left)
            print("Value at left:",s[left])
            seen.remove(s[left])
            left += 1

        # Add current character
        seen.add(s[right])

        # Update max length
        max_length = max(max_length, right - left + 1)

    return max_length

def longestUniqueSubstring(s: str) -> int:
    last_seen = {}
    left = 0
    max_length = 0

    for right, char in enumerate(s):
        print(f"right:{right} & char:{char}")
        if char in last_seen and last_seen[char] >= left:
            left = last_seen[char] + 1

        last_seen[char] = right
        print(f"left-> {left} & last_seen->{last_seen}")
        max_length = max(max_length, right - left + 1)

    return max_length


# Example usage:
input_string = "abcabcbb"
print("Input String:", input_string)
# print("Length of Longest Substring without Repeating Characters:", longestSubstring(input_string))
print("Length of Longest Substring without Repeating Characters:", longestUniqueSubstring(input_string))

input_string = "abcadefb"
print("Input String:", input_string)
print("Length of Longest Substring without Repeating Characters:", longestUniqueSubstring(input_string))


