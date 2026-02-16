# Given an array arr[] containing only non-negative integers, your task is to find a continuous subarray (a contiguous sequence of elements) whose sum equals a specified value target. 
# You need to return the 1-based indices of the leftmost and rightmost elements of this subarray. You need to find the first subarray whose sum is equal to the target.
# Note: If no such array is possible then, return [-1].


# User function Template for python3
class Solution:
    def subarraySum(self, arr, target):
        n = len(arr)
        current_sum = 0
        left = 0
        
        for right in range(n):
            # Add the current element to the window
            current_sum += arr[right]
            
            # Shrink the window from the left while current_sum > target
            # Added a check to allow left to equal right for single-element targets
            while current_sum > target and left <= right:
                current_sum -= arr[left]
                left += 1
                
            # Check if we found the target
            if current_sum == target:
                return [left + 1, right + 1]
                
        return [-1]
