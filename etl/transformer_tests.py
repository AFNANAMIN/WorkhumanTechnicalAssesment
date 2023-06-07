import unittest
import pandas as pd
from transformer import Transformer

class TransformerTests(unittest.TestCase):
    def setUp(self):
        self.freq = 5
        self.transformer = Transformer(self.freq)

    def test_transform(self):
        # Create a sample DataFrame for testing
        df = pd.DataFrame({
            'year': [1990, 1991, 1992, 1993],
            'sex': ['Male', 'Female', 'Male', 'Female'],
            'value': [10, 20, 30, 40]
        })
        
        df_grouped = self.transformer.transform(df)

        # Add assertions to test the transformed DataFrame
        self.assertIsInstance(df_grouped, pd.DataFrame)


    def test_transform_column_names(self):
        # Create a sample DataFrame for testing
        df = pd.DataFrame({
            'Year': [1990, 1991, 1992, 1993],
            'Sex': ['SEX', 'SUM', 'year from', 'year to'],
            'Value': [10, 20, 30, 40]
        })

        # Call the transform method
        df_grouped = self.transformer.transform(df)

        # Check if the column names are transformed to lowercase
        expected_columns = ['sex', 'sum', 'year from', 'year to']
        self.assertEqual(list(df_grouped.columns), expected_columns)

    

if __name__ == '__main__':
    unittest.main()