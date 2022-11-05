# import libraries:
import gspread
from google.oauth2.service_account import Credentials
from pprint import pprint

# define scope:
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

# connect to spreadsheet:
CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("movie_database")

all_data = SHEET.worksheet("data").get_all_values()

def get_user_input():
    input(">>>")
    

def main():
    print("\nWelcome to the Movie Database!")
    print("/help for detailed instructions.")
    print("\nPlease enter a query:")
    get_user_input()
    

main()