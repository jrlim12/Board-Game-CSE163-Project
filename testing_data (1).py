"""
Allysa Peredo & J.R. Lim
CSE 163 Section AI

This file implements all of our test functions used to verify that our
functions in our main file, "board_game.py", work correctly.
"""


import pandas as pd
from board_game import year_vs_bgg
from board_game import time_vs_bgg
from board_game import age_vs_bgg
from board_game import complex_vs_bgg
from board_game import minplay_vs_bgg
from board_game import maxplay_vs_bgg
from board_game import domain_vs_bgg
from board_game import bggrank_vs_rating_average
from board_game import bggrank_vs_users


def testing_year(test):
    """
    This function tests our "year_vs_bgg" function to make sure it graphs
    values properly.
    """
    mask1 = test['Year'] <= 1960
    bef_1960 = test[mask1]
    mask2 = test['Year'] > 1960
    aft_1960 = test[mask2]
    print(bef_1960)
    print(aft_1960)


def testing_min_player(test):
    """
    This function tests our "minplay_vs_bgg" function to make sure it graphs
    values properly.
    """
    average = test.groupby('Min Players', as_index=False)[
        'Geek Rating'].mean()
    print(average)
    if average.iat[2, 1] == 5.691795:
        print('Nice!')


def testing_max_player(test):
    """
    This function tests to our "maxplay_vs_bgg" function to make sure it
    graphs values properly.
    """
    average = test.groupby('Max Players', as_index=False)[
        'Geek Rating'].mean()
    print(average)
    if average.iat[4, 1] == 5.67217:
        print('Nice!')


def testing_domain(test):
    """
    This function tests our "domain_vs_bgg" function to make sure it graphs
    values properly.
    """
    print(test['Domains'])
    test = test.fillna(0)
    mask = test['Domains'] != 0
    masked_data = test[mask]
    print(masked_data['Domains'])


def main():
    """
    Main method runs all of our functions in this file.
    """
    test = pd.read_csv(
        r'C:/Users/jrlim/Documents/UW/2021-2022/CSE 163/VS Projects'
        r'/final project board game/test_data.csv',
        encoding='unicode_escape')
    year_vs_bgg(test)
    time_vs_bgg(test)
    age_vs_bgg(test)
    complex_vs_bgg(test)
    minplay_vs_bgg(test)
    maxplay_vs_bgg(test)
    domain_vs_bgg(test)
    bggrank_vs_rating_average(test)
    bggrank_vs_users(test)
    testing_year(test)
    testing_min_player(test)
    testing_max_player(test)
    testing_domain(test)


if __name__ == '__main__':
    main()
