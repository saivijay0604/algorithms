def search(list,searchNum):
    lower = 0
    upper = len(list)-1
    for i in list:
        if lower <= upper:
            midValue = (lower + upper)//2
            if list[midValue] == searchNum:
                globals() ['position'] = midValue
                return True
            else:
                if list[midValue] < searchNum:
                    lower = midValue+1
                else:
                    upper = midValue-1
def arrayList():
    numOfList = int(input("Number of element in the list: "))
    listArray = []
    print("Elements in list: ")
    for i in range(numOfList):
        elementsInList = int(input())
        listArray.append(elementsInList)
    listArray.sort()
    print(listArray)
    searchElement = int(input("Enter the search element: "))
    if search(listArray, searchElement):
        print("Element Found at {} position" .format(position+1))
    else:
        print("Element not found")
position = -1
arrayList()
