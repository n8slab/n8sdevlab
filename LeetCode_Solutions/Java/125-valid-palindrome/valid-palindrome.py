class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        #initial case to skip extra calculations for duds
        if s == " " or s=="":
            return True
        
        # Convert string to alphanumeric only
        # start with placeholders for comparison
        ogstr = ""
        revstr = ""
        for x in s:
            if x.isalpha() or x.isnumeric():
                ogstr += x
                revstr = x + revstr
        return ogstr.lower()==revstr.lower()

