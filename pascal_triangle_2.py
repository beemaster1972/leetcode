from math import factorial as f


class Solution(object):
    def generate(self, rowIndex: int) -> list[int]:
        """
        type rowIndex: int
        rtype: List[Int]
        """
        result = [int(f(rowIndex)/(f(rowIndex-i)*f(i))) for i in range(rowIndex+1)]

        return result


if __name__ == '__main__':
    sol = Solution()
    print(sol.generate(3))
