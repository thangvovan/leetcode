import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    employee = employee.merge(department, left_on="departmentId", right_on="id", suffixes=("", "_d"))
    highest = employee.groupby("name_d")['salary'].transform("max")
    return employee.loc[employee["salary"] == highest, ["name_d", "name", "salary"]].rename(columns={"name_d": "Department", "name": "Employee", "salary": "Salary"})