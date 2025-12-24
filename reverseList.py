inputList = [10,20,30,40]

def reverseList(inputList):
  output=[]
  listSize = (len(inputList) - 1)
  for i in range(len(inputList)):
    output.append(inputList[listSize-i])
  return output

print("Original List:", inputList)
print("Reverse List:",reverseList(inputList))

inputList = [1, 2, 2, 3, 1, 4]
def countItemFrequency(inputList):
  frequency = {}
  for i in inputList:
    frequency[i] = frequency.get(i,0) + 1
  return frequency
print("CountOfItems:",countItemFrequency(inputList))

inputList = [2,1, 2, 3,4]
def findMinMax(inputList):
  minItem = maxItem = inputList[0]
  for i in inputList:
    if i > maxItem:
      maxItem = i
    elif i < minItem:
      minItem = i
  return (minItem,maxItem)

print(findMinMax(inputList))
    