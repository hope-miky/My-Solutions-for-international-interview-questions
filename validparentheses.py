'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
'''

class Solution(object):
    def __init__(self):
        self.stack = []
        self.top = -1
    
    def push1(self, val):
        self.top += 1
        self.stack[self.top] = val 
    
    def pop1(self):
        self.top -= 1
    
    def peek1(self):
        if self.stack[self.top] == '{':
            return '}'
        elif self.stack[self.top] == '(':
            return ')'
        else:
            return ']'
        

    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        self.stack = [""] * len(s)

        self.push1(s[0])
        s = s[1:]
        for i in s:
            if i == self.peek1():
                self.pop1()
            else:
                self.push1(i)
                
        return self.top == -1
        


