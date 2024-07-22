class Solution:
    def strIn(self,haystack,needle):
        if not needle:
            return 0
        
        for i in range(len(haystack)):
            if haystack[i :i+len(needle)] == needle:
                return i 
        return -1
    
if __name__ == "__main__":
    solution = Solution()

    a = "sadbutsad"
    b = "sad"

    res = solution.strIn(a,b)
    print(res)