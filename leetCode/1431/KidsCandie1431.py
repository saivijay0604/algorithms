class Solution(object):
    def __init__(self):
        print('hi')

    def KidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        print("T1")
        list = []
        for i in range(len(candies)):
            numAdd = 0
            numAdd = candies[i] + extraCandies
            if (max(candies) > numAdd):
                list.append(False)
            else:
                list.append(True)
        print("test")
        return list

t=Solution()
print(t.KidsWithCandies([1,4,9],3))


