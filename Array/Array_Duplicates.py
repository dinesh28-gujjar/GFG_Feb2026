# Given an array arr[] of size n, containing elements from the range 1 to n, and each element appears at most twice, 
# return an array of all the integers that appears twice.
# Note: You can return the elements in any order but the driver code will print them in sorted order.


class Solution:
    def findDuplicates(self, arr):
        n = len(arr)
        counts = {}
        result = []
        
        for num in arr:
            counts[num] = counts.get(num, 0) + 1
            if counts[num] == 2:
                result.append(num)
                
        return result
