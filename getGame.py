from lxml import html
import requests
import numpy as np

#Gets url for a given game
#Takes season formatted as yearStart yearEnd concatenated
#Takes 4 digit game number
def getURL(season, gameNumber):
    url = "http://www.nhl.com/scores/htmlreports/"
    if season[0:4] != str(int(season[4:8]) - 1):
        raise ValueError('Incorrect season formatting')
    url += season
    url += "/PL02"
    if len(gameNumber) != 4:
        raise ValueError('Incorrect game number formatting')
    url += gameNumber
    url += ".HTM"
    return url

def getGame(season, gameNumber):
    url = getURL(season, gameNumber)
    page = requests.get(url)
    if page.status_code == 404:
        return None
    html_content = html.fromstring(page)
    return html_content

#returns an array of games for the season
#def getSeason(season):

print(getURL('20162017', '0156'))
print(getURL('20172015', '01442'))
print(getURL('20162017', '011115'))
