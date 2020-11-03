from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd


def BBRef_player_stats_scraper(year_start, year_end):
    # create an empty list for the combined stats
    complete_stats = []

    # assign the year to start loop at
    year = year_start

    # number of years after the first year to be considered (add one to compensate for range function)
    delta = year_end - year_start + 1

    # start loop
    for x in range(delta):

        # URL page function is scraping from
        url = "https://www.basketball-reference.com/leagues/NBA_{}_per_game.html".format(year)

        # HTML for above url
        html = urlopen(url)
        soup = BeautifulSoup(html)

        # use findALL() to get the column headers
        soup.findAll('tr', limit=2)

        # use getText()to extract the text into a list
        headers = [th.getText() for th in soup.findAll('tr', limit=2)[0].findAll('th')]

        # exclude the first column as we will not need the ranking order from Basketball Reference for the analysis
        headers = headers[1:]
        # avoid the first header row
        rows = soup.findAll('tr')[1:]
        player_stats = [[td.getText() for td in rows[i].findAll('td')]
                        for i in range(len(rows))]

        # loop through players adding year for stats and then appending each player to the complete list
        for player in player_stats:
            player.insert(0, year)
            complete_stats.append(player)

        # move to the next year and loop again
        year = year + 1

    # add in the year column header
    headers.insert(0, 'year')

    # create a dataframe from the complete list
    stats = pd.DataFrame(complete_stats, columns=headers)

    return stats

df = BBRef_player_stats_scraper(2010, 2020)

df.to_csv('data/bbref_df.csv')
