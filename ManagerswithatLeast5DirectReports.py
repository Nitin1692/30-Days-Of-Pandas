import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    val = employee.groupby('managerId', as_index=False).agg(reporting=('id',"count")).query('5<=reporting')['managerId']
    return employee[employee['id'].isin(val)][['name']]