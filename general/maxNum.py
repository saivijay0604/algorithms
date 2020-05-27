from numpy import *
def maxNumber(x,y):
    if max(x) >= y:
        return False
    return True

arr = array([10,22,113,14,95,6])#array
print("list of numbers: ", arr)
num = 30
print(maxNumber(arr,num))
for i in range(len(arr)):
    newNum = arr[i]+ num
    print("new elements:", newNum)
    print(maxNumber(arr, newNum))



