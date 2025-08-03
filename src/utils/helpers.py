from pathlib import Path

def save_df_to_excel(file_name, df):
    """
    Save the DataFrame of companies to an Excel file.
    
    Parameters:
    file_name (str): Name of the Excel file to save.
    df_companies (pd.DataFrame): DataFrame containing company data.
    """
    from pathlib import Path
    
    # Define folder and file path
    folder = Path("../data")
    file_path = folder / f"{file_name}.xlsx" # Use f-string for dynamic file name
    
    # Create folder if it doesn't exist
    folder.mkdir(parents=True, exist_ok=True)

    # Save DataFrame to Excel
    df.to_excel(file_path, index=False)