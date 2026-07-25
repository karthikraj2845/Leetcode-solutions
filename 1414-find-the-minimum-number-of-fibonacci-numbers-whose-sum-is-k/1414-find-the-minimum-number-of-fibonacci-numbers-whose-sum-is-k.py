class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        fib = [1,1]
        prev1 = 1
        prev2 = 1
        cur = 2
        while cur <= k:
            fib.append(cur)
            prev2 = prev1
            prev1 = cur
            cur = prev1 + prev2
        print(fib)
        n = len(fib)  
        c = 0 
        for i in range(n-1,-1,-1):
            if fib[i] <= k:
                k -= fib[i]
                c += 1
            if k == 0:return c
        
        

        