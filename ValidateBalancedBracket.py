# Validate Balanced Brackets
# This script checks if the brackets in a given string are balanced. 
# It supports three types of brackets: (), {}, and [].
def is_balanced(s):
    # Stack to keep track of opening brackets
    stack = []
    
    # Mapping of closing brackets to their corresponding opening brackets
    bracket_map = {')': '(', '}': '{', ']': '['}
    
    # Set of opening brackets for quick lookup
    opening_brackets = set(bracket_map.values())
    
    for char in s:
        if char in opening_brackets:
            # If it's an opening bracket, push it onto the stack
            print("Open Bracket:",char)
            stack.append(char)
        elif char in bracket_map:
            print("Closing Bracket:",char)
            print("Mapping Bracket:",bracket_map[char])
            print("In Stack Before Pop:",stack[-1])
            # If it's a closing bracket, check for matching opening bracket
            if not stack or stack[-1] != bracket_map[char]:
                return False
            stack.pop()  # Pop the matched opening bracket from the stack
            print("In Stack After Pop:",stack)
    
    # If the stack is empty, all brackets were balanced
    return len(stack) == 0

print (is_balanced("([])"))            # True
#print (is_balanced("({[]})"))        # True