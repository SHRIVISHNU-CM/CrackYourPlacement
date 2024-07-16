class Solution:
    def twoSum(self,nums,k):
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] ==k:
                    return (i,j)
                    
        

if __name__ == "__main__":
    solution = Solution()

    nums1 = [2,7,11,15]
    k =9
    res = solution.twoSum(nums1,k)
    print(res)

    nums2 = [3,2,3] 
    k1  = 6
    res = solution.twoSum(nums2,k1)
    print(res)