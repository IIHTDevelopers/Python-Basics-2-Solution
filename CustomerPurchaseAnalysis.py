
import pandas as pd

def create_dataframe():
    data = {
        'Customer': ['Jane', 'Mike', 'Tom', 'Sara', 'Leo'],
        'Items_Bought': [4, 8, 6, 1, 10],
        'Amount_Spent': [200.0, 500.0, 350.0, 75.0, 750.0]
    }
    return pd.DataFrame(data)

def calculate_average_spending(df):
    return df['Amount_Spent'].mean()

def get_top_spenders(df, average_spending):
    return df[df['Amount_Spent'] > average_spending]
