'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.
'''
class Solution(object):
    def __init__(self):
        pass
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str

        Input: ["flower","flow","floight"]
        Output: "fl"
        """
        if len(strs)==0:
            return ""
        s = strs[0]
        for i in strs:
            if i == "":
                return ""
            if len(i) > len(s):
                s = i
        
        co = 0
        for i in range(0, len(strs)):
            co = 0
            for j in strs[i]:
                if co == len(s):
                    break
                if j == s[co]:
                    co += 1
                    if co == len(strs[i]):
                        s = strs[i]
                        break
                else:
                    s = s[:co]
                    break
            
            
        return s




