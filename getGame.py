from lxml import html
import requests

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

print(getURL('20162017', '0156'))
print(getURL('20172015', '01442'))
print(getURL('20162017', '011115'))
