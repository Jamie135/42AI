import pandas as pd
from FileLoader import FileLoader


def how_many_medals_by_country(df, team):
    team_sports = [
        'Basketball', 'Football', 'Tug-Of-War', 'Handball', 'Water Polo', 
        'Hockey', 'Rowing', 'Volleyball', 'Synchronized Swimming', 'Baseball', 
        'Rugby', 'Lacrosse', 'Polo'
    ]
    try:
        if not isinstance(df, pd.DataFrame):
            print("The provided data is not a valid pandas DataFrame.")
            return
        if not isinstance(team, str):
            print("The country's name should be a string.")
            return
        
        # filter the DataFrame for the given country and non null medals
        # notna() referes to values that are not null
        df_team = df[(df['Team'] == team) & (df['Medal'].notna())]
        # print(df_team)

        medals_year = {}

        # iterrows() iterate over DataFrame rows as a pair (index, row)
        for _, row in df_team.iterrows():
            year = row['Year']
            medal = row['Medal'][0]

            # if team sport, count one medal per team per event
            if row['Sport'] in team_sports:
                # unique key to avoid counting the same event
                event_key = (row['Year'], row['Event'])
                print(event_key)
                if event_key in medals_year:
                    if row['Medal'][0] in medals_year[event_key]:
                        continue
                    else:
                        medals_year[event_key].add(row['Medal'][0])
                else:
                    medals_year[event_key] = {row['Medal'][0]}
            else:
                if year not in medals_year:
                    medals_year[year] = {'G': 0, 'S': 0, 'B': 0}
                medals_year[year][medal] += 1
        
        result = {}
        for key, medals in medals_year.items():
            if isinstance(key, tuple):
                year = key[0]
                if year not in result:
                    result[year] = {'G': 0, 'S': 0, 'B': 0}
                for medal in medals:
                    result[year][medal] += 1
            else:
                result[key] = medals
        
        return result
    except Exception as e:
        print(f"Error: {e}")


# Example usage
df = pd.read_csv('../data/athlete_events.csv')
print(how_many_medals_by_country(df, 'United States'))
