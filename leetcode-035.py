# 题目：704. 二分查找
# 地址：https://leetcode-cn.com/problems/binary-search/
# 标签：二分法

from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        index_left = 0
        index_right = len(nums)

        index_middle = (int)(index_left + (index_right - index_left) / 2)
        while index_left <= index_right:
            if nums[index_middle] > target:
                index_right = index_middle - 1
            elif nums[index_middle] < target:
                index_left = index_middle + 1
            else:
                return index_middle

            index_middle = (int)(index_left + (index_right - index_left) / 2)

        return index_left


if __name__ == '__main__':
    so = Solution()

    print(so.searchInsert([1, 3, 5, 6], 5))
