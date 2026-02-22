# You are given two strings s1 and s2, of equal lengths. The task is to check if s2 is a rotated version of the string s1.
# Note: A string is a rotation of another if it can be formed by moving characters from the start to the end (or vice versa) without rearranging them.


class Solution:
    def areRotations(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False
        
        return s2 in (s1 + s1)
