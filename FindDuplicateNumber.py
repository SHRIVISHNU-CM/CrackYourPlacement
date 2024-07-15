class Solution:
    def duplicateNumber(self,nums):
        a = nums[0]
        b = nums[0]

        while True:
            a= nums[a]
            b = nums[nums[b]]

            if a == b:
                break
        
        a = nums[0]

        while a !=b:
            a = nums[a]
            b = nums[b]

        return b
    
if __name__ == "__main__":
    solution = Solution()

    nums1 = [1,3,4,2,2]
    res = solution.duplicateNumber(nums1)
    print(res)

    nums2 = [3,1,3,4,2]
    res = solution.duplicateNumber(nums2)
    print(res)

    nums3 = [3,3,3,3,3]
    print(solution.duplicateNumber(nums3))