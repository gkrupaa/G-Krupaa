import pandas as pd
from sklearn.preprocessing import StandardScaler

def handle_missing_values(df, strategy="drop", fill_value=None, columns=None):
    """
    Handles missing values in a DataFrame.

    Parameters:
    - df (pd.DataFrame): The input DataFrame.
    - strategy (str): Strategy to handle missing values:
        - "drop": Drops rows with missing values.
        - "fill": Fills missing values with a specified value or mean/median/mode.
    - fill_value (any or str): The value to fill missing data if strategy is "fill".
        - Can be a specific value (e.g., 0) or "mean", "median", "mode".
    - columns (list): List of columns to apply the strategy to. If None, applies to all columns.

    Returns:
    - pd.DataFrame: DataFrame with missing values handled.
    """

    if columns is None:
        columns = df.columns

    if strategy == "drop":
        # Drop rows with missing values in the specified columns
        return df.dropna(subset=columns)

    elif strategy == "fill":
        if fill_value == "mean":
            for col in columns:
                df[col] = df[col].fillna(df[col].mean())
        elif fill_value == "median":
            for col in columns:
                df[col] = df[col].fillna(df[col].median())
        elif fill_value == "mode":
            for col in columns:
                df[col] = df[col].fillna(df[col].mode()[0])
        else:
            # Fill missing values with a specified value (e.g., 0 or any other constant)
            for col in columns:
                df[col] = df[col].fillna(fill_value)

    return df

def oneHotEncode(df, columns=['explicit']):
    """
    One-hot encodes categorical columns in a DataFrame.

    Parameters:
    - df (pd.DataFrame): The input DataFrame.
    - columns (list): List of columns to one-hot encode.

    Returns:
    - pd.DataFrame: DataFrame with one-hot encoding applied.
    """
    if columns == 'explicit':
        columns = df.select_dtypes(include=['object', 'category']).columns.tolist()

    return pd.get_dummies(df, columns=columns)

def write2csv(data, filename):
    """
    Write a DataFrame to a CSV file.

    Parameters:
    - data (pd.DataFrame): The input DataFrame.
    - filename (str): The output CSV file name.
    """
    data.to_csv(filename, index=False)

def normalizeData(data, columns):
    """
    Normalize the data using StandardScaler.

    Parameters:
    - data (pd.DataFrame): The input DataFrame.
    - columns (list): List of columns to normalize.

    Returns:
    - pd.DataFrame: DataFrame with normalized data.
    """
    scaler = StandardScaler()
    data[columns] = scaler.fit_transform(data[columns])

    return data

def dropColumns(data, columns):
    return data.drop(columns, axis=1)