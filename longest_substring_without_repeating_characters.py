class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(set(s)) == len(s):
            return len(s)
        res = 0
        left, right = 0, 1
        while right < len(s):
            if s[right] not in s[left:right]:
                right += 1
            else:
                res = max(res, len(s[left:right]))
                left += 1
        res = max(res, len(s[left:right]))
        return res


if __name__ == '__main__':
    sol = Solution()
    print(sol.lengthOfLongestSubstring('abcdefghi'))
