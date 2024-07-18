class Solution:
    def findDuplicates(self,nums):
        result =[]

        for i in nums:
            index = abs(i) -1
            if nums[index] >0:
                nums[index] = -nums[index]
            else:
                result.append(abs(i))
        return result

if __name__ =="__main__":
    solution = Solution()

    nums1 = [4,3,2,7,8,2,3,1]
    print(solution.findDuplicates(nums1))