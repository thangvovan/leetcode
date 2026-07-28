from algorithms.RisingTemperature import *
from dataStructures import *

print(rising_temperature(schema("""
| id | recordDate | temperature |
| -- | ---------- | ----------- |
| 1  | 2000-12-14 | 3           |
| 2  | 2000-12-16 | 5           |
""")))