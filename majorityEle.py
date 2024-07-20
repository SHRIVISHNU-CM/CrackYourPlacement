class Solution:
    def majority(self,nums):
        a = None
        count = 0

        for num in nums:
            if count == 0:
                a= num
            count += (1 if num == a else -1)
        return a
    
if __name__ == "__main__":
    solution = Solution()
    nums1 = [3,2,3]
    res = solution.majority(nums1)
    print(res)
