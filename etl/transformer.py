import pandas as pd

class Transformer:
    def __init__(self, freq):
        self.freq = freq

    def transform(self, df):
        df.columns = df.columns.str.lower()
        df.dropna(inplace=True)
        df_grouped = df.groupby([pd.cut(df['year'], bins=range(min(df['year']), max(df['year'])+self.freq, self.freq)), 'sex'])['value'].sum()
        df_grouped = df_grouped.reset_index()
        df_grouped.columns = ['year', 'sex', 'sum']
        df_grouped['year'] = df_grouped['year'].astype(str)
        df_grouped['year'] = df_grouped['year'].str.strip('()[]')
        df_grouped[['year from', 'year to']] = df_grouped['year'].str.split(',', expand=True)
        df_grouped = df_grouped.drop('year', axis=1)
        return df_grouped