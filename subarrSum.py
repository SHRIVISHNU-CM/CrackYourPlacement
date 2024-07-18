from collections import defaultdict
class Solution:
    def subarray(self,nums,k):
        dic = defaultdict(int)
        currsum = 0
        dic[0] = 1
        result = 0 

        for n in nums:
            currsum +=n
            diff = currsum -k
            if diff in dic:
                result +=dic[diff]
            dic[currsum] +=1
        return result
    
if __name__ =="__main__":
    solution = Solution()
    nums1 = [1,1,1]
    k = 2
    res = solution.subarray(nums1, k)
    print(res)
