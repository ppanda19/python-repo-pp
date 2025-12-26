def checkPalindrome(str):
  inputStr = list(str)
  i=0
  j=(len(inputStr)-1)

  for i in range(len(inputStr)):
    if inputStr[i] != inputStr[j]:
      return False
    j -= 1
  return True
print("Check Palindrom:",checkPalindrome("madam"))
print("Check Palindrom:",checkPalindrome("hari"))
print("Check Palindrom:",checkPalindrome("madaM"))

inputList = [2,7,11,15]
target = 9

def findSumIndicies(inputList,target):
  i=0
  
  for i in range(len(inputList)):
    j=1
    while ((len(inputList)-1) >= j):
      # print(f"i:{i} & Value->",inputList[i])
      # print(f"j:{j} & Value->",inputList[j])
      if (target== (inputList[i] + inputList[j])):
        return (i,j)
      j +=1
      # print("j:",j)

print(f"Sum OF Indicies:{inputList} ->",findSumIndicies(inputList,target))
inputList = [1,3,4,5]
print(f"Sum OF Indicies::{inputList} ->",findSumIndicies(inputList,target))

def findRepeatingChar(inputList):
  strList = list(inputList)
  i=0
  
  for i in range(len(inputList)):
    j=i+1
    while (len(inputList)-1 >= j):
      if strList[i] == strList[j]:
        return strList[i]
      j += 1
  
  
inputList="swis"
print("RUNNING FILE:", __file__)
print("Reapting")
print(f"First repeating Char in : {inputList}",findRepeatingChar(inputList))