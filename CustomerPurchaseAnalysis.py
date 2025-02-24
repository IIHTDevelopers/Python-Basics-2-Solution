# customer_purchase_analysis.py
import pandas as pd


def create_dataframe():
    # Customer purchase dataset
    data = {
        'Customer': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve'],
        'Items_Bought': [3, 7, 5, 2, 9],
        'Amount_Spent': [150.0, 400.0, 275.0, 100.0, 600.0]
    }
    # Create DataFrame
    df = pd.DataFrame(data)
    return df


def calculate_average_spending(df):
    # Calculate the average spending
    return df['Amount_Spent'].mean()


def get_top_spenders(df, average_spending):
    # Identify customers who spent above the average
    return df[df['Amount_Spent'] > average_spending]


def main():
    df = create_dataframe()
    average_spending = calculate_average_spending(df)

    print(" Customer Purchase Analysis\n")
    print(df)

    top_spenders = get_top_spenders(df, average_spending)
    print("\n High-Spending Customers (Above Average):\n", top_spenders)




if __name__ == "__main__":
    main()
