import pandas as pd

def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    employees['time_spent'] = employees['out_time'] - employees['in_time']
    employees = employees.groupby(['emp_id', 'event_day'])['time_spent'].sum().reset_index()
    employees = employees.rename(columns={'event_day': 'day', 'time_spent': 'total_time'})
    return employees[['day', 'emp_id', 'total_time']]