from lxml import html
import requests

#formatting for page is 
#'http://www.nhl.com/scores/htmlreports/yearsOfSeason/PL02####.htm')
#where #### is the game number
page = requests.get('http://www.nhl.com/scores/htmlreports/20162017/PL021000.HTM')
tree = html.fromstring(page.content)

#Gets goals for game
#Work on formatting
goals = tree.xpath('//td[@class="goal + bborder"]/text()')

if page.status_code == 404:
    print(404)
        
print('Goals: ', goals)
