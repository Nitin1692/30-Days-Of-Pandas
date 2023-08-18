import pandas as pd

def count_rich_customers(store: pd.DataFrame) -> pd.DataFrame:
    value = store[(store.amount > 500)]
    count = value['customer_id'].nunique()
    return pd.DataFrame({'rich_count': [count]})