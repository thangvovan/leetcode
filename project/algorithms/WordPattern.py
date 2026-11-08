class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        m = s.split(" ")
        if len(pattern) != len(m):
            return False

        map = {}
        h = set()
        for i in range(len(pattern)):
            if pattern[i] not in map:
                if m[i] not in h:
                    map[pattern[i]] = m[i]
                    h.add(m[i])
                else:
                    return False
            else:
                if map[pattern[i]] != m[i]:
                    return False
        return True