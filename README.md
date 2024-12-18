**About RedBus:**

RedBus is India’s largest online bus ticketing platform that has transformed bus travel in the country by bringing ease and convenience to millions of Indians who travel using buses. Founded in 2006, redBus is part of India’s leading online travel company MakeMyTrip Limited (NASDAQ: MMYT). By providing widest choice, superior customer service, lowest prices and unmatched benefits, redBus has served over 18 million customers. redBus has a global presence with operations across Indonesia, Singapore, Malaysia, Colombia and Peru apart from India.

**About Project:**

The "Redbus Data Scraping and Filtering with Streamlit Application" aims to revolutionize the transportation industry by providing a comprehensive solution for collecting, analyzing, and visualizing bus travel data. By utilizing Selenium for web scraping, this project automates the extraction of detailed information from Redbus, including bus routes, schedules, prices, and seat availability. By streamlining data collection and providing powerful tools for data-driven decision-making, this project can significantly improve operational efficiency and strategic planning in the transportation industry. I have took bus data of 10 states inc;uding their Private and Government bus Services.

**Approach to the Project:**

**Data Scraping:**
I have used Selenium Python to extract the data from redbus website(www.redbus.in). Selenium Python bindings provides a simple API to write functional/acceptance tests using Selenium WebDriver. Through Selenium Python API you can access all functionalities of Selenium WebDriver in an intuitive way. The extraction includes data such as Route Name, Route Links, Bus name, Bus Type, Start rating of the bus, Depature Time, Arrival Time, Price and Seat Availability.

For installing selenium:  pip install selenium

**Data Cleaning:**
Once the data has been extracted, I’ve used Pandas library from Python, to clean the extracted data in multiple ways such as replacing the NULL values, changing the data types to the required format. Collaging the data into the single csv file.

For Installing pandas: pip install pandas

**Data Storage:**
I’ve used Postgresql as the storage database to store the extracted and cleaned data. I have created a connection to SQL database from Jupiter Notebook and created a Table and pushed the values from the CSV to dataframe to the SQL Table.

For connecting between Python and SQL I’ve installed two packages: pip install psycopg2 sqlalchemy

**Streamlit Application:**

Developed a Streamlit application to display the scraped data as an end information to the end user.
Here, I have connected the python file with sql to extract required data to give out the information on the UI and to cross check the input received to give the appropriate information for the end user.
For installing selenium: Pip install streamlit 

**Information About the files updated in the GitHub:**

I have scraped all the 10 states individually, and saved files individually using .ipynb extension. These 10 files create 10 individual  csv files of the scrapped data. And using Final_bus_compililation.ipynb, I’ve collaborated all csv files into individual files and pushed the data in SQL database.
Now for streamlit application, I’ve created Project_redbus.py, I have connected the SQL database and used python and streamlit to display get the input from the user in the form of UI and display the result in the table format.

![image](https://github.com/user-attachments/assets/ea6993d0-18c9-4d75-923a-fc5dfd786473)

The UI part contains 2 pages. Page 1 allows user to select the Filters for the bus service.

Box 1, Allows users to select the Bus service based on the state. I have designed this based upon the Radio Button to get the input from the user. Once the user selects, the data of the relevant services will be accessed using SQL connection. SO the users will be able to select the filters for the specified services.

Box 2, Displays the welcome sign for the each transport service corporation. This changes Dynamically for each services users select.

Box 3, Gives us 2 tabs (Select the Options, View the uses). Select the options allows user to select the options for the buses based on the filters. 

Box 4, allows user to select the filters for the buses for the choice. It is not necessary that users needs to select every option, even if the user selects route all the bus details will be visible and user can further use filters to narrow down the selection.

Now if the user have selected all required filters, From Box 3, user needs to select View the buses option.

![image](https://github.com/user-attachments/assets/2e61e217-476a-424b-884a-cbe82045d47b)

User can click on Load the Buses Option to view the available buses. If No buses are avialble for the selection, an warning will be displayed for the user.


