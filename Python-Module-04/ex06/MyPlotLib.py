import seaborn as sns
import matplotlib.pyplot as plt

class MyPlotLib:
    """
         class implements different plotting methods, each of which
         take two arguments:
         Args:
            • a pandas.DataFrame which contains the dataset,
            • a list of feature names.
           
            • density(data, features): plots the density curve
                of each numerical feature in the list,
            • pair_plot(data, features): plots a matrix of subplots (also called scatter plot
                matrix). On each subplot shows a scatter plot of one numerical variable against
                another one. The main diagonal of this matrix shows simple histograms.
            • box_plot(data, features): displays a box plot for each numerical variable in the
                dataset.
    """
    def __init__(self):
        pass

    def histogram(self, data, features):
        """
            histogram(data, features): plots one histogram for
                each numerical feature in the list,
        """
        nb = len(features)
        pos = 1
        plt.figure(1)
        for feature in features:
            plt.subplot(1, nb, pos)
            plt.gcf().subplots_adjust(wspace = 0.5)
            plt.hist(x=data[feature])
            plt.title(feature)
            pos += 1
        plt.show()

    def density(self, data, features):
        """
             plots the density curve of each numerical feature in the list

        """
        sns.displot(data[features], kind='kde', label=features)
        plt.show()

    def pair_plot(self, data, features):
        """
         plots a matrix of subplots (also called scatter plot matrix).
         On each subplot shows a scatter plot of one numerical variable
         against another one. The main diagonal
         of this matrix shows simple histograms.
        """
        sns.pairplot(data[features],diag_kind="hist")
        plt.show()

    def box_plot(self, data, features):
        """
            displays a box plot for each numerical variable in the dataset.

        """
        data.head()
        sns.boxplot( data[features] , palette="Blues", width=0.3)
        plt.show()

    def imputation(self, data, numerique = False, threshold = 0.7):
        """
            Drop columns and rows missing value
        """
        #Dropping columns with missing value rate higher than threshold
        data = data[data.columns[data.isnull().mean() < threshold]]

        #Dropping rows with missing value rate higher than threshold
        data = data.loc[data.isnull().mean(axis=1) < threshold]