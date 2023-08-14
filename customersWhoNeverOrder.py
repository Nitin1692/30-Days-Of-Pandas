import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    cust_orders = orders['customerId'].unique()
    cust_customer = customers[~customers.id.isin(cust_orders)]
    return cust_customer[['name']].rename(columns={'name': 'Customers'})