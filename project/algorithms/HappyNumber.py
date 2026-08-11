class Solution:
    def isHappy(self, n: int) -> bool:
        visit = set()

        while n not in visit:
            visit.add(n)

            output = 0
            while n:
                digit = n % 10
                output += digit ** 2
                n = n // 10
            n = output

            if n == 1:
                return True
        
        return False