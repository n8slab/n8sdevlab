class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxLen = 0
        charSet = set()
        n = len(s)
        l=0

        for r in range(n):
            while s[r] in charSet:
                charSet.remove(s[l])
                l+=1
            maxLen = max(maxLen, r-l+1)
            charSet.add(s[r])
        
        return maxLen