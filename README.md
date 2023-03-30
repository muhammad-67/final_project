# si507_final_project
## Instructions for running the Airport Weather Information Program
This program retrieves current weather information for a given U.S. airport code by calling the National Weather Service API.

## Prerequisites
* Python 3.x
* requests module
* pandas module
* datetime module
* webbrowser module
* airport csv data

## Running the Program
1. Download csv file from: "https://data.world/ourairports/989444cc-447b-4030-a866-57fcd6c2d3ee/workspace/file?filename=list-of-airports-in-united-states-of-america-hxl-tags-1.csv" and place it in the same directory as main file.
1. Open a terminal or command prompt and navigate to the directory where the script is saved.
1. Run the script.
1. The program will display a welcome message and prompt you to enter a three-letter airport code.
1. Enter a valid U.S. airport code when prompted. If an invalid code is entered, the program will prompt you to enter a valid code.
1. The program will retrieve the latest weather information for the specified airport and display it in the terminal.
1. If more information about airport is present, it promts user to display that information.
1. You will then be prompted to choose whether to view the weather information in imperial or metric units.
1. After selecting a unit type, the program will display the weather information again in the chosen units.
1. Finally, the program will prompt you to save the weather information to a text file. If you choose to do so, the program will create a text file in the current directory with the name of the airport code and save the weather information to the file.

Note: If you encounter any errors while running the program, make sure that you have the required modules installed and that you have the airport csv file saved in its original name.
