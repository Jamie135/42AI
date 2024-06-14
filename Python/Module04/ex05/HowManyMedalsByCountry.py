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
        stop = False # for print test, unnecessary for the solution

        # iterrows() returns an iterator that yields index and row data for each row in df_team
        for _, row in df_team.iterrows():
            year = row['Year']
            medal = row['Medal'][0] # extract the first letter of the medal

            if row['Sport'] in team_sports:
                # unique key to avoid counting the same event
                event_key = (row['Year'], row['Event'])
                # if not stop:
                #     print(event_key)
                #     stop = True
                
                if event_key in medals_year:
                    # check if the specific medal type is already counted, if not we add to the set
                    if medal in medals_year[event_key]:
                        continue
                    else:
                        medals_year[event_key].add(medal)
                else:
                    medals_year[event_key] = {medal}
                # if not stop:
                #     print(medals_year[event_key])
                #     stop = True
            else:
                # initialize a new dictionary for that year
                if year not in medals_year:
                    medals_year[year] = {'G': 0, 'S': 0, 'B': 0}
                medals_year[year][medal] += 1
        # print(medals_year)
        
        # convert medals_year to a dictionary where the keys are only years 
        # and the value are the medals count
        result = {}
        # reminder: item() concatenate each pair of values in a dictionary into a list of tuple
        # key can be the year for solo sport or a tuple of year and event for team sport
        # medals is a dictionary of medals 
        for key, medals in medals_year.items():
            # if key is a tuple, we just want its first index that represents the year
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
print(how_many_medals_by_country(df, 'Thailand'))
