from KidsCandie1431 import *
t=Solution()

listLength = int(input('Size of elements : '))
userList = list()
for i in range(listLength):
  ele = int(input("Elements in list: "))
  userList.append(ele)

print("user list is ",userList )
num = int(input("Enter number of ExtraCandies :"))

print(t.KidsWithCandies(userList,num))
