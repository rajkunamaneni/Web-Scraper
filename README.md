# Web-Scraper with MySQL

This program is a Web-Scraper that parses the contents with the existing URL via the library BeautifulSoup and consolidates the information by passing it to the MySQL server. This program will also create the table via `create_table.py` and drop the table if it already exists. The program also will log information for debugging and error handling. For a quick start, run `create_table.py` and run `scraper.py`.  

## Required Library 

This program uses BeautifulSoup for parsing. Download the [latest package](https://pypi.org/project/beautifulsoup4/). This program also requires an environment to host the MySQL server. I personally used [Clever-Cloud](https://www.clever-cloud.com) as it is accessible. 

## Build

General build, run `python3 'program_name'`.

## Run

 - Create Table with `python3 create_table.py`.

 - Run Web-Scraper with `python3 scraper.py`.

## Issues

The program currently has no documented issues.
