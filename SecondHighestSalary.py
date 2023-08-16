import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    employee = employee['salary'].sort_values(ascending=False).drop_duplicates()
    if len(employee) > 1:
        value = employee.iloc[1]
    else:
        value = None
    return pd.DataFrame({'SecondHighestSalary': [value]})   