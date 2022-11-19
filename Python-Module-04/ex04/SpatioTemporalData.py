import pandas as pd
import numpy as np

class SpatioTemporalData:
    """
    takes a dataset (pandas.DataFrame) as argument in its constructor and implements the following methods:
        • when(location): takes a location as an argument and returns a list containing the
            years where games were held in the given location,
        • where(date): takes a date as an argument and returns the location where the
            Olympics took place in the given year.
    """

    def __init__(self, dataset):
        self.data = dataset

    def when(self, location):
        """
            takes a location as an argument and returns a list containing the years where games were held in the given location
            Args:
                location (string)
            
            return:
                list of years where held in given location
        """
        filter = "City == '" + location + "'"
        return self.data.query(filter)['Year'].unique()

    def where(self, date):
        """
        Takes a date as an argument and returns the location where the Olympics took place in the given year.
            Args:
                date: the year to search

            return:
                location (string)
        """
        filter = "Year == " + str(date)
        return self.data.query(filter)['City'].unique()