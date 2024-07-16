class Solution :
    def threeSum(self,nums):

       nums.sort()
       result =[]
       n = len(nums)

       for i in range(n-2):
           if i >0 and nums[i] == nums[i-1]:
               continue
           left = i+1
           right = n-1

           while left<right:
               curr = nums[i] + nums[left] + nums[right]
               if curr == 0:
                   result.append([nums[i],nums[left],nums[right]])
                   while left <right and nums[left ] == nums[left+1]:
                       left +=1
                
                    
                   while left <right  and nums[right] == nums[right-1]:
                       right -=1
                   left +=1
                   right -=1
               elif curr < 0:
                   left +=1
               else:
                   right -=1

       return result
                    
                    
if __name__ == "__main__":
    solution = Solution()

    nums1 =[-1,0,1,2,-1,-4]
    res = solution.threeSum(nums1)
    print(res)