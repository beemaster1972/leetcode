class Solution:
    def countBits(self, n: int) -> list[int]:
        ans = [self.convert_to_bin(i).count(1)  for i in range(n + 1)]
        return ans

    def bits_count(self,n: int)->list[int]:
        ans = [0] * (n + 1)
        for i in range(1,n + 1):
            ans[i] = ans[i >> 1] + (i & 1)
        return ans
    def convert_to_bin(self, n: int) -> list[int]:
        ans = [0]
        while n:
            ans.append(n%2)
            n //=2
        return ans


if __name__ == '__main__':
    sol = Solution()
    print(sol.bits_count(10))
