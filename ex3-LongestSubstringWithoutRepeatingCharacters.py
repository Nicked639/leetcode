# Given a string, find the length of the longest substring without repeating characters.

# Examples:

# Given "abcabcbb", the answer is "abc", which the length is 3.

# Given "bbbbb", the answer is "b", with the length of 1.

# Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = []
        midres = []
        length = []
        lens = len(s)
        flag = 0
        i = 0
        
        while i < lens:
            if s[i] in midres:
                result.append(midres)
                midres = midres[(midres.index(s[i])+1):len(midres)]
                #midres = []
                midres.append(s[i])
                flag = 1
            else: 
                midres.append(s[i])
                flag = 0
            i += 1
        if flag == 0:
            result.append(midres)
        if result == []:
            return 0
        else:
            for i in result:
                length.append(len(i))
            length.sort()
            return length[len(length)-1]