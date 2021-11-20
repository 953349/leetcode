# 题目：977. 有序数组的平方
# 地址：https://leetcode-cn.com/problems/squares-of-a-sorted-array/
# 标签：数组

class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        squre_nums =[]
        for item in nums:
            squre_nums.append(item*item)

        squre_nums.sort()
        return squre_nums;

if __name__ == '__main__':
    so = Solution()
    nums = [-7, -3, 2, 3, 11]

    print( so.sortedSquares(nums) )
