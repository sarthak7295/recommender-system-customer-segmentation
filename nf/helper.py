import pandas as pd
import json

df_client_rfm = pd.read_csv('./../client_rfm.csv', sep=',')

df_client_rfm = df_client_rfm[['Client','Rank_Recency','Rank_Frequency','Rank_Monetary','Cluster']]
df_client_rfm.drop_duplicates(keep='first',inplace=True)

print(df_client_rfm['Client'].nunique())


def get_users():
    result = df_client_rfm.to_json(orient='records')
    return result

