# Ariel Ashkenazy 208465096

import pandas as pd

""" the class reads the data that in the given csv file,
    and perform various functions on it, using pandas library. """
class myData:
    def __init__(self, path) -> None:
        self.data = pd.read_csv(path)

    """ given a height x and a height y (x<y),
        the function returns the number of players that their height is between x and y """
    def num_players_height(self, x, y):
        all_heights = self.data.loc[:, "height_cm"]

        # x should be smaller than y, so if x>y we swap them and get x<y as wanted.
        # enforce x<y
        if x > y:
            temp = y
            y = x
            x = temp

        num_of_players = 0
        for height in all_heights:
            if x <= height <= y:
                num_of_players += 1

        return num_of_players

    """ the function receives a year input and returns a dataframe,
        with 'short_name' and 'club_name' of players born in input year """
    def df_birthyear(self, year):
        # the 'dob' column is of 'datetime' data type (e.g. 24-06-87)
        # extract the year from the dob column, so we can check specifically on a chosen year
        self.data['year'] = pd.DatetimeIndex(self.data['dob']).year

        # Select only the rows where the 'year' column is equal to the input year
        input_year_players_df = self.data[self.data['year'] == year]
        name_and_club_df = input_year_players_df[["short_name", "club_name"]]
        return name_and_club_df

    """ given two columns (column1, column2) and an integer k,
        the function returns a list of the names of the first k players with highest values in column1.
        that list is sorted in ascending order, by the values in column2"""
    def list_sorted(self, column1, column2, k):
        # get k first players with the top values in column1
        column1_values_and_names = self.data[[column1, column2, "short_name"]]
        column1_sorted = column1_values_and_names.sort_values(by=column1, ascending=False)
        # sort in ascending order and extract the last (tail) k records
        top_k_column1 = column1_sorted.head(k)
        # sort k players according to column2
        column2_sorted = top_k_column1.sort_values(by=column2)
        return list(column2_sorted["short_name"])

    """ given years x and y (x<y), the function will return a list of tuples, 
        where each tuple holds the year and the number of players who were born in it.
        this function uses 'df_birthyear' function """
    def tuples_players_by_year(self, x, y):
        # enforce x<y
        if x > y:
            temp = y
            y = x
            x = temp

        tuples_list = []
        # for every year from x to y, run 'df_birthyear' function to get number of players born in that year
        for year in range(x, y+1):
            temp_df = self.df_birthyear(year)
            count = len(temp_df.index)
            tuples_list.append((year, count))

        return tuples_list

    """ given column name and player name,
        return the mean and the standard deviation of column values, for the given player name """
    def mean_std(self, column, player_name):
        column_and_names = self.data[[column, "long_name"]]

        # Select only the rows where string 'long_name' starts with substring 'player_name'
        column_and_player = column_and_names[column_and_names['long_name'].str.startswith(player_name)]

        mean = column_and_player[column].mean()
        std = column_and_player[column].std()
        return mean, std

    """ given a column name, return the most frequent value in that column"""
    def max_players(self, column):
        column_values = self.data[column]
        return column_values.value_counts().idxmax()


# if __name__ == '__main__':
#     md = myData("players_22.csv")
    # print("1:", "\n", md.num_players_height(180, 190), "\n")
    # print("2:", "\n", md.df_birthyear(1980), "\n")
    # print("3:", "\n", md.list_sorted("weight_kg", "movement_sprint_speed", 10), "\n")
    # print("4:", "\n", md.tuples_players_by_year(1980, 1990), "\n")
    # print("5:", "\n", md.mean_std("wage_eur", "Adriano"), "\n")
    # print("6:", "\n", md.max_players("nationality_name"), "\n")
