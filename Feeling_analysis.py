import requests
import json
import pandas as pd
import datetime as dt

SCORE_TAG_MEANINGS ={
'P+': 'P+: strong positive',
'P': 'P: positive',
'NEU':'NEU: neutral',
'N':'N: negative',
'N+':'N+: strong negative',
'NONE':'NONE: without polarity'
}

def feeling_analysis(text):
    url = "https://api.meaningcloud.com/sentiment-2.1"

    payload={
        'key': 'b9a2dc96eb49d8757b7bac4e0995e4f7',
        'txt': text,
        'lang': 'auto'
    }

    response = requests.post(url, data=payload)

    response_status = response.status_code

    if response_status == 200:
        dict_return = json.loads(response.text)
        return SCORE_TAG_MEANINGS[dict_return['score_tag']]
    else:
        print(f'Error: return {response_status}')
        exit(1)

date = dt.datetime.now().strftime('%Y%m%d')
parquet_df = pd.read_parquet(f'Heading_News_{date}.parquet')

parquet_df['feeling'] = parquet_df['title'].apply(feeling_analysis)

parquet_df.to_parquet(f'Daily_News_{date}.parquet', index=None)
parquet_df.to_csv(f'Daily_News_{date}.csv', index=False, sep=';')