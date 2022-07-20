from bs4 import BeautifulSoup as bsoup
import requests
import MySQLdb
from log import Logger

'''
Parse through URL and store the content in MySQL database
Logging visible through logs.log
'''
def main():
    #set user info for mysql login
    HOST = "localhost"
    USERNAME = "test_user"
    PASSWORD = ""
    DATABASE = "test_sample"

    #create log file for debugging
    logger = Logger().logger

    #website to scrape and store 
    url_to_scrape = 'https://howpcrules.com/sample-page-for-web-scraping/'
    
    #use https get request to get the html info to parse
    plain_html_text = requests.get(url_to_scrape)
    
    #read the html content (use prettify for easier read)
    soup = bsoup(plain_html_text.text, "html.parser")

    logger.info("\n*** Read HTML succeeded. ***\n")
    
    #Get the name of the table
    name_of_class = soup.h3.text.strip()

    basic_data_table = soup.find("table", {"summary": "Basic data for the event"});
   
    basic_data_cells = basic_data_table.findAll('td')

    #strip the data from the table
    type_of_course = basic_data_cells[0].text.strip()
    lecturer = basic_data_cells[1].text.strip()
    number = basic_data_cells[2].text.strip()
    short_text = basic_data_cells[3].text.strip()
    choice_term = basic_data_cells[4].text.strip()
    hours_per_week_in_term = basic_data_cells[5].text.strip()
    expected_num_of_participants = basic_data_cells[6].text.strip()
    maximum_participants = basic_data_cells[7].text.strip()
    assignment = basic_data_cells[8].text.strip()
    lecture_id = basic_data_cells[9].text.strip()
    credit_points = basic_data_cells[10].text.strip()
    hyperlink = basic_data_cells[11].text.strip()
    language = basic_data_cells[12].text.strip()

    # Open database connection
    db = MySQLdb.connect(HOST, USERNAME, PASSWORD, DATABASE)
   
    logger.info("\n*** connection to server succeeded. ***\n")  

    # prepare a cursor object using cursor() method
    cursor = db.cursor()
    sql = "INSERT INTO classes(name_of_class, type_of_course, lecturer, number, short_text, choice_term, hours_per_week_in_term, expected_num_of_participants, maximum_participants, assignment, lecture_id, credit_points, hyperlink, language, created_at) VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', {})".format(name_of_class, type_of_course, lecturer, number, short_text, choice_term, hours_per_week_in_term, expected_num_of_participants, maximum_participants, assignment, lecture_id, credit_points, hyperlink, language, 'NOW()')
    try:
        cursor.execute(sql)
        db.commit()
        logger.info("\n*** Insert was successful. ***\n")
    except:
        db.rollback()
        logger.error("\n*** Insert was failed. ***\n")
        
    sql = "SELECT LAST_INSERT_ID()"
    try:
        cursor.execute(sql)
        result = cursor.fetchone()
        class_id = result[0]
    except:
        #error happened so end program :(
        db.rollback()
        db.close()
        logger.error("\n*** Program Closed with ERROR ***\n")
        class_id = -1

    #Get the tables where the dates are written.
    dates_tables = soup.find_all("table", {"summary": "Overview of all event dates"});

    #move through multiple tables
    for table in dates_tables:
        for row in table.select("tr"):
            cells = row.findAll("td")
            if(len(cells) > 0):
                duration = cells[0].text.split("to")
                start_date = duration[0].strip()
                end_date = duration[1].strip()
                day = cells[1].text.strip()
                time = cells[2].text.split("to")
                start_time = time[0].strip()
                end_time = time[1].strip()
                frequency = cells[3].text.strip()
                room = cells[4].text.strip()
                lecturer_for_date = cells[5].text.strip()
                status = cells[6].text.strip()
                remarks = cells[7].text.strip()
                cancelled_on = cells[8].text.strip()
                max_participants = cells[9].text.strip()
                
                #Save event data to database
                db = MySQLdb.connect(HOST, USERNAME, PASSWORD, DATABASE)
                cursor = db.cursor()
                
                sql = "INSERT INTO events(class_id, start_date, end_date, day, start_time, end_time, frequency, room, lecturer_for_date, status, remarks, cancelled_on, max_participants, created_at) VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', {})".format(class_id, start_date, end_date, day, start_time, end_time, frequency, room, lecturer_for_date, status, remarks, cancelled_on, max_participants, 'NOW()')
                try:
                    logger.info("\n*** Insert was successful. ***\n")
                    cursor.execute(sql)
                    db.commit()
                except:
                    db.rollback()
                    logger.error("\n*** Error ***\n")
                
                logger.info("\n*** Insert Ended ***\n")
                db.close()

    logger.info("\n*** Program Closed ***\n")

if __name__ == "__main__":
    main()
