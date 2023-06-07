import os
class Loader:
    def __init__(self, file_name):
        self.file_name = file_name
        self.data_folder = "./data" 

    def load(self, df):
        file_path = os.path.join(self.data_folder, self.file_name)
        df.to_csv(file_path + '.csv', index=False)
        df.to_parquet(file_path + '.parquet', index=False)