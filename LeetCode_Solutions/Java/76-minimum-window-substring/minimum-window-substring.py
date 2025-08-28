class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if (len(s)<len(t) or t==""):
            return ""

        countT, curWin = {}, {}

        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        haveCount = 0
        needCount = len(countT)
        res, resLen = [-1, -1], float("inf")
        l =0
        for r in range(len(s)):
            c = s[r]
            curWin[c] = 1 + curWin.get(c, 0)                    

            if c in countT and (curWin[c] == countT[c]):
                haveCount +=1

            while haveCount == needCount:
                if(r-l+1)< resLen:
                    res = [l, r]
                    resLen = (r - l + 1)
                curWin[s[l]] -= 1
                if s[l] in countT and curWin[s[l]] < countT[s[l]]:
                    haveCount -= 1
                l+=1
        l, r = res
        return s[l:r+1] if resLen != float("inf") else ""