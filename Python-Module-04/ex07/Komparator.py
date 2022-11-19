import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

class Komparator:
    """
    Class implementing plotting methods
    """

    def __init__(self, data):
        if isinstance(data, pd.DataFrame):
            self.data = data
        else:
            raise TypeError("Error, data is not a pandas.DataFrame.")

    def compare_box_plots(self, categorical_var, numerical_var):
        """
            Displays a series of box plots to compare how the distribution of
            the numerical variable changes if we only consider the subpopulation
            which belongs to each category. There should be as many box plots as
            categories.
            args:
                categorical_var (string)
                numerical_var (string)
        """
        sns.boxplot( x=self.data[categorical_var], y=self.data[numerical_var] , width=0.3)
        plt.tick_params(axis='x', labelsize = 10)
        if len(self.data[categorical_var].unique()) > 4:
            plt.xticks(rotation='vertical')

        plt.show()

    def density(self, categorical_var, numerical_var):
        """
            displays the density of the numerical variable.
            Each subpopulation should be represented by a separate curve
            on the graph.
            args:
                categorical_var (string)
                numerical_var (string)
        """
        sns.displot(self.data, x = numerical_var, hue=categorical_var, kind='kde')
        plt.show()

    def compare_histograms(self, categorical_var, numerical_var):
        """
            plots the numerical variable in a separate histogram for each category.
            args:
                categorical_var (string)
                numerical_var (string)
        """

        sns.displot(self.data, x=numerical_var, col=categorical_var)
        plt.show()