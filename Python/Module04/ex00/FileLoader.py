import pandas as pd

class FileLoader:

    def load(self, path):
        try:
            df = pd.read_csv(path)
            print(f"Loading dataset of dimensions {df.shape[0]} x {df.shape[1]}")
            return df
        except Exception as e:
            print(f"Error: {e}")
            return None


    def display(self, df, n):
        try:
            if not isinstance(df, pd.DataFrame):
                print("The provided data is not a valid pandas DataFrame.")
                return

            if not isinstance(n, int):
                print("The number of rows to display should be an integer.")
                return
            
            if n > 0:
                # print the first n rows
                print(df.head(n))
            elif n < 0:
                # print the last n rows
                print(df.tail(-n))
            else:
                print("The value of n should be non-zero.")
        except Exception as e:
            print(f"Error: {e}")


# Example usage:
loader = FileLoader()
data = loader.load("../data/athlete_events.csv")
loader.display(data, -2)
