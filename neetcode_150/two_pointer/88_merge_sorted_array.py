from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1 = m - 1
        p2 = len(nums2) - 1
        i = len(nums1) - 1

        while p2 >= 0 and p1 >= 0:
            if nums2[p2] >= nums1[p1]:
                nums1[i] = nums2[p2]
                p2 -= 1
            else:
                nums1[i], nums1[p1] = nums1[p1], nums1[i]
                p1 -= 1
            i -= 1

        while i >= 0 and p2 >= 0:
            nums1[i] = nums2[p2]
            i -= 1
            p2 -= 1


