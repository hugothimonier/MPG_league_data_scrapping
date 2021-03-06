#!/usr/bin/python
import sys
import argparse
sys.path.append('./utilities/')

from MPG_Scraper import MpgScraper


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="MPG League Data Scrapping")

    ### scrapper options
    parser.add_argument('-user',           type=str,     default=None,              help='username in the form of email',     required=True) 
    parser.add_argument('-pwd',            type=str,     default=None,              help='corresponding password',            required=True)
    parser.add_argument('-nb_gw',          type=int,     default=None,              help='Number of games played',            required=True)
    parser.add_argument('-nb_teams',       type=int,     default=10,                help='Number of teams in the league',     required=True) 
    parser.add_argument('-first_season',   type=int,     default=1,                 help='Season number',                     required=True)
    parser.add_argument('-last_season',    type=int,     default=1,                 help='Season number',                     required=True)
    parser.add_argument('-team_name',      type=str,     default=None,              help='Name of your team',                 required=False)
    parser.add_argument('-league_name',    type=str,     default=None,              help='league to scrape',                  required=True) 
    parser.add_argument('-json_file',      type=str,     default='data_MPG_league', help='name of json file',                 required=True)
    parser.add_argument('-driver',         type=str,     default='Firefox',         help='Chrome or Firefox',                 required=False)

    opts = parser.parse_args()

    mpg_scrapper = MpgScraper(user=opts.user, pwd=opts.pwd, nb_gw=opts.nb_gw, 
                              nb_gamers=opts.nb_teams, first_season=opts.first_season, last_season=opts.last_season,
                              user_team_name=opts.team_name, driver=opts.driver)
    data = mpg_scrapper.get_league_data(league_name=opts.league_name)
    data.to_json('./{}.json'.format(opts.json_file))

    print('Done ! Data was saved as json file as {}.json'.format(opts.json_file))