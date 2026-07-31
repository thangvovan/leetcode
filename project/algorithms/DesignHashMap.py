class MyHashMap:
    def __init__(self):
        self.map = [None for _ in range(0, 10**6+1)]

    def put(self, key: int, value: int) -> None:
        map[key] = value

    def get(self, key: int) -> int:
        return map[key] if map[key] != None else -1

    def remove(self, key: int) -> None:
        map[key] = None