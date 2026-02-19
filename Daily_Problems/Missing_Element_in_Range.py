# Given an array arr[] of distinct integers and a range [low, high], find all the numbers within the range that are not present in the array.
# return the missing numbers in sorted order.



class Solution:
    def missingRange(self, arr, low, high):
        present = set(arr)
        result = []

        for num in range(low, high + 1):
            if num not in present:
                result.append(num)

        return result
