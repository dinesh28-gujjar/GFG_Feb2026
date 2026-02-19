# Given an integer array arr[ ], your task is to find the minimum number of increment operations required to make all the array elements unique.
# i.e. no value in the array should occur more than once. In one operation, a value can be incremented by 1 only.
# Note: The answer will always fit into a 32-bit integer.



class Solution:
    def minIncrements(self, arr):
        arr.sort()

        moves = 0
        prev = arr[0]

        for i in range(1, len(arr)):
            if arr[i] <= prev:
                needed = prev + 1
                moves += needed - arr[i]
                prev = needed
            else:
                prev = arr[i]

        return moves
