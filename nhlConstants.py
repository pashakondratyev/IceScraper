import datetime
#List of seasons available
#Important: from 2007-2008 format switched
#Based on when Stanley Cup Playoffs would be held 
def SeasonAvailable(year):
    now = datetime.datetime.now()
    #HTML Reports only has from 2003
    if year < 2004: 
        return False
    if year == 2005:
        return False
    if year <= (now.year + 1):
        return True
    else:
        return False

availableSeasons = [
        "2003",
        "2004",
        #2005 was a lockout year
        "2006",
        "2007",
        "2008",
        "2009",
        "2010",
        "2011",
        "2012",
        "2013",
        "2014",
        "2015",
        "2016",
        "2017"
]

#Dictionary of seasons + games played

#Dictionary of preseason + games played

#Dictionary of postseason + games played

#Dictionary of Team names

