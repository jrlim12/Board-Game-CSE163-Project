"""
Allysa Peredo & J.R. Lim
CSE 163 Section AI

This main file does all of our data analysis by plotting various graphs using
the Plotly library and implementing a training model that predicts the BGG
rating of a trial board game based on the given features. Each function
utilizes the cleaned, merged dataset from the "cleaning_data.py" file.
"""


import pandas as pd
from plotly import express as px
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from cleaning_data import CleaningData
from sklearn.metrics import mean_squared_error


def year_vs_bgg(MERGED_DATA):
    """
    This function takes in the merged dataset and plots two scatterplots,
    each using the release year of a board game, and what BGG rating it was
    given. The first chart only includes board games from before 1960, while
    the second displays games from 1961 and onwards.
    """
    mask1 = MERGED_DATA['Year'] <= 1960
    bef_1960 = MERGED_DATA[mask1]
    mask2 = MERGED_DATA['Year'] > 1960
    aft_1960 = MERGED_DATA[mask2]
    fig1 = px.scatter(bef_1960, x='Year', y='Geek Rating',
                      color='Geek Rating',
                      title="Year vs. Geek Rating (1000-1960)")
    fig1.show()
    fig2 = px.scatter(aft_1960, x='Year', y='Geek Rating',
                      color='Geek Rating',
                      title="Year vs. Geek Rating (1960-Present)")
    fig2.show()


def time_vs_bgg(MERGED_DATA):
    """
    This function takes in the merged dataset and plots the average play time
    versus the geek rating a board game received in a scatterplot.
    """
    fig = px.scatter(MERGED_DATA, x='Play Time', y='Geek Rating', log_x=True,
                     color='Geek Rating',
                     title="Play Time vs. Geek Rating")
    fig.show()


def age_vs_bgg(MERGED_DATA):
    """
    This function takes in the merged dataset and plots the recommended
    minimum age of a board game compared to what BGG rating it received
    in the form of a scatterplot.
    """
    fig = px.scatter(MERGED_DATA, x='Min Age', y='Geek Rating',
                     color='Geek Rating',
                     title="Min Age vs. Geek Rating")
    fig.show()


def complex_vs_bgg(MERGED_DATA):
    """
    This function takes in the merged dataset and plots the average
    complexity rating of a board game versus what BGG rating it received
    in the form of a scatterplot.
    """
    fig = px.scatter(MERGED_DATA, x='Complexity Average', y='Geek Rating',
                     color='Geek Rating',
                     title="Complexity Average vs. Geek Rating")
    fig.show()


def minplay_vs_bgg(MERGED_DATA):
    """
    This function takes in the merged dataset and plots the minimum player
    count of a board game versus the BGG rating it received in the form of
    a bar chart.
    """
    average = MERGED_DATA.groupby('Min Players', as_index=False)[
        'Geek Rating'].mean()
    fig = px.bar(average, x='Min Players', y='Geek Rating',
                 color='Geek Rating',
                 title="Minimum Players vs. Geek Rating")
    fig.show()


def maxplay_vs_bgg(MERGED_DATA):
    """
    This function takes in the merged dataset and plots a similar chart as
    the last function, except instead of the minimum player count versus
    BGG rating, it plots the manximum player count versus BGG rating. The
    resulting graph is in the form of a bar chart.
    """
    average = MERGED_DATA.groupby('Max Players', as_index=False)[
        'Geek Rating'].mean()
    fig = px.bar(average, x='Max Players', y='Geek Rating',
                 color='Geek Rating',
                 title="Maximum Players vs. Geek Rating")
    fig.show()


def bggrank_vs_users(MERGED_DATA):
    """
    This function takes in the merged dataset and plots the BGG ranks and
    amount of owners each board game has in a scatterplot. This helps
    visualize any possible correlations or relationships between the two
    variables.
    """
    MERGED_DATA['Owned Users'] = MERGED_DATA['Owned Users'].astype(int)
    fig = px.scatter(MERGED_DATA, y='BGG Rank', x='Owned Users',
                     log_x=True, title="BGG Rank vs. Owned Users")
    fig.show()


