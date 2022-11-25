"""
Allysa Peredo & J.R. Lim
CSE 163 Section AI

This file takes in the two separate datasets we have and cleans them before
merging them into a single dataset to be used for the rest of our data
analysis process in the "board_game.py" file.
"""


import pandas as pd


class CleaningData():

    def __init__(self, DATASET_1, DATASET_2):
        """
        This function initalizes the two datasets.
        """
        self._DATASET_1 = DATASET_1
        self._DATASET_2 = DATASET_2
        self._MERGED_DATA = {}

    def clean_data(self):
        """
        This function "cleans" the data by selecting specific columns of
        interest between the two datasets and combines them into a single
        dataset. Certain columns are renamed for consistency and only certain
        values from each column are kept. All NaN and NA values are also
        replaced.
        """
        # takes out columns that we don't want to include in merged data
        self._DATASET_1 = self._DATASET_1.drop(
            self._DATASET_1.columns[12], axis=1)
        self._DATASET_2 = self._DATASET_2.drop(self._DATASET_2.columns[[
            0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 13, 14, 15, 16,
            17, 18, 19]], axis=1)
        self._DATASET_2.columns = ['Geek Rating',
                                   "Number of Voters"]  # renames columns
        self._MERGED_DATA = pd.concat(
            [self._DATASET_1, self._DATASET_2], axis="columns")
        mask1 = self._MERGED_DATA['Geek Rating'] > 0
        self._MERGED_DATA = self._MERGED_DATA[mask1]
        mask2 = self._MERGED_DATA['Year'] > 1000
        self._MERGED_DATA = self._MERGED_DATA[mask2]
        self._MERGED_DATA = self._MERGED_DATA.fillna(0)

    def return_data(self):
        """
        This function returns the merged dataset.
        """
        return self._MERGED_DATA
