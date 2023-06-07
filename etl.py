import requests
import pandas as pd

def extract(url):
    response = requests.get(url)
    df = pd.read_csv(url)
    df.columns = df.columns.str.lower()
    df.dropna(inplace=True)
    return df



""" Group the years into five-year frequency intervals and calculate the counts """

def transform(df, freq):
    df = df.groupby([pd.cut(df['year'], bins=range(min(df['year']), max(df['year'])+freq, freq)), 'sex'])['value'].sum()
    df = df.reset_index()
    df.columns = ['year', 'sex', 'sum']
    df['year'] = df['year'].astype(str)
    df['year'] = df['year'].str.strip('()[]')
    df[['year from', 'year to']] = df['year'].str.split(',', expand=True)
    df = df.drop('year', axis=1)
    return df

def load(df,file_name):
    df.to_csv(file_name + '.csv', index=False)
    df.to_parquet(file_name + '.parquet', index=False)
    return df


def main():
    url = "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/EDA14/CSV/1.0/en"
    freq = 5
    df = extract(url)
    df_grouped = transform(df, freq)
    df_grouped = load(df_grouped,"data")
    print(df_grouped.head())

if __name__ == '__main__':
    main()