def bggrank_vs_rating_average(MERGED_DATA):
    """
    This function takes in the merged dataset and plots the BGG ranks and
    what average public rating each board game received in a scatterplot.
    Just as the last function, this helps visualize any possible correlations
    or relationships between the two variables.
    """
    fig = px.scatter(MERGED_DATA, x='BGG Rank', y='Rating Average',
                     title='BGG Rank vs. Public Rating Average')
    fig.show()


def domain_vs_bgg(MERGED_DATA):
    """
    This function takes in the merged dataset and plots each domain of board
    games and what the average BGG rating is for each domain in a bar chart.
    """
    mask = MERGED_DATA['Domains'] != '0'
    masked_data = MERGED_DATA[mask]
    average = masked_data.groupby('Domains', as_index=False)[
        'Geek Rating'].mean()
    fig = px.bar(average, x='Domains', y='Geek Rating',
                 title='Domain vs. Geek Rating')
    fig.show()


def year_vs_users(MERGED_DATA):
    """
    This function takes in the merged dataset and plots the sum of board game
    owners from each year and plots them in a bar chart to easily visualize
    the differences in owners per year.
    """
    mask = MERGED_DATA['Owned Users'] != 0
    masked_data = MERGED_DATA[mask]
    per_year = masked_data.groupby('Year', as_index=False)[
        'Owned Users'].sum()
    fig = px.bar(per_year, x='Year', y='Owned Users',
                 color='Year',
                 title='Release Year vs. Amount of Owners')
    fig.show()


def fit_and_predict(MERGED_DATA):
    """
    This function takes in the merged dataset and creates a model for
    predicting the Geek Rating of a board game based on the other features
    it is given. The mean squared error is returned.
    """
    MERGED_DATA = MERGED_DATA[['Year', 'Min Players', 'Max Players',
                               'Play Time', 'Min Age',
                               'Complexity Average', 'Geek Rating']]
    features = MERGED_DATA.loc[:, MERGED_DATA.columns != 'Geek Rating']
    features = pd.get_dummies(features)
    labels = MERGED_DATA['Geek Rating']
    features_train, features_test, labels_train, labels_test = \
        train_test_split(features, labels, test_size=0.2)
    model = DecisionTreeRegressor()
    model.fit(features_train, labels_train)
    train_pred = model.predict(features_test)
    print(mean_squared_error(train_pred, labels_test))


def main():
    """
    Main method runs each of our functions and declares the two datasets
    to be used in the data analysis of our project.
    """
    DATASET_1 = pd.read_csv(
        r'C:/Users/jrlim/Documents/UW/2021-2022/CSE 163/VS Projects'
        r'/final project board game/The_Larxel_BBG_Dataset.csv',
        encoding='unicode_escape')
    DATASET_2 = pd.read_csv(
        r'C:/Users/jrlim/Documents/UW/2021-2022/CSE 163/VS Projects'
        r'/final project board game/Pantherson_Data_Set.csv',
        encoding='unicode_escape')
    merge = CleaningData(DATASET_1, DATASET_2)
    merge.clean_data()
    MERGED_DATA = merge.return_data()
    print('Main runs, no errors found!')
    year_vs_bgg(MERGED_DATA)
    time_vs_bgg(MERGED_DATA)
    age_vs_bgg(MERGED_DATA)
    complex_vs_bgg(MERGED_DATA)
    minplay_vs_bgg(MERGED_DATA)
    maxplay_vs_bgg(MERGED_DATA)
    bggrank_vs_users(MERGED_DATA)
    bggrank_vs_rating_average(MERGED_DATA)
    domain_vs_bgg(MERGED_DATA)
    year_vs_users(MERGED_DATA)
    fit_and_predict(MERGED_DATA)
    print(MERGED_DATA.keys())  # prints out names of each column (14 columns)
    print('Main runs, no errors found!')


if __name__ == '__main__':
    main()
