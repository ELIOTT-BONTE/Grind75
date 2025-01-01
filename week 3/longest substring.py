class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # use a set to keep track of encountered chars
        # l, r pointers, l is the current beginning of substring, r is the end of it
        # when r is a char in set, move l until r is not a char in set anymore

        l, r = 0, 0
        enc = set()
        maxi = 0

        while r < len(s):
            if s[r] in enc:
                enc.remove(s[l])
                l += 1
            else :
                enc.add(s[r])
                r += 1
            maxi = max(maxi, r - l)

        return maxi