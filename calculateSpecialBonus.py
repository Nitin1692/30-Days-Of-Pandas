import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    employees['bonus'] =employees[(employees.name.astype(str).str[0] != 'M') & (employees.employee_id %2 !=0)]['salary']
    employees['bonus'] = employees.bonus.fillna(value=0)
    return employees[['employee_id', 'bonus']].sort_values(by=['employee_id'], ascending=True)