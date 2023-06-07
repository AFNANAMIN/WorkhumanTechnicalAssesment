import requests
import pandas as pd

class Extractor:
    def __init__(self, url):
        self.url = url

    def extract(self):
        response = requests.get(self.url)
        df = pd.read_csv(self.url)
        return df
    
    