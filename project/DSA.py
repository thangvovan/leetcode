from algorithms.ImplementTriePrefixTree import *
from dataStructures import *

# print(Solution().countPrimeSetBits(10, 15))
obj = Trie()
obj.insert("apple")
print(obj.search("apple"))
print(obj.search("app"))
print(obj.startsWith("app"))
obj.insert("app")
print(obj.search("app"))