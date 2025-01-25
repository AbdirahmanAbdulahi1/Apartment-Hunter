import apartmentBot
import pandas as pd
dataframe = apartmentBot.df

    

def sortByExpensive(df):
    #replace anything that can cause error with empty string
    #convert the string prices into integers for comparison 
    #If anything in the field causes a parsing error  make it NaN
    #Convert NaN into zero for comparison
    # then create the sorted dataframe 
    df['Price ($CAD)'] = df['Price ($CAD)'].str.replace(r'[^0-9]', '', regex=True)
    df['Price ($CAD)'] = pd.to_numeric(df['Price ($CAD)'], errors='coerce').fillna(0).astype(int)
    sorted_df = df.sort_values(by='Price ($CAD)', ascending=False)
    return sorted_df

def sortByCheapest(df):
    #same logic as sortByExpensive
    #I turned df['Price ($CAD)'] = pd.to_numeric(df['Price ($CAD)'], errors='coerce').fillna(0).astype(int)
    #into 2 different lines because I was getting errors
    df['Price ($CAD)'] = df['Price ($CAD)'].str.replace(r'[^0-9]', '', regex=True)
    df['Price ($CAD)'] = pd.to_numeric(df['Price ($CAD)'], errors='coerce')
    df['Price ($CAD)'] = df['Price ($CAD)'].fillna(0).astype(int)
    sorted_df = df.sort_values(by='Price ($CAD)', ascending=True)
    return sorted_df
    

def sortByMostRooms(df):
    #similar to previous functions
    # No need to replace any error causing strings in fields cause there were none
    #first line converts string number into ins, then it turns studio to NaN
    #All NaN turns into 0
    #after sorting replace all 0's with studio becuase 
    df['Rooms'] = pd.to_numeric(df['Rooms'], errors='coerce').fillna(0).astype(int)
    sorted_df = df.sort_values(by='Rooms', ascending=False)
    sorted_df['Rooms'] = sorted_df['Rooms'].replace(0,"Studio")
    return sorted_df



def sortByBiggest(df):
    #same Logic as sortByMostRooms
    df['Area (ft²)'] = pd.to_numeric(df['Area (ft²)'], errors='coerce').fillna(0).astype(int)
    sorted_df = df.sort_values(by='Area (ft²)', ascending=False, na_position='last')
    sorted_df['Area (ft²)'] = sorted_df['Area (ft²)'].replace(0,"N/A")
    return sorted_df







