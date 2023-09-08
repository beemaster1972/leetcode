class Solution(object):
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        """
        type nums: List[int]
        type target: int
        rtype: List[Int]
        """
        result = []
        nums_dict = {num: i for i, num in enumerate(nums)}
        for i, num in enumerate(nums):
            if (required := nums_dict.get(target - num, None)) is not None and required != i:
                return [i, required]

        return result


if __name__ == '__main__':
    sol = Solution()
    print(sol.twoSum([2, 7, 11, 15], 17))
