import pandas as pd
from FileLoader import FileLoader


class SpatioTemporalData:

    def __init__(self, data):
        self.data = data
    

    def when(self, location):
        df_location = self.data[self.data['City'] == location]
        # print(df_location)
        years = df_location['Year'].unique()
        return years
    

    def where(self, date):
        df_year = self.data[self.data['Year'] == date]
        # print(df_year)
        city = df_year['City'].unique()
        return city
    

# Example usage:
from FileLoader import FileLoader
loader = FileLoader()
data = loader.load('../data/athlete_events.csv')
sp = SpatioTemporalData(data)
print(sp.where(1896))  # Output: ['Athina']
print(sp.where(2016))  # Output: ['Rio de Janeiro']
print(sp.when('Athina'))  # Output: [1896, 1906, 2004]
print(sp.when('Paris'))  # Output: [1900, 1924]
