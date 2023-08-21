import pandas as pd

def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    value = actor_director.groupby(['actor_id', 'director_id'])['timestamp'].size().reset_index()
    value = value[value['timestamp'] >= 3]
    return value[['actor_id', 'director_id']]