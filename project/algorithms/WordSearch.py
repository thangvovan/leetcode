from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        s = set()

        def dfs(i, j, cur):
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or (i, j) in s:
                return False

            s.add((i, j))
            if board[i][j] == word[cur]:
                if cur == len(word)-1:
                    s.remove((i, j))
                    return True
                else:
                    sol = (dfs(i-1, j, cur+1)) or (dfs(i, j+1, cur+1)) or (dfs(i+1, j, cur+1)) or (dfs(i, j-1, cur+1))
                    s.remove((i, j))
                    return sol
            else:
                s.remove((i, j))
                return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    s.add((i, j))
                    if len(word) == 1 or dfs(i-1, j, 1) or dfs(i, j+1, 1) or dfs(i+1, j, 1) or dfs(i, j-1, 1):
                        return True
                    s.remove((i, j))
        
        return False

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def dfs(x, y, root):
            letter = board[x][y]
            cur = root[letter]

            word = cur.pop('#', False)
            if word:
                res.append(word)

            board[x][y] = '*'
            for dirx, diry in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                curx, cury = x + dirx, y + diry
                if 0 <= curx < m and 0 <= cury < n and board[curx][cury] in cur:
                    dfs(curx, cury, cur)

            board[x][y] = letter
            if not cur:
                root.pop(letter)

        trie = {}
        for word in words:
            cur = trie
            for letter in word:
                cur = cur.setdefault(letter, {})
            cur['#'] = word
            
        m, n = len(board), len(board[0])
        res = []
        
        for i in range(m):
            for j in range(n):
                if board[i][j] in trie:
                    dfs(i, j, trie)

        return res