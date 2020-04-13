# Use urllib and Beautiful soup libraries
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup


def write2csv(titles):
    for title in zip(titles):
        title = title.string
        f.write(title + '\n')


# URL to grab
myurl = 'https://www.linkedin.com/jobs/search?location=germany&trk=public_jobs_jobs-search-bar_search-submit&f_JT=I&currentJobId=1822520184&position=3&pageNum=0&redirect=false'
# Opening up the connection
uClient = uReq(myurl)
# Reading the raw HTML file and storing it
pageHTML = uClient.read()
# Closing the connection
uClient.close()

# Use BeautifulSoup to parse it
pageSoup = soup(pageHTML, "html.parser")

# Open a csv file
fileName = 'linkedin.csv'
f = open(fileName, "w")

# Headers
headers = "Title\n"

# Write first line
f.write(headers)

links = pageSoup.find_all("a", {"class": "result-card__full-card-link"})

titles = pageSoup.find_all("h1", {"class": "topcard__title"})
write2csv(titles)

f.close()
