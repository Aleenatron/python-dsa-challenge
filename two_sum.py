# Two Sum question
"""
Input : nums = [3,4,5,6], target = 7
Output: [0,1]

"""
"""
Step 1:
Restate the problem:
------------------------
"We are given an array of integers nums and a target integer. Our goal is to find two indices i and j such that nums[i] + nums[j] == target and return [i, j]. The indices should be distinct."
Ask clarifying questions: \
"Can I assume there is always exactly one valid pair?" \
"Should I return an empty list if no solution exists?" \
"Can numbers be negative?" \
"Are numbers unique, or can duplicates exist?" \
"Do I need to return indices in sorted order?" \

"""
"""
Step 2: Write Test cases
-------------------------
Test Cases

|   Case Type        |       Input        | Expected Ouput |
--------------------------------------------------------------
|   Basic Case      | [2, 7, 11, 15], 9   | [0,1]          |
|   Negative Nos    | [-1, -2, -3], -5    | [1,2]          |
|   Duplicates      |  [3, 3], 6          | [0, 1]         |
|   No solution     |  [1, 2, 3], 10      | []             |

"""

"""
Step 3: Identify Patterns
--------------------------
Brute force approach: Try every pair (i, j) → O(n²).
Sorting + Two Pointers: Sort array and use i, j → O(n log n).
Hashmap for O(1) lookups: Use dictionary to track seen numbers → O(n).
Optimal Choice? → Hashmap (O(n)) is best.

"""

"""
Step 4: Pseudocode 
---------------------

Brute Force O(n^2)
Loop through nums with index i:
    Loop through nums again with index j>1:
    if nums[i] + nums[j] == target
        return [i, j]
return []


Optimized Hashmap
------------------
Create empty dictionary hashmap
Loop through nums with index i:
    Compute diff = target - nums[i]
    If diff exists in hashmap:
        Return [hashmap[diff], i]  # Found solution
    Store nums[i] in hashmap with value i
Return []

"""


def sort_twopointers(nums, target):
    A = []
    
    for i, num in enumerate(nums):  # Step 1: Store values & indices
        A.append([num, i])

    A.sort()  # Step 2: Sort based on values

    i, j = 0, len(nums) - 1  # Step 3: Initialize two pointers

    while i < j:  # Step 4: Search for target
        cur = A[i][0] + A[j][0]  # Calculate sum
        
        if cur == target:  # Step 5: If sum matches target
            return [min(A[i][1], A[j][1]), max(A[i][1], A[j][1])]
        
        elif cur < target:  # Step 6: If sum too small, move left
            i += 1  
        
        else:  # Step 7: If sum too large, move right
            j -= 1  
    
    return []  # Step 8: Return empty list if no solution

        # TC: O(nlogn) SC O(n)
        # Two pointers only work on sorted array

    # Method 2 : Opimized soln

def twosum_hashing(inputs):
    hashmap = {}  # Step 1: Initialize dictionary

    for i, num in enumerate(inputs):  # Step 2: Loop through elements
        diff = target - num  # Step 3: Compute the complement

        if diff in hashmap:  # Step 4: If complement exists, return indices
            return [hashmap[diff], i]

        hashmap[num] = i  # Step 5: Store value in hashmap

    return []  # Step 6: If no pair is found, return empty list

