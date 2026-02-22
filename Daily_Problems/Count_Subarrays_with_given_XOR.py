# Given an array of integers arr[] and a number k, count the number of subarrays having XOR of their elements as k.
# Note: It is guranteed that the total count will fit within a 32-bit integer.


class Solution:
    def subarrayXor(self, arr, k):
        prefix_xor = 0
        count = 0
        
        # hashmap to store frequency of prefix XORs
        freq = {0: 1}
        
        for num in arr:
            prefix_xor ^= num
            
            # check if required prefix exists
            required = prefix_xor ^ k
            if required in freq:
                count += freq[required]
            
            # update frequency
            freq[prefix_xor] = freq.get(prefix_xor, 0) + 1
        
        return count
