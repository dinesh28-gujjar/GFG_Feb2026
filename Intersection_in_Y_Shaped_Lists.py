# You are given the heads of two non-empty singly linked lists, head1 and head2, that intersect at a certain point. Return that Node where these two linked lists intersect.
# Note: It is guaranteed that the intersected node always exists.
# In the custom input you have to give input for CommonList which pointed at the end of both head1 and head2 to form a Y-shaped linked list.


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    def intersectPoint(self, head1, head2):
        # If either list is empty
        if not head1 or not head2:
            return None

        c1 = head1
        c2 = head2

        # Two-pointer switching technique
        while c1 != c2:
            c1 = c1.next if c1 else head2
            c2 = c2.next if c2 else head1

        # Returns intersection node or None
        return c1
