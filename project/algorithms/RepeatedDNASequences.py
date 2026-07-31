from typing import List

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s) < 10:
            return []

        sol = []
        map = {}
        hashed = set()

        def num(c):
            if c == 'A':
                return 0
            elif c == 'C':
                return 1
            elif c == 'G':
                return 2
            else:
                return 3

        hash = 0
        for i in range(0, 10):
            hash += (num(s[i])*(4**(10-i-1)))
        map[hash] = s[0:10]

        string = s[0:10]
        for i in range(10, len(s)):
            hash -= (num(s[i-10])*(4**9))
            hash *= 4
            hash += num(s[i])

            string = string[1:10] + s[i]
            if hash in map and hash not in hashed:
                sol.append(string)
                hashed.add(hash)
            else:
                map[hash] = string

        return sol