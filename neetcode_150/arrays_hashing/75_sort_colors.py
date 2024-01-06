class Solution:
    def sortColors(self, nums: List[int]) -> None:
        count = [0, 0, 0]

        for num in nums:
            count[num] += 1

        i = 0
        while i < len(nums):
            while count[0] > 0:
                nums[i] = 0
                count[0] -= 1
                i += 1

            while count[1] > 0:
                nums[i] = 1
                count[1] -= 1
                i += 1

            while count[2] > 0:
                nums[i] = 2
                count[2] -= 1
                i += 1




