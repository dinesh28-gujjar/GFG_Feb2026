# Given an array arr[] containing integers and an integer k, your task is to find the length of the longest subarray where the sum of its elements is equal to the given value k. 
# If there is no subarray with sum equal to k, return 0.



class Solution:
    def longestSubarray(self, arr, k):
        # Hash map to store (prefix_sum: first_occurrence_index)
        sum_map = {}
        current_sum = 0
        max_length = 0
        
        for i in range(len(arr)):
            current_sum += arr[i]
            
            # Case 1: Agar shuruat se hi sum k ke barabar mil jaye
            if current_sum == k:
                max_length = i + 1
            
            # Case 2: Agar (current_sum - k) map mein maujood hai
            # Matlab beech ka portion sum k de raha hai
            rem = current_sum - k
            if rem in sum_map:
                length = i - sum_map[rem]
                max_length = max(max_length, length)
            
            # Agar current_sum pehle nahi dekha gaya, toh hi store karein
            # Taaki pehle wala (leftmost) index barkarar rahe
            if current_sum not in sum_map:
                sum_map[current_sum] = i
                
        return max_length
