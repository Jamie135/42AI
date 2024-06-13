import pandas as pd
from FileLoader import FileLoader


def youngest_fellah(df, year):
    try:
        if not isinstance(df, pd.DataFrame):
            print("The provided data is not a valid pandas DataFrame.")
            return
        if not isinstance(year, int):
            print("The Olympic year should be an integer.")
            return
        
        # filter the DataFrame for the given year
        # syntax: df_year is equal to SELECT 'Year' WHERE the value is equal year
        df_year = df[df['Year'] == year]
        # print(df_year)
        
        # find the youngest age for females
        youngest_female = df_year[df_year['Sex'] == 'F']['Age'].min()
        # print(youngest_female)
        
        # find the youngest age for males
        youngest_male = df_year[df_year['Sex'] == 'M']['Age'].min()
        # print(youngest_male)

        return {'f': youngest_female, 'm': youngest_male}
    
    except Exception as e:
        print(f"Error: {e}")


# Example usage:
loader = FileLoader()
data = loader.load("../data/athlete_events.csv")
print(youngest_fellah(data, 2004))
# Output
# {’f’: 13.0, ’m’: 14.0}
