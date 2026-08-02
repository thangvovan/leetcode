class MyHashSet:
    def __init__(self):
        self.map = [None for _ in range(0, 10**6+1)]

    def add(self, key: int) -> None:
        self.map[key] = key

    def remove(self, key: int) -> None:
        self.map[key] = None

    def contains(self, key: int) -> bool:
        return self.map[key] != None
