class Solution:
    def maxArea(self,nums):
        left = 0
        right = len(nums) -1
        max_area = 0

        while left <right:
            width = right -left
            containerHeight = min(nums[left],nums[right])

            area = width * containerHeight
            max_area = max(max_area,area)

            if nums[left] < nums[right]:
                left +=1
            else:
                right -=1
        return max_area

if __name__ == "__main__":
    solution = Solution()

    nums1 = [1,8,6,2,5,4,8,3,7]
    res = solution.maxArea(nums1)
    print(res)
        