import pandas as pd

def clean_and_edit_csv(input_file, output_file):
    # Read the CSV file into a pandas DataFrame
    df = pd.read_csv(input_file)

    # Remove empty rows
    df.dropna(how='all', inplace=True)

    # Remove rows where 'Godiste' or 'Proizvodjac' columns are NaN
    df.dropna(subset=['Godiste', 'Proizvodjac'], inplace=True)

    # Remove duplicate rows
    df.drop_duplicates(inplace=True)

    # Function to edit Kilometraza column
    def edit_kilometraza(km):
        try:
            km = int(km)
            if 100 <= km <= 999:
                return km * 1000
            else:
                return km
        except ValueError:
            return km

    # Apply the edit_kilometraza function to the 'Kilometraza' column
    df['Kilometraza'] = df['Kilometraza'].apply(edit_kilometraza)

    # Save the modified dataframe to a new CSV file
    df.to_csv(output_file, index=False)

# Specify the input and output file paths
input_file = 'data.csv'
output_file = 'data.csv'

# Clean, edit Kilometraza, remove duplicates, and save the result to a new CSV file
clean_and_edit_csv(input_file, output_file)
