import pandas as pd

def food_delivery(delivery: pd.DataFrame) -> pd.DataFrame:
    immediate = delivery[delivery['order_date'] == delivery['customer_pref_delivery_date']]
    total_order = len(delivery)
    percentage = round(len(immediate) / total_order *100, 2)
    return pd.DataFrame({'immediate_percentage': [percentage]})