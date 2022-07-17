from bs4 import BeautifulSoup as bsoup
import requests
import MySQLdb
from log import Logger

logger = Logger().logger
logger.debug("This log's level is 'DEBUG'")
logger.info("This log's level is 'info'")
logger.error("This log's level is 'error'")

def connect():
    HOST = "localhost"
    USERNAME = "scraping_user"
    PASSWORD = ""
    DATABASE = "scraping_sample"

def request():
    #scrape the website 
    url = "https://howpcrules.com/sample-page-for-web-scraping/"
    
    html = requests.get(url)
    
    read = bsoup(html.text, "html.parser")

    #print for debug
    print(read.prettify())

    #classinfo = bsoup.h3.text.string()

#    print(classinfo.prettify())
    


if __name__=='__main__':

    connect()
    request()

