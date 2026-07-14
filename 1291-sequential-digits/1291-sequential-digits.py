class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        def find_next(num):
            nonlocal initial
            unit_digit = num%10
            if unit_digit == 9:
                ini_unit_digit = initial%10
                initial = initial*10 +(ini_unit_digit + 1)
                return initial
            next = 0
            pos = 1
            while num > 0:
                cur = num%10
                next = next + (cur + 1)*pos
                pos *= 10
                num = num//10
            return next    
        start = 1
        initial = start
        while start < low:
            start = find_next(start)
        ans =  []
        n_digits_start = len(str(start))
        initial = 0
        cur = 1
        cur_digits =0
        while cur_digits < n_digits_start:
            initial = initial*10 +cur
            cur += 1
            cur_digits += 1
        while start <= high:
            ans.append(start)
            start = find_next(start)
            print(start)
        return ans         
        