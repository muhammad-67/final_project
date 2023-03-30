# Name: Muhammad Ghous
# Unique name: ghous

import re
import requests
import datetime
import pandas as pd
import webbrowser

def welcome_message():
    """Display welcome message to user"""

    print("-" * 50)
    print("Welcome to the Airport Weather Information Program")


def ask_user_input():
    """Ask user for a U.S airport code and validate input"""
    while True:
        airport_code = input("Enter a U.S airport code (e.g. DTW, SFO): ")
        if not re.match("^[a-zA-Z]{3}$", airport_code):
            print(
                "Invalid input. Please enter a three-letter airport code with no integers.")
            continue
        return airport_code.upper()


def get_weather_data(airport_code):
    """Get weather data from the National Weather Service API"""

    url = 'https://api.weather.gov/stations/{}/observations/latest'
    name_url = 'https://api.weather.gov/stations/{}'

    try:
        response = requests.get(url.format("K" + airport_code)).json()
        name_response = requests.get(
            name_url.format(
                "K" + airport_code)).json()
    except requests.exceptions.RequestException as e:
        print(f"Error occurred: {e}")
        return None, None

    if response.get('status') == 404:
        print("Airport code does not exist. Please enter a valid airport code.")
        return None, None

    return response, name_response


def display_weather_data(response, name_response):
    """Display weather data in a metric format"""

    name = name_response['properties']['name']
    temp = response['properties'].get('temperature', {}).get('value')
    visibility = response['properties'].get('visibility', {}).get('value')
    wind_speed = response['properties'].get('windSpeed', {}).get('value')

    if temp is None:
        temp = "No temperature data available"
    else:
        temp = f"Current temperature at {airport_code.lower()}: {temp} °C"

    if visibility is None:
        visibility = "No visibility data available"
    else:
        visibility = f"Current visibility at {airport_code.lower()}: {visibility} m"

    if wind_speed is None:
        wind_speed = "No wind speed data available"
    else:
        wind_speed = f"Current wind speed at {airport_code.lower()}: {wind_speed} km/h"

    now = datetime.datetime.now()
    date = now.strftime("%b %d, %Y")
    time = now.strftime("%H:%M:%S")
    timezone = now.strftime("%Z")

    print("-" * 50)
    print(f"Name of airport: {name}")
    print(f"Date: {date}")
    print(f"Time: {time} {timezone}")
    print(temp)
    print(visibility)
    print(wind_speed)
    print("-" * 50)


def display_weather_data_imperial(response, name_response):
    """Display weather data in imperial units"""

    name = name_response['properties']['name']
    temp_c = response['properties'].get('temperature', {}).get('value')
    visibility_m = response['properties'].get('visibility', {}).get('value')
    wind_speed_kmh = response['properties'].get('windSpeed', {}).get('value')

    if temp_c is not None:
        temp = round((int(temp_c) * 1.8) + 32, 2)
        temp_f = f"Current temperature at {airport_code.lower()}: {temp} °F"
    else:
        temp_f = "No temperature data available"

    if visibility_m is not None:
        visibility = round(int(visibility_m) * 0.000621371, 2)
        visibility_m = f"Current visibility at {airport_code.lower()}: {visibility} mi"
    else:
        visibility_m = "No visibility data available"

    if wind_speed_kmh is not None:
        wind_speed = round(int(wind_speed_kmh) * 0.621371, 2)
        wind_speed_mph = f"Current wind speed at {airport_code.lower()}: {wind_speed} mph"
    else:
        wind_speed_mph = "No wind data available"

    now = datetime.datetime.now()
    date = now.strftime("%b %d, %Y")
    time = now.strftime("%H:%M:%S")
    timezone = now.strftime("%Z")
    print("-" * 50)
    print(f"Name of airport: {name}")
    print(f"Date: {date}")
    print(f"Time: {time} {timezone}")
    print(temp_f)
    print(visibility_m)
    print(wind_speed_mph)
    print("-" * 50)


