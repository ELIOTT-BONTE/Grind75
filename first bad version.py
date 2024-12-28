# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l, r = 1, n
        m = 1
        while l < r:
            m = (l + r) // 2
            print(m)
            if isBadVersion(m) :
                print("shift L")
                r = m
            else :
                print("shift R")
                l = m+1
        return l
