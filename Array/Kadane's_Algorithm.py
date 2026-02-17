# You are given an integer array arr[]. You need to find the maximum sum of a subarray (containing at least one element) in the array arr[].
# Note : A subarray is a continuous part of an array.


class Solution:
    def maxSubarraySum(self, arr): # 'A' ko 'a' kar diya
        max_so_far = arr[0]
        current_max = arr[0]
        
        for i in range(1, len(arr)):
            current_max = max(arr[i], current_max + arr[i])
            max_so_far = max(max_so_far, current_max)
            
        return max_so_far
