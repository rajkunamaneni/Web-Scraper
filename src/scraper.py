from bs4 import BeautifulSoup as bsoup
import requests
import MySQLdb
from log import Logger

def main():
    #set user info for mysql login

    for i in range(0, 2):
        #scrape the website 
        url = "https://howpcrules.com/sample-page-for-web-scraping/"
        
        html = requests.get(url)
        
        parse = bsoup(html.text, "html.parser")

        name_of_class = parse.h3.text.strip()

        table_contents = parse.find("table", {"summary": "Basic data for the event"});
        findtd = table_contents.findAll('td')

        #table content and filter
        type_of_course = findtd[0].text.strip()
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

        db = MySQLdb.connect(HOST, USERNAME, PASSWORD, DATABASE)

        cursor = db.cursor()
        sql = "INSERT INTO classes(name_of_class, type_of_course, lecturer, number, short_text, choice_term, hours_per_week_in_term, expected_num_of_participants, maximum_participants, assignment, lecture_id, credit_points, hyperlink, language, created_at) VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', {})".format(name_of_class, type_of_course, lecturer, number, short_text, choice_term, hours_per_week_in_term, expected_num_of_participants, maximum_participants, assignment, lecture_id, credit_points, hyperlink, language, 'NOW()')
        try:
            # fill each set of rows with data
            cursor.execute(sql)
            db.commit()

        except:
            # Rollback in case there is any error
            db.rollback()
            #get the just inserted class id
            sql = "SELECT LAST_INSERT_ID()"
        try:
            cursor.execute(sql)
            # Get the result
            result = cursor.fetchone()
            # Set the class id to the just inserted class
            class_id = result[0]
        except:
            #error happened :(
            db.rollback()
            db.close()
            class_id = -1
            
        dates_tables = parse.find_all("table", {"summary": "Overview of all event dates"});
        #Iterate through the tables
        for table in dates_tables:
            #Iterate through the rows inside the table
            for row in table.select("tr"):
                #Get all cells inside the row
                cells = row.findAll("td")
                #check if there is at least one td cell inside this row
                if(len(cells) > 0):
                    #get all the different data from the table's tds
                    #Split this cell into two different parts seperated by 'to' in order to have a start_date and an end_date.
                    duration = cells[0].text.split("to")
                    start_date = duration[0].strip()
                    end_date = duration[1].strip()
                    day = cells[1].text.strip()
                    #Split this cell into two different parts seperated by 'to' in order to have a start_time and an end_time.
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
                    # Open database connection
                    db = MySQLdb.connect(HOST, USERNAME, PASSWORD, DATABASE)
                    # prepare a cursor object using cursor() method
                    cursor = db.cursor()
                    # Prepare SQL query to INSERT a record into the database.
                    sql = "INSERT INTO events(class_id, start_date, end_date, day, start_time, end_time, frequency, room, lecturer_for_date, status, remarks, cancelled_on, max_participants, created_at) VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', {})".format(class_id, start_date, end_date, day, start_time, end_time, frequency, room, lecturer_for_date, status, remarks, cancelled_on, max_participants, 'NOW()')
                    try:
                    # Execute the SQL command
                    cursor.execute(sql)
                    # Commit your changes in the database
                    db.commit()
                    except:
                    # Rollback in case there is any error
                    db.rollback()
                    # disconnect from server
                    db.close()

if __name__ == "__main__":
    main()
