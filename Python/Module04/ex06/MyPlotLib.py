import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


class MyPlotLib:

    # features is a list of strings representing the names of numerical features/columns in the DataFrame
    # for which all graph frunctions are to be plotted.

    def histogram(self, data, features):
        # print(data[features])

        # data[features] extracts a new DataFrame that contains only the columns specified in the features list
        # hist(...) is a method that generates histograms for each numerical column in the DataFrame
        # bin specifies the number of intervals for the histogram
        # figsize sets the size of the entire graph figure (width, height) in inches
        # layout specifies the layout of subplots in the figure (rows, columns)
        # in our case, the layout will be arranged in a single row with two columns (1, len(features))
        # meaning there will be two histogram side by side
        data[features].hist(bins=10, edgecolor='black', figsize=(10, 5), layout=(1, len(features)))
        plt.show()


    def density(self, data, features):
        plt.figure(figsize=(10, 5))
        for feature in features:
            # kdeplot generates a density graph for each feature
            sns.kdeplot(data[feature], label=feature)
        # adds legend to each plot to know which plot corresponds to which feature 
        plt.legend()
        plt.show()
    

    def pair_plot(self, data, features):
        # generate pair plot
        # diag_kws={'bins': 10} instruct to create histograms with 10 bins for each diagonal plot
        sns.pairplot(data[features], diag_kws={'bins': 10})
        plt.show()
    

    def box_plot(self, data, features):
        # kind='box' specifies that box plots are to be created
        data[features].plot(kind='box', figsize=(10, 5))
        plt.show()


    
if __name__ == "__main__":

    data = pd.read_csv('../data/athlete_events.csv')
    mpl = MyPlotLib()
    features = ['Height', 'Weight']

    mpl.histogram(data, features)
    mpl.density(data, features)
    mpl.pair_plot(data, features)
    mpl.box_plot(data, features)
