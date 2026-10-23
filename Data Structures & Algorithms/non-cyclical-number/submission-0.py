class Solution:
    def isHappy(self, n: int) -> bool:

#given- positive integer, replace with sum of squares
#repeat until number equals 1 or loops
    #stops at 1 == non cyclical, return True

#Structure -> helper function that keeps running until number is exhausted


#outer while loop that runs until helper functon returns 1

        def helper(n):
            total = 0
            while n > 0:
                num = n % 10
                total += num ** 2
                n = n // 10
            return total




        visited = set()
        while n != 1:
            if n in visited:
                return False
            visited.add(n)
            n = helper(n)
        return True


        