"""
Top K Frequent Elements
Given an integer array nums and an integer k, return the k most frequent elements within the array.

The test cases are generated such that the answer is always unique.

You may return the output in any order. TC: O(n) SC: O(n)
"""

"""
Test Cases
Input: nums = [1, 2, 2, 3, 3, 3], k =2
Output: [2,3]

Input: nums = [7, 7], k = 1
Output: [7]

Input: nums = [1, 2, 2, 3, 3, 3], k =6
Output: [1, 2, 3]

Input: nums = [2, 2, 3, 3, 4, 4 , 1, 0, 6], k = 1
Output: [2] # follow up question: what if there are 2, 3 ,4 all repeating smae number of times we return 1

"""
"""
Pseudocode
------------
dict{}
Loop through nums store each element and their count in dctionary
sort the dict in descending order of frequency 
out []
run anther loop for k times and store in out the  kth maximum frequency key values
"""
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Count occurrences
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1  # Fix KeyError issue

        # Step 2: Sort by frequency (descending)
        sorted_counts = sorted(count.items(), key=lambda x: x[1], reverse=True)

        # Step 3: Handle edge case when k > unique elements
        k = min(k, len(sorted_counts))

        # Step 4: Extract top k elements
        return [sorted_counts[i][0] for i in range(k)]

# I first count occurrences using a dictionary."
# "Then, I sort it in descending order to get the top k elements."
# "To avoid errors when k is larger than unique elements, I take min(k, len(unique_elements))."
# "If efficiency is a concern, I would use a heap (heapq.nlargest()), which runs in O(n log k).