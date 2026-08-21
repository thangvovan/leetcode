class Solution:
    def numDecodings(self, s: str) -> int:
        map = {}

        def dynamic(st):
            if st in map:
                return map[st]

            if len(st) == 0:
                map[st] = 1
                return 1
            if int(st[0]) <= 0:
                map[st] = 0
                return 0
            
            num = 0
            if len(st) >= 2 and (int(st[0]) == 1 or (int(st[0]) <= 2 and int(st[1]) <= 6)):
                num += dynamic(st[2:])
            num += dynamic(st[1:])

            map[st] = num
            return num
        
        return dynamic(s)

    def numDecodings(self, s: str) -> int:
        memo = {}

        def dynamic(i: int) -> int:
            if i in memo:
                return memo[i]
            if i == len(s):
                return 1
            if s[i] == '0':
                return 0
            
            ans = 0
            if s[i] == '*':
                ans += dynamic(i+1) * 9
            else:
                ans += dynamic(i+1)

            if i+1 < len(s):
                if s[i] == '*' and s[i+1] == '*':
                    ans += dynamic(i+2) * 15
                elif s[i] != '*' and s[i+1] != '*':
                    if 10 <= int(s[i] + s[i+1]) <= 26:
                        ans += dynamic(i+2)
                elif s[i] != '*' and s[i+1] == '*':
                    if s[i] == '1':
                        ans += dynamic(i+2) * 9
                    elif s[i] == '2':
                        ans += dynamic(i+2) * 6
                elif s[i] == '*' and s[i+1] != '*':
                    if s[i+1] in '0123456':
                        ans += dynamic(i+2) * 2
                    elif s[i+1] in '789':
                        ans += dynamic(i+2)

            memo[i] = ans % (10**9 + 7)
            return memo[i]

        return dynamic(0)