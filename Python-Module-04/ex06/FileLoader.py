import pandas as pd

class FileLoader:
    """Class to load and display a CSV file"""

    def __init__(self) -> None:
        pass

    def load(self, path):
        """ load the 'path' file, display a message specifying the dimensions of the dataset
            and return the dataset 
            args:
                path: path of the file to load

            return:
                the dataset loaded as a pandas.Dataframe
        """
        try:
            data = pd.read_csv(path)
            columns = data.columns
            print(f"Loading dataset of dimensions {len(data)} x {len(columns)}")
            return data
        except FileNotFoundError:
            print(f"Error: [{path}] not found.")
            return None
        except pd.errors.EmptyDataError:
            print(f"Error: [{path}] is empty")

    def display(self, df, n):
        """
            display the first n rows of a dataset
            Args:   df  a dataset in pandas.Dataframe format
                    n an integer, display the fisrt n rows if n positive,
                        or the last n rows id n is negative.
            return:
                    None   
        """
        if isinstance(df, pd.DataFrame):
            try:
                if int(n) == n:
                    if n >= 0:
                        print(df[:n])
                    else:
                        print(df.tail(-n))
                else:
                    print("Error: n must be an integer.")
            except Exception:
                print("Error: n must be an integer.")
        else:
            print(f"Error: {type(df)} is not a pandas.Dataframe.")
