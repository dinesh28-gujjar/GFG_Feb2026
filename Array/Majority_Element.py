# Given an array arr[]. Find the majority element in the array. If no majority element exists, return -1.
# Note: A majority element in an array is an element that appears strictly more than arr.size()/2 times in the array.



class Solution:
    def majorityElement(self, arr):
        n = len(arr)
        candidate = None
        count = 0
        
        # Phase 1: Candidate dhoondna
        for num in arr:
            if count == 0:
                candidate = num
                count = 1
            elif num == candidate:
                count += 1
            else:
                count -= 1
        
        # Phase 2: Candidate ko verify karna
        actual_count = 0
        for num in arr:
            if num == candidate:
                actual_count += 1
        
        if actual_count > n // 2:
            return candidate
        else:
            return -1
