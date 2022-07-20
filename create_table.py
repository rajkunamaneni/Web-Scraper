import mysql.connector
from log import Logger

'''
Check Tables are created or Drop the Table when
it already exists. 
Logging visible through logs.log
'''
def create_table():
    #establishing the connection
    HOST = "localhost"
    USERNAME = "test_user"
    PASSWORD = ""
    DATABASE = "test_sample"

    db = mysql.connector.connect(user=USERNAME, password=PASSWORD, host=HOST, database=DATABASE)

    logger = Logger().logger #log for error handling
    logger.info("\n*** connection to server succeeded. ***\n")

    #Creating a cursor object using the cursor() method
    cursor = db.cursor()

    #check if table need to be dropped if it already exists
    cursor.execute("SHOW TABLES")
    logger.info("\n*** Check Table Exist ***\n")
    print(cursor.fetchall())

    #Drop table if Exist for either classes or events
    cursor.execute("SET FOREIGN_KEY_CHECKS=0")
    cursor.execute("DROP TABLE IF EXISTS classes")
    cursor.execute("SET FOREIGN_KEY_CHECKS=1")

    cursor.execute("SET FOREIGN_KEY_CHECKS=0")
    cursor.execute("DROP TABLE IF EXISTS events")
    cursor.execute("SET FOREIGN_KEY_CHECKS=1")

    #check table again
    logger.info("\n*** Check Table are Dropped ***\n")
    cursor.execute("SHOW TABLES")
    
    print(cursor.fetchall())
    
    logger.info("\n*** Dropped Tables ***\n")

    sql1 = '''CREATE TABLE `classes` (
 `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
 `name_of_class` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
 `type_of_course` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
 `lecturer` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
 `number` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
 `short_text` text COLLATE utf8_unicode_ci DEFAULT NULL,
 `choice_term` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
 `hours_per_week_in_term` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
 `expected_num_of_participants` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
 `maximum_participants` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
 `assignment` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
 `lecture_id` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
 `credit_points` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
 `hyperlink` text COLLATE utf8_unicode_ci DEFAULT NULL,
 `language` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
 `created_at` timestamp NULL DEFAULT NULL,
 PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;'''

    cursor.execute(sql1)
    logger.info("\n*** `classes` Table Created ***\n") 
    
    sql2 = '''CREATE TABLE `events` (
 `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
 `class_id` int(10) unsigned NOT NULL,
 `start_date` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
 `end_date` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
 `day` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
 `start_time` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
 `end_time` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
 `frequency` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
 `room` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
 `lecturer_for_date` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
 `status` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
 `remarks` text COLLATE utf8_unicode_ci,
 `cancelled_on` text COLLATE utf8_unicode_ci,
 `max_participants` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
 `created_at` timestamp NULL DEFAULT NULL,
 PRIMARY KEY (`id`),
 KEY `events_class_id_foreign` (`class_id`),
 CONSTRAINT `events_class_id_cascade` FOREIGN KEY (`class_id`) REFERENCES `classes` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;'''

    cursor.execute(sql2)
    logger.info("\n*** `events` Table Created ***\n")
    
    #Closing the connection
    db.close()
    logger.info("\n*** Program create_tables.py Closed ***\n")

if __name__ == "__main__":
    create_table()

