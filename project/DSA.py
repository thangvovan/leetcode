from algorithms.CustomersWhoNeverOrder import *
from dataStructures import *

print(find_customers(schema("""
| id | name    |
| -- | ------- |
| 5  | wyu{sk  |
| 2  | rgt     |
| 4  | hbrmrz  |
| 1  | tmjow   |
| 3  | ynrl{wq |
"""), schema("""
| id | customerId |
| -- | ---------- |
| 10 | 4          |
| 3  | 5          |
| 2  | 3          |
| 6  | 2          |
| 4  | 3          |
| 8  | 3          |
| 9  | 3          |
| 1  | 2          |
| 7  | 2          |
| 5  | 3          |
""")))