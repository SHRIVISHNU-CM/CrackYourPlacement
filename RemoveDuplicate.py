class Solution:
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        
        k = 1
        for i in range(1,len(nums)):
            if nums[i] !=nums[i-1]:
                nums[k] = nums[i]
        return k
    
if __name__ == "__main__":
    solution = Solution()
    nums1 = [1,1,2]
    res = solution.removeDuplicates(nums1)
    print(res)

    nums2 = [0,0,1,1,1,2,2,3,3,4]
    res = solution.removeDuplicates(nums1)
    print(res)