from lxml import html
import requests

page = requests.get('http://www.nhl.com/scores/htmlreports/20162017/PL020714.HTM')
tree = html.fromstring(page.content)

#Gets goals for game
#Work on formatting
goals = tree.xpath('//td[@class="goal + bborder"]/text()')

print 'Goals: ', goals
