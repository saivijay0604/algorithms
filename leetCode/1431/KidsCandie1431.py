class Solution(object):
    def __init__(self):
        pass

    def KidsWithCandies(self, candies, extraCandies):
        list = []
        for i in range(len(candies)):
            numAdd = 0
            numAdd = candies[i] + extraCandies
            if (max(candies) > numAdd):
                list.append(False)
            else:
                list.append(True)
        return list


