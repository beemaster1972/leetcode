class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums = self.merge_sorted_arrays(nums1, nums2)
        length = len(nums)
        if length % 2:
            return nums[length // 2]
        else:
            return (nums[length // 2 - 1] + nums[length // 2]) / 2

    def merge_sorted_arrays(self, n1, n2):
        if n1 and n2 and n1[-1] < n2[0]:
            return n1 + n2
        elif not n1:
            return n2
        elif not n2:
            return n1
        nums = []
        length = len(n1) + len(n2)
        point_1, point_2 = 0, 0
        while len(nums) < length:
            if n1[point_1] < n2[point_2]:
                nums.append(n1[point_1])
                point_1 += 1 if point_1 < len(n1) else 0
            else:
                nums.append(n2[point_2])
                point_2 += 1 if point_1 < len(n1) else 0
            if point_1 == len(n1):
                nums.extend(n2[point_2:])
                break
            if point_2 == len(n2):
                nums.extend(n1[point_1:])
                break
        return nums


if __name__ == '__main__':
    sol = Solution()
    print(sol.findMedianSortedArrays([1, 2], []))
