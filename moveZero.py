class Solution:
    def moveZero(self,nums):
        a = 0
        for i in range(len(nums)):
            if nums[i] !=0:
                nums[a],nums[i] = nums[i] , nums[a]
                a +=1


if __name__ =="__main__":
    solution = Solution()

    nums1 = [0,1,0,3,12]
    solution.moveZero(nums1)
    print(nums1)