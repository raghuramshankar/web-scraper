# Use urllib and Beautiful soup libraries
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup


def write2csv(games, ori_price, dis_price):
    for game, ori_price, dis_price in zip(games, ori_prices, dis_prices):
        game = game.string
        ori_price = ori_price.string.replace(',', '.')
        dis_price = dis_price.string.replace(',', '.')
        f.write(game + ',' + ori_price + ',' + dis_price + '\n')


# URL to grab
myurl = 'https://store.steampowered.com/specials#p=0'
# Opening up the connection
uClient = uReq(myurl)
# Reading the raw HTML file and storing it
pageHTML = uClient.read()
# Closing the connection
uClient.close()

# Use BeautifulSoup to parse it
pageSoup = soup(pageHTML, "html.parser")

games = pageSoup.find_all("div", {"class": "tab_item_name"})
ori_prices = pageSoup.find_all(
    "div", {"class": "discount_original_price"})
dis_prices = pageSoup.find_all(
    "div", {"class": "discount_final_price"})

# Open a csv file
fileName = 'steam.csv'
f = open(fileName, "w")

# Headers
headers = "Game Title, Original Price, Discounted Price\n"

# Write first line
f.write(headers)

write2csv(games, ori_prices, dis_prices)

f.close()
