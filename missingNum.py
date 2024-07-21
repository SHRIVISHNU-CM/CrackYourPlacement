class Solution:
    def missNum(self,nums):
        n = len(nums) + 1
        expected_sum = n*(n+1)//2
        actual_sum = sum(nums)

        return expected_sum  - actual_sum
    
if __name__ == "__main__":
    solution = Solution()

    nums1 = [1,2,4,6,3,7,8]

    res = solution.missNum(nums1)
    print(res)