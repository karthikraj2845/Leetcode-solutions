class Solution:
    def digitSum(self, s: str, k: int) -> str:
        def findSum(num):
            ans = 0
            while num > 0:
                ans += num%10
                num = num // 10
            return ans
        while len(s) > k:
            cur_s = ""
            for i in range(0,len(s),k):
                sub_s = s[i:i+k]
                # print(sub_s)
                int_subs = int(sub_s)
                cur_s += str(findSum(int_subs))
                # print(cur_s)
            s = cur_s
            # print(s)
        return s        

        