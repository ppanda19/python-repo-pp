from array import array

arr = array('i',[1, 2, 3, 4, 5])
str_arr = array('u', 'hello')
print("Array elements:",arr)

for i in arr:
    print(f"Element: {i}")

str_arr.append('!')
print("String Array elements:",str_arr)

for i in range(len(str_arr)):
    print(f"Character at index {i}: {str_arr[i]}")

#adding elements to string array 
str_arr.extend(' world')
print("Extended String Array elements:",str_arr)

str_list = ["abc", "def", "ghi"]
print("String Array as list:", str_list)

