class PeekingIterator:
    def __init__(self, iterator):
        self.iterator = iterator
        self.current = self.iterator.next() if self.iterator.hasNext() else None        

    def peek(self):
        return self.current

    def next(self):
        value = self.current
        self.current = self.iterator.next() if self.iterator.hasNext() else None       
        return value

    def hasNext(self):
        return self.current != None