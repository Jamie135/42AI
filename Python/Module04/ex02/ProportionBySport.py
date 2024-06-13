import pandas as pd
from FileLoader import FileLoader


def proportion_by_sport(df, year, sport, gender):
    try:
        if not isinstance(df, pd.DataFrame):
            print("The provided data is not a valid pandas DataFrame.")
            return
        if not isinstance(year, int):
            print("The Olympic year should be an integer.")
            return
        if not isinstance(sport, str):
            print("The sport's name should be a string.")
            return
        if not isinstance(gender, str):
            print("The athlete's gender should be a string.")
            return
        
        # filter the DataFrame for the given year and gender
        df_year_gender = df[(df['Year'] == year) & (df['Sex'] == gender)]
        
        # drop duplicates to count only unique athletes
        df_id_unique = df_year_gender.drop_duplicates(subset='ID')
        
        # get the total distinct athlete with shape[0] that represent the row i.e. the number of distinct id
        total_ath = df_id_unique.shape[0]

        # get the total distinct athlete that plays the sport passed in the argument
        sport_ath = df_id_unique[df_id_unique['Sport'] == sport].shape[0]

        return  sport_ath / total_ath
    
    except Exception as e:
        print(f"Error: {e}")


# Example usage:
loader = FileLoader()
data = loader.load("../data/athlete_events.csv")
print(proportion_by_sport(data, 2004, 'Tennis', 'F'))
