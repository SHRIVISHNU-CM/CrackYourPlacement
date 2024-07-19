class Solution:
    def isValid(self, s):
        bracket_map = {")":"(","}":"{","]":"["}
        stack = []

        for char in s:
            if char in bracket_map:
                top_ele = stack.pop() if stack else "#"

                if bracket_map[char] != top_ele:
                    return False
            else:
                stack.append(char)

        return not stack

if __name__ == "__main__":
    solution = Solution()

    s1 = "()"
    res=solution.isValid(s1)
    print(res)    