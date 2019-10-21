'''
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.

Example 1:

Input: "III"
Output: 3
Example 2:

Input: "IV"
Output: 4
'''
class Solution():
    def __init__(self):
        pass
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        prev = 0
        val = 0
        for i in s:
            if i == 'I':
                val = val + 1
                prev = 1
            elif i == 'V':
                if prev != 1:
                    val = val + 5
                else:
                    val = val + 5 - (2 * prev)
                prev = 5
            elif i == 'X':
                if prev != 1:
                    val = val + 10
                else:
                    val = val + 10 - (2 * prev)
                prev = 10
            
            elif i == 'L':
                if prev != 10:
                    val = val + 50
                else:
                    val = val + 50 - (2 * prev)
                prev = 50
            elif i == 'C':
                if prev != 10:
                    val = val + 100 
                else:
                    val = val + 100 - (2 * prev)
                prev = 100
            elif i == 'D':
                if prev != 100:
                    val = val + 500 
                else:
                    val = val + 500 - (2 * prev)
                prev = 500
            elif i == 'M':
                if prev != 100:
                    val = val + 1000 
                else:
                    val = val + 1000 - (2 * prev)
                prev = 1000
        
        return val


        