class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        length = len(s)
        result = ''
        max_len = 0
        for i, ch in enumerate(s):
            right = length
            while right > i:
                res = s[i:right]
                if len(res) < max_len:
                    break
                if res == res[::-1] and max_len < len(res):
                    result = res
                    max_len = len(result)
                right -= 1
        return result


if __name__ == '__main__':
    sol = Solution()
    print(sol.longestPalindrome('assadubbbud'))
