import streamlit as st
import pandas as pd
import numpy as np
import psycopg2
import matplotlib.pyplot as plt
import time

st.set_page_config(page_title="Red_Bus", page_icon=":oncoming_bus:")


def get_data():
    try:
        # Establish the connection
        conn = psycopg2.connect(
            host='localhost',
            database='red_bus',
            user='postgres',
            password='QWERTY',
            port='5432'
        )
        print("Connection established!")
        return conn
    except Exception as e:
        print(f"Error: {e}")
        return None

# Fetch data
conn = get_data()


# Create to get the service names for the page navigation
service_query = f"SELECT distinct(service_name) FROM public.bus_routes"
service =  pd.read_sql(service_query,conn)['service_name'].to_list()

# Sidebar for Pages
pages = ["ANDHRA", "BIHAR", "CHANDIGAR", "GUJARAT", "JAMMU & KASHMIR", "KARBI - ASSAM", "PUNJAB", "SIKIM", "WEST BENGAL", "MEHALAYA"]
st.sidebar.title("Select the Bus Service")
selected_page = st.sidebar.radio("",pages)

# Mapping pages to service
page_to_service = {
    "ANDHRA":'APSRTC',
   "BIHAR":"Bihar",
    "CHANDIGAR":"CTU",
    "GUJARAT":"GSRTC",
    "JAMMU & KASHMIR":"JKSRTC",
    "KARBI - ASSAM":"KAAC",
    "PUNJAB":"PEPSU",
    "SIKIM":"sikim",
    "WEST BENGAL":"WBTC",
    "MEHALAYA":"Mehalaya" 
}


selected_service = page_to_service.get(selected_page, None)


# Query to get the route
def select_route(selected_service):
    query = f"SELECT distinct(route_name) FROM public.bus_routes where service_name = '{selected_service}'"
    route =  pd.read_sql(query,conn)['route_name'].to_list()
    return route
# Query for get the bus tyoes
def select_type(selected_route):
    query = f"SELECT distinct(bus_type) FROM public.bus_routes where route_name = '{selected_route}'"
    type =  pd.read_sql(query,conn)['bus_type'].to_list()
    return type

#Main code starts here.
if selected_service and selected_service in service:
    selected_rating=''
    selected_price=''
    selected_start_time=''
    selected_type = ()
    selected_end_time = ''

    st.header(f"Welcome to {selected_service.upper()} Transport Corporation")
    #st.snow()
    tab1,tab2 = st.tabs(["Select the Options ✋","View the Buses 🚌"])
    with tab1:
        selected_route = st.selectbox("Select the Route",select_route(selected_service))
        if selected_route:
            selected_type = st.multiselect("Select the Bus Type",select_type(selected_route))
            selected_type = tuple(selected_type) if selected_type else None
            selected_rating = st.slider("Select the Minimum Bus Rating",min_value=1.0,max_value=5.0,step=0.5)
            selected_price = st.pills("Select the Price Range",['upto 250', 'upto 500', 'upto 1000', 'upto 1500', '1500+'],selection_mode="single")
            selected_start_time = st.pills("Select the Departure Time",['None','Before 6 AM', '6AM - 12PM', '12PM - 6PM', 'After 6PM'],selection_mode="single",key="departure_time")
            selected_end_time = st.pills("Select the Reaching Time",['None','Before 6 AM', '6AM - 12PM', '12PM - 6PM', 'After 6PM'],selection_mode="single",key="reaching_time")
                

    with tab2:
        st.write(f"List of Buses Available for {selected_route} route",":bus:")
    
        if st.button("Load the buses"):
            # used this method to get values from db based upon user selection.
            query = f"SELECT bus_name, bus_type, departing_time, duration, reaching_time, star_rating, price, seats_available FROM public.bus_routes WHERE route_name = '{selected_route}'"
            
            if selected_type and selected_type != None:
                if len(selected_type) == 1:
                    query += f" AND bus_type = '{selected_type[0]}'"
                else:
                    query += f" AND bus_type IN {selected_type}"
            if selected_rating:
                query += f" AND star_rating >= {selected_rating}"
            if selected_price:
                price_values = {
                    'upto 250': "price <= 250",
                    'upto 500': "price <= 500",
                    'upto 1000': "price <= 1000",
                    'upto 1500': "price <= 1500",
                    '1500+': "price > 1500"
                }
                query += f" AND {price_values[selected_price]}"
            if selected_start_time and selected_start_time != "None":
                start_time = {
                    'Before 6 AM': "departing_time < '06:00:00'",
                    '6AM - 12PM': "departing_time BETWEEN '06:00:00' AND '12:00:00'",
                    '12PM - 6PM': "departing_time BETWEEN '12:00:00' AND '18:00:00'",
                    'After 6PM': "departing_time > '18:00:00'"
                }
                query += f" AND {start_time[selected_start_time]}"
            if selected_end_time and selected_end_time != "None":
                end_time = {
                    'Before 6 AM': "reaching_time < '06:00:00'",
                    '6AM - 12PM': "reaching_time BETWEEN '06:00:00' AND '12:00:00'",
                    '12PM - 6PM': "reaching_time BETWEEN '12:00:00' AND '18:00:00'",
                    'After 6PM': "reaching_time > '18:00:00'"
                }
                query += f" AND {end_time[selected_end_time]}"

            result = pd.read_sql(query, conn)
            if not result.empty:
                st.snow()
                st.dataframe(result)
            else:
                st.warning("No buses available for the selected Filters.", icon="⚠️")
        
else:
    st.title("No Data Available for This Page")       

            