def save_data_to_file():
    """Saves the weather data to a text file."""

    name = name_response['properties']['name']
    temp = response['properties'].get('temperature', {}).get('value')
    visibility = response['properties'].get('visibility', {}).get('value')
    wind_speed = response['properties'].get('windSpeed', {}).get('value')
    now = datetime.datetime.now()
    date = now.strftime("%b %d, %Y")
    time = now.strftime("%H:%M:%S")
    timezone = now.strftime("%Z")

    filename = f"{airport_code}.txt"
    with open(filename, 'a') as file:
        if temp is None:
            temp = "No temperature data available"
        else:
            temp = f"Current temperature at {airport_code.lower()}: {temp} °C\n"

        if visibility is None:
            visibility = "No visibility data available"
        else:
            visibility = f"Current visibility at {airport_code.lower()}: {visibility} m\n"

        if wind_speed is None:
            wind_speed = "No wind speed data available"
        else:
            wind_speed = f"Current wind speed at {airport_code.lower()}: {wind_speed} km/h\n"

        file.write("-" * 50 + '\n')
        file.write(f"Name of airport: {name}\n")
        file.write(f"Date: {date}\n")
        file.write(f"Time: {time} {timezone}\n")
        file.write(temp)
        file.write(visibility)
        file.write(wind_speed)
        file.write("-" * 50 + '\n')

    print(f"Data saved to file: {filename}")

def ask_to_display_info():
    """Asks the user if they want to display additional airport information."""

    while True:
        answer = input("Do you want to display additional information? (y/n): ")
        if answer.lower() == 'yes' or answer.lower() == 'y' or answer.lower() == 'yeah':
            return True
        elif answer.lower() == 'no' or answer.lower() == 'n' or answer.lower() == 'nope':
            return False
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")
            continue

def display_airport_info(airport_info):
    """Display additional airport information."""

    print("-" * 50)
    print("Additional airport information:\n")
    print("Type:", airport_info['type'].iloc[0])
    print("Latitude:", airport_info['latitude_deg'].iloc[0])
    print("Longitude:", airport_info['longitude_deg'].iloc[0])
    print("Municipality:", airport_info['municipality'].iloc[0])
    wikipedia_link = airport_info['wikipedia_link'].iloc[0]
    print("Wikipedia link:", wikipedia_link)
    while True:
        answer = input("Do you want to visit the Wikipedia page for this airport? (y/n): ")
        if answer.lower() == 'y':
            webbrowser.open(wikipedia_link)
            break
        elif answer.lower() == 'n':
            break
        else:
            print("Invalid input. Please enter 'y' or 'n'.")
            continue
    print("-" * 50)



def ask_for_unit_conversion():
    """Ask the user if they want to convert the temperature to
    Fahrenheit and the visibility to miles"""

    response = input(
        "Do you want to display the temperature in Fahrenheit and the visibility in miles? (yes/no): ")
    return response.lower() == "yes" or response.lower() == "y" or response.lower(
    ) == "yeah" or response.lower() == "yup" or response.lower() == "sure"


def ask_another_search():
    """ Ask the user if they want to search for another airport
    if not save the output of display_weather_data to a file"""

    response = input("Do you want to search for another airport? (yes/no): ")
    if response.lower() in ["yes", "y", "yeah", "yup", "sure"]:
        return True
    else:
        response = input(
            "Do you want to save the latest weather search results to a file? (yes/no): ")
        if response.lower() in ["yes", "y", "yeah", "yup", "sure"]:
            save_data_to_file()
            print("Results saved/upades! Bye!")
            exit()
        print("Bye!")
        exit()


if __name__ == "__main__":

    # Airport data is downloaded from:
    # "https://data.world/ourairports/989444cc-447b-4030-a866-57fcd6c2d3ee/workspace/file?filename=list-of-airports-in-united-states-of-america-hxl-tags-1.csv"

    # Read the csv file containing the list of airports in the US
    airport_df = pd.read_csv('list-of-airports-in-united-states-of-america-hxl-tags-1.csv')

    # Extract type of airport type, latitude and longitude, municipality, local code, wikipedia link
    airport_df = airport_df[['type', 'latitude_deg', 'longitude_deg', 'municipality', 'local_code', 'wikipedia_link']]

    # Drop the first row which contains the descriptive names
    airport_df = airport_df.drop(airport_df.index[0])

    welcome_message()

    while True:
        airport_code = ask_user_input()
        airport_info = airport_df[airport_df['local_code'] == airport_code]
        response, name_response = get_weather_data(airport_code)
        if response is None:
            continue
        display_weather_data(response, name_response)
        if len(airport_info) > 0:
            print("More info is found about airport in our local database.")
            if ask_to_display_info():
                display_airport_info(airport_info)
        if ask_for_unit_conversion():
            display_weather_data_imperial(response, name_response)
            ask_another_search()
        else:
            ask_another_search()