class RecentCounter:
    def __init__(self):
        self.recent = []

    def ping(self, t: int) -> int:
        while len(self.recent) != 0 and self.recent[0] < t - 3000:
            self.recent.pop(0)
        self.recent.append(t)

        return len(self.recent)