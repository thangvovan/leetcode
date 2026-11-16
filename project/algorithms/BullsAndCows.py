class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        secret = list(secret) 
        guess = list(guess)

        i = 0
        while i < len(secret):
            if int(secret[i]) == int(guess[i]):
                bulls += 1 
                secret.pop(i)
                guess.pop(i)
            else:
                i += 1

        cows = 0
        j = 0
        while j < len(secret):
            if secret[j] in guess:
                cows += 1
                guess.remove(secret[j])
                secret.pop(j)
            else:
                j += 1

        return str(bulls) + "A" + str(cows) + "B"