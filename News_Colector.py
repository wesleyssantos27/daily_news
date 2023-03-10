import requests as re
import datetime as dt
import pandas as pd
import json

countries = {'Brazil': 'br','United States': 'us', 'Portugal': 'pt'}
news_df = pd.DataFrame(columns=['country','title','description','url','source_name'])

for country_name, country_id  in countries.items():
    parameters = {
                'apikey':'c11a24beca4eb7e251c74ee5abd2f71e',
                'category':'general',
                'country':country_id,
                #'lang':'pt', Considerar adicionar conectar em uma API de traducao num proximo momento
                'max':5
                }

    api_return = re.get(
    'https://gnews.io/api/v4/top-headlines',
    params=parameters
    )

    if api_return.status_code == 200:
        dict_return = json.loads(api_return.text)
        df = pd.DataFrame.from_dict(dict_return['articles'])

        df['source_name'] = df['source'].apply(lambda x: x['name'])
        df['country'] = country_name
                
        df = df[['country','title','description','url','source_name']]
        
        news_df = pd.concat([news_df, df])
    else:
        print(f'Error: return {api_return.status_code}')
        exit(1)

date = dt.datetime.now().strftime('%Y%m%d')

news_df[['country','title','description','url','source_name']].to_parquet(f'Raw_News_{date}.parquet', index=None)