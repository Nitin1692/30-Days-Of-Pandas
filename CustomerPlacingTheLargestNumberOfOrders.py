import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    value = orders.groupby('customer_number')['order_number'].count().reset_index()
    return value[value['order_number'] == value['order_number'].max()][['customer_number']]