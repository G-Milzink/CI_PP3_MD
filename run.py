# import libraries:
import sys
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
    main()


def input_parser(input):
    """
    Parse user query and execute relevant functions.
    """
    if input == ["/help"]:
        display_instructions()
    elif input == ["/leave"]:
        print("Goodbye...")
        print("Thank you for using the Movie Database!")
        sys.exit()
    else:
        print("bob")


def main():
    """
    Display welcome message.
    Run all program functions.
    """
    print("\nWelcome to the Movie Database!")
    print("/help for detailed instructions.")
    print("/leave to exit Movie Database")
    query = get_user_input()
    input_parser(query)


main()
