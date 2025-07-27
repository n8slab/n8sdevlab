class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        pathStack = []

        for str in path.split('/'):
            if str in ('', '.'):
                continue
            if str == '..':
                if pathStack:
                    pathStack.pop()
            else:
                pathStack.append(str)
        
        return '/' + '/'.join(pathStack)