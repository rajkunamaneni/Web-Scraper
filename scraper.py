from bs4 import BeautifulSoup as bsoup
import requests
import MySQLdb
from log import Logger

def connect():
    #install mysql with "brew install mysql"
    #start server with "brew services start mysql"
    #end server with "brew services stop mysql"

    #tested with Sequel Pro
    HOST = "localhost"
    USERNAME = "test_user"
    PASSWORD = ""
    DATABASE = "test_sample"

def request():
    #scrape the website 
    url = "https://howpcrules.com/sample-page-for-web-scraping/"
    
    html = requests.get(url)
    
    parse = bsoup(html.text, "html.parser")

    info = parse.h3.text.strip()

    table_contents = parse.find("table", {"summary": "Basic data for the event"});
    findtd = table_contents.findAll('td')

    #table content 
    course = findtd[0].text.strip()
    lecturer = findtd[1].text.strip()
    number = findtd[2].text.strip()
    short_text = findtd[3].text.strip()
    choice_term = findtd[4].text.strip()
    hours_per_week_in_term = findtd[5].text.strip()
    expected_num_of_participants = findtd[6].text.strip()
    maximum_participants = findtd[7].text.strip()
    assignment = findtd[8].text.strip()
    lecture_id = findtd[9].text.strip()
    credit_points = findtd[10].text.strip()
    hyperlink = findtd[11].text.strip()
    language = findtd[12].text.strip()

    dates_table = read.find_all("table", {"summary": "Overview of all event dates"});

    #parse content of dates table
    for i in dates_table:
        for j in i.select("tr"):
            cell = j.findAll("td")
            if (len(j) > 0):
                #split the table
                duration = cell[0].text.split("to")
                start_date = duration[0].strip()
                end_date = duration[1].strip()
                day = cell[1].text.strip()
                time = cell[2].text.split("to")
                start_time = time[0].strip()
                end_time = time[1].strip()
                frequency = cell[3].text.strip()
                room = cell[4].text.strip()
                lecturer_for_date = cell[5].text.strip()
                status = cell[6].text.strip()
                remarks = cell[7].text.strip()
                cancelled_on = cell[8].text.strip()
                max_participants = cell[9].text.strip()



if __name__=='__main__':

    connect()
    request()

