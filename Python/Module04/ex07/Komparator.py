import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


class Komparator:

    def __init__(self, df):
        self.df = df

    
    def compare_box_plots(self, categorical_var, numerical_var):

        categories = self.df[categorical_var].unique()
        num_categories = len(categories)
        # subplots() creates a figure with a row of subplots assigned to axes
        fig, axes = plt.subplots(1, num_categories, figsize=(5 * num_categories, 6), sharey=True)
        # print(axes)

        for i, category in enumerate(categories):
            # create dataframe of the current category
            subset = self.df[self.df[categorical_var] == category]
            # boxplot(data, x, y) generates a box plot for the numerical variable in the current category
            # axes[i] specifies which subplot to draw the box plot on
            sns.boxplot(y=subset[numerical_var], ax=axes[i])
            axes[i].set_title(f'{categorical_var}: {category}')
            axes[i].set_ylabel(numerical_var)
            # print(axes)
        plt.show()


    def density(self, categorical_var, numerical_var):
        plt.figure(figsize=(10, 6))
        categories = self.df[categorical_var].unique()
        for category in categories:
            # create dataframe of the current category
            subset = self.df[self.df[categorical_var] == category]
            # kdeplot generates a density graph for each feature
            # label=category sets up a legend for each category that will be displayed by plt.legend()
            sns.kdeplot(subset[numerical_var], label=category)
        plt.legend(title=categorical_var)
        plt.show()
    

    def compare_histograms(self, categorical_var, numerical_var):
        categories = self.df[categorical_var].unique()
        num_categories = len(categories)
        fig, axes = plt.subplots(1, num_categories, figsize=(5 * num_categories, 6), sharey=True)
    
        for i, category in enumerate(categories):
            subset = self.df[self.df[categorical_var] == category]
            axes[i].hist(subset[numerical_var], bins=30, edgecolor='black')
            axes[i].set_title(f'{categorical_var}: {category}')
            axes[i].set_xlabel(numerical_var)
            axes[i].set_ylabel('Frequency')
        plt.show()


if __name__ == "__main__":

    df = pd.read_csv('../data/athlete_events.csv')
    komparator = Komparator(df)

    # recommend to not display all at once
    komparator.compare_box_plots('Sex', 'Height')
    komparator.density('Sex', 'Height')
    komparator.compare_histograms('Sex', 'Height')

