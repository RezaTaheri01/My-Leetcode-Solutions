from typing import List


class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        binary_num = ""

        for i, num in enumerate(nums):
            binary_num += str(num)

            nums[i] = int(binary_num, 2) % 5 == 0

        return nums


s = Solution()

print(s.prefixesDivBy5(nums=[1, 0, 1]))
print(s.prefixesDivBy5(nums=[0, 1, 1]))
print(s.prefixesDivBy5(nums=[1, 1, 1]))
