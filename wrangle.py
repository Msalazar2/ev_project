import pandas as pd
import os

# =============================== ACQUISITION FUNCTION ===========================
def get_ev():
    '''
    Retrieve EV charging station data.

    This function checks if a CSV file containing EV charging station data exists.
    If the file exists, it reads the data from the file. If not, it prints an error message to

    Returns:
    --------
    pd.DataFrame
        A DataFrame containing EV charging station data.

    Raises:
    -------
    Exception
        If there's an error during file operations or data retrieval.
    '''
    try:
        if os.path.isfile('EV_Charging_Stations.csv'):
            print('Found file')
            # If csv file exists, read in data from csv file.
            df = pd.read_csv('EV_Charging_Stations.csv', index_col=0)
            
        else:
            print('Retrieving file...\n')
            # Read fresh data from db into a dataframe
            df = new_telco_data()
            
            # Cache data
            df.to_csv('EV_Charging_Stations.csv')
            print('\nFile retrieved.')
            
    except Exception as e:
        print(f"Error: {e}")

    return df
        # Handle the error appropriately, e.g., return a default dataframe or raise an exception.



# ============================= PREPARE FUNCTION ========================================

def clean_ev(df):
    '''
    Clean EV charging station data.

    This function performs the following cleaning steps:
    - Converts column names to lowercase.
    - Creates a 'Coordinates' column by combining index and 'Y' column values.
    - Resets the index to make 'Coordinates' a regular column.
    - Drops the 'X' and 'Y' columns.
    - Drops duplicate rows based on all columns.

    Parameters:
    -----------
    df : pd.DataFrame
        The input DataFrame containing EV charging station data.

    Returns:
    --------
    pd.DataFrame
        A cleaned DataFrame.
    '''

    df.columns = df.columns.str.lower()

    # Create the 'Coordinates' column by combining index and 'Y' column values
    df['coordinates'] = df.index.astype(str) + ', ' + df['y'].astype(str)
    
    # Reset the index to make 'Coordinates' a regular column
    df = df.reset_index(inplace=False)
    
    # Drop 'X' and 'Y' columns
    df = df.drop(columns=['X', 'y'])
    
    # Drop duplicates based on all columns
    df = df.drop_duplicates()

    return df


    
    