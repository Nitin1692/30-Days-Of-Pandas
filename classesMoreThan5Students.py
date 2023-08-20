import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    value = courses.groupby('class').count().reset_index()
    return value[value['student'] >= 5][['class']]