# You are given an array citations[], where each element citations[i] represents the number of citations received by the ith paper of a researcher. You have to calculate the researcher’s H-index.
# The H-index is defined as the maximum value H, such that the researcher has published at least H papers, and all those papers have citation value greater than or equal to H.



class Solution:
    def hIndex(self, citations):
        n = len(citations)

        # Step 1: Create buckets
        bucket = [0] * (n + 1)

        for c in citations:
            if c >= n:
                bucket[n] += 1
            else:
                bucket[c] += 1

        # Step 2: Traverse from highest possible h
        papers = 0
        for h in range(n, -1, -1):
            papers += bucket[h]
            if papers >= h:
                return h

        return 0
