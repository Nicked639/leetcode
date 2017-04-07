# Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

# Example:

# Input: "babad"

# Output: "bab"

# Note: "aba" is also a valid answer.
# Example:

# Input: "cbbd"

# Output: "bb"

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # 从中心开始往两边找回文（两边相等则是回文，不等则不是回文）
        length = len(s)
        front = 0
        back = 0
        max = 0
        res1 = 0
        res2 = 0
        for i in range(length):
            front = i - 1
            back = i + 1
            while front >= 0 and back < length:
                if s[front] == s[back]:
                    front -= 1
                    back += 1
                else:
                    front +=1
                    back -=1
                    break
            else:
                front += 1
                back -= 1
            if front < back and front >=0 and back < length:
                pass
            else:
                front = i
                back = i
            num = back - front
            if num >= max:
                max = num
                res1 = front
                res2 = back
            if i + 1< length and s[i] == s[i+1]:
                front = i - 1
                back = i + 2
                while front >= 0 and back < length:
                    if s[front] == s[back]:
                        front -= 1
                        back += 1
                    else:
                        front += 1
                        back -= 1
                        break
                else:
                    front +=1
                    back -= 1
                if front < back and front >=0 and back < length:
                    pass
                else:
                    front = i
                    back = i + 1
                num = back - front

                if num >= max:
                    max = num
                    res1 = front
                    res2 = back
        return s[res1:res2+1]
        
ex5 = Solution()
print(ex5.longestPalindrome("babaaa"))