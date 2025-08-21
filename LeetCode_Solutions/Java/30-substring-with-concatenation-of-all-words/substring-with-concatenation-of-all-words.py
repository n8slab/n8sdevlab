class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        wlen = len(words[0])
        wslen = len(words) * len(words[0])
        res = []
        
        for pos in range(wlen):
            i = pos
            d = Counter(words)
            
            for j in range(i, len(s) + 1 - wlen, wlen):
                word = s[j: j + wlen]
                d[word] -= 1
                
                while d[word] < 0:
                    d[s[i: i + wlen]] += 1
                    i += wlen
                if i + wslen == j + wlen:
                    res. append(i)
        
        return res


