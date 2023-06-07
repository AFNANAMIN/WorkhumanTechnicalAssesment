from .extractor import Extractor
from .transformer import Transformer
from .loader import Loader

def run_etl():
    url = "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/EDA14/CSV/1.0/en"
    freq = 5

    extractor = Extractor(url)
    df = extractor.extract()

    transformer = Transformer(freq)
    df_grouped = transformer.transform(df)

    loader = Loader("data")
    loader.load(df_grouped)