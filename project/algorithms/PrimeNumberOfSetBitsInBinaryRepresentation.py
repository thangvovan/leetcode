class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        sol = 0
        primes = {2, 3, 5, 7, 11, 13, 17, 19}

        for i in range(left, right+1):
            if bin(i).count('1') in primes:
                sol+=1

        return sol