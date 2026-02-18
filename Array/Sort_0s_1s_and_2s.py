# Given an array arr[] containing only 0s, 1s, and 2s. Sort the array in ascending order.
# Note: You need to solve this problem without utilizing the built-in sort function.


class Solution:
    def sort012(self, arr):
        low = 0
        mid = 0
        high = len(arr) - 1
        
        while mid <= high:
            if arr[mid] == 0:
                # 0 ko low position par bhejo
                arr[low], arr[mid] = arr[mid], arr[low]
                low += 1
                mid += 1
            elif arr[mid] == 1:
                # 1 apni sahi jagah (beech mein) hi hai
                mid += 1
            else: # arr[mid] == 2
                # 2 ko high position par bhejo
                arr[mid], arr[high] = arr[high], arr[mid]
                high -= 1
        
        return arr
