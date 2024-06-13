import pandas as pd
from FileLoader import FileLoader


def how_many_medals(df, name):
    try:
        if not isinstance(df, pd.DataFrame):
            print("The provided data is not a valid pandas DataFrame.")
            return
        if not isinstance(name, str):
            print("The athlete's name should be a string.")
            return
        
        # filter the DataFrame for the given name and non null medals
        # notna() referes to values that are not null
        df_name = df[(df['Name'] == name) & (df['Medal'].notna())]
        # print(df_name)

        medals_year = {}

        # group df_name by the year with groupby()
        # iterate through it with two iterator (one for year and one for medals group)
        for year, medal in df_name.groupby('Year'):
            # initialize the dictionary for the current year
            medals_year[year] = {'G': 0, 'S': 0, 'B': 0}
            # Count the number of each type of medal
            medals_year[year]['G'] = (medal['Medal'] == 'Gold').sum()
            medals_year[year]['S'] = (medal['Medal'] == 'Silver').sum()
            medals_year[year]['B'] = (medal['Medal'] == 'Bronze').sum()
        return medals_year
    
    except Exception as e:
        print(f"Error: {e}")

# Example usage:
loader = FileLoader()
data = loader.load("../data/athlete_events.csv")
print(how_many_medals(data, 'Kjetil Andr Aamodt'))
