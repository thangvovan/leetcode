from algorithms.DepartmentHighestSalary import *
from dataStructures import *

print(department_highest_salary(schema("""
| id | name  | salary | departmentId |
| -- | ----- | ------ | ------------ |
| 1  | Joe   | 70000  | 1            |
| 2  | Jim   | 90000  | 1            |
| 3  | Henry | 80000  | 2            |
| 4  | Sam   | 60000  | 2            |
| 5  | Max   | 90000  | 1            |
"""), schema("""
| id | name  |
| -- | ----- |
| 1  | IT    |
| 2  | Sales |
""")))