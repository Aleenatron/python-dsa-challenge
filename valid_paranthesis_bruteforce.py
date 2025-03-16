"""
Input: s = "[(])"
Stack process: 
Push '[' -> Stack: ['[']
Push '(' -> Stack: ['[', '(']
Pop ']' -> expected : ) , we got ]
o/p: false

we return false when it contains unmatched braxkets at the end or if the stack os empty when encountering a closing brace
"""

"""
Pseudocode:
1. Create an empty stack
2. Iterate through each character in the string:
a. If its an opening bracket, push it into the stack.\
b. If it's a closing bracket:
    - if the stack is empty return False becuase unmatched closing bracket.
    - Pop from the stack and check if it matched the closing bracket, if not return False
3. After all iteration, stack is empty means all matching pairs found so return True else retuen False

"""

class Solution:
    def isValid(self, s: str)-> bool:
        stack = []
        for char in s:
            if char in "({[":
                stack.append(char)
            elif char in ")}]":
                if not stack:
                    return False
                k = stack.pop()
                if (k == '(' and char != ')' ) or \
                (k == '{' and char != '}') or \
                (k =='[' and char != ']'):
                    return False
        return len(stack)==0
if __name__ == '__main__':
    solution = Solution()
    test_cases = ['()', '[{]}]', '[{()}}{}[()]]']
    for test in test_cases:
        print(f"{test} is {solution.isValid(test)}")