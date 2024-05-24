import pandas as pd

# Function to clean the dataframe
def clean_dataframe(df):
    # Remove rows where all elements are NaN
    df.dropna(how='all', inplace=True)
    # Remove rows where 'Godiste' or 'Proizvodjac' columns are NaN
    df.dropna(subset=['Godiste', 'Proizvodjac'], inplace=True)
    # Remove duplicate rows
    df.drop_duplicates(inplace=True)
    return df

# Function to modify 'Kilometraza' column
def modify_kilometraza(df):
    def transform_kilometraza(value):
        try:
            value = int(value)
            if 100 <= value <= 999:
                return value * 1000
            else:
                return value
        except ValueError:
            return value

    df['Kilometraza'] = df['Kilometraza'].apply(transform_kilometraza)
    return df

def merge_csv_files(file1, file2, file3, output_file):
    # Read the CSV files into pandas dataframes
    df1 = pd.read_csv(file1)
    df2 = pd.read_csv(file2)
    df3 = pd.read_csv(file3)

    # Concatenate the dataframes
    combined_df = pd.concat([df1, df2, df3], ignore_index=True)

    # Clean the combined dataframe
    clean_df = clean_dataframe(combined_df)
    
    # Modify 'Kilometraza' column
    modified_df = modify_kilometraza(clean_df)

    # Save the modified dataframe to a new CSV file
    modified_df.to_csv(output_file, index=False)
    
# Specify the paths to the input and output files
file1 = 'data_1.csv'
file2 = 'data_2.csv'
file3 = 'data_3.csv'
output_file = 'data.csv'

# Merge the CSV files
merge_csv_files(file1, file2, file3, output_file)
