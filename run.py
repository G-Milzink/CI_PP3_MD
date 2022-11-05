# import libraries:
# from pprint import pprint
import gspread
from google.oauth2.service_account import Credentials


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
    """
    Wait for user input and return received query as a list of strings.
    """
    print("\nPlease enter a query:")
    user_input = [input(">>>")]
    return user_input


def display_instructions():
    """
    Display detailed instructions on application functionality and syntax.
    """
    print("\nThis will contain detailed instuctions on how to use")
    print("this application.")
    get_user_input()


def input_parser(input):
    """
    Parse user query and execute relevant functions.
    """
    if input == ["/help"]:
        display_instructions()
        get_user_input()


def main():
    """
    Display welcome message.
    Run all program functions.
    """
    print("\nWelcome to the Movie Database!")
    print("/help for detailed instructions.")
    print("/exit to exit Movie Databse")
    query = get_user_input()
    input_parser(query)


main()
