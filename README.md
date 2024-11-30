# Redbus-Data-Scraping-with-Selenium-Dynamic-Filtering-using-Streamlit

About RedBus:

RedBus is India’s largest online bus ticketing platform that has transformed bus travel in the country by bringing ease and convenience to millions of Indians who travel using buses. Founded in 2006, redBus is part of India’s leading online travel company MakeMyTrip Limited (NASDAQ: MMYT). By providing widest choice, superior customer service, lowest prices and unmatched benefits, redBus has served over 18 million customers. redBus has a global presence with operations across Indonesia, Singapore, Malaysia, Colombia and Peru apart from India.

About Project:

The "Redbus Data Scraping and Filtering with Streamlit Application" aims to revolutionize the transportation industry by providing a comprehensive solution for collecting, analyzing, and visualizing bus travel data. By utilizing Selenium for web scraping, this project automates the extraction of detailed information from Redbus, including bus routes, schedules, prices, and seat availability. By streamlining data collection and providing powerful tools for data-driven decision-making, this project can significantly improve operational efficiency and strategic planning in the transportation industry. I have took bus data of 10 states inc;uding their Private and Government bus Services.

Approach to the Project:

Data Scraping:

I have used Selenium Python to extract the data from redbus website(www.redbus.in). Selenium Python bindings provides a simple API to write functional/acceptance tests using Selenium WebDriver. Through Selenium Python API you can access all functionalities of Selenium WebDriver in an intuitive way. The extraction includes data such as Route Name, Route Links, Bus name, Bus Type, Start rating of the bus, Depature Time, Arrival Time, Price and Seat Availablity.

For installing selenium i have used : pip install selenium

Data Cleaning:

Once the data has been extracted, i used Pandas library from Python, to clean the extracted data in mutiple ways such as replacing the NULL values, changing the data types to the required format. Collaging the data into the single csv file.

Data Storage:
Store the scraped data in a SQL database.
Streamlit Application:
Develop a Streamlit application to display and filter the scraped data.
Implement various filters such as bustype, route, price range, star rating, availability.
Data Analysis/Filtering using Streamlit:
Use SQL queries to retrieve and filter data based on user inputs.
Use Streamlit to allow users to interact with and filter the data through the application.
