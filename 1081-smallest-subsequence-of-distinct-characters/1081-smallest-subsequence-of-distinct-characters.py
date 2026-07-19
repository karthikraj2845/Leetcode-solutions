class Solution:
    def smallestSubsequence(self, s: str) -> str:
        map = {}
        for i,ch in enumerate(s):
            map[ch] = i
        v = set()
        stack = []
        for i,ch in enumerate(s):
            if ch in v:continue
            while stack and stack[-1] > ch and map[stack[-1]] > i:
                v.remove(stack.pop())
            stack.append(ch)
            v.add(ch)
        return "".join(stack)            
        