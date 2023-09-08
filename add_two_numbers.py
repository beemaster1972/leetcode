class Solution:

    @staticmethod
    def list_to_integer(lst: list[int]) -> int:
        result = 0
        for i, num in enumerate(lst):
            result += num * 10 ** i
        return result

    @staticmethod
    def integer_to_list(num: int) -> list[int]:
        result = []
        while num:
            result.append(num % 10)
            num //= 10
        return result

    def addTwoNumbers(self, l1: list[int], l2: list[int]) -> list[int]:
        result = self.list_to_integer(l1) + self.list_to_integer(l2)
        return self.integer_to_list(result)


if __name__ == '__main__':
    sol = Solution()
    print(sol.addTwoNumbers([9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9]))
