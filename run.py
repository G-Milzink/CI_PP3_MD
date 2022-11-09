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

database = SHEET.worksheet("data")
results = SHEET.worksheet("results")


def get_user_input():
    """
    Wait for user input and return received query as a string.
    """
    print("\nPlease enter a query:")
    user_input = input(">>>")
    return user_input


def display_instructions():
    """
    Display detailed instructions on application functionality and syntax.
    """
    print("\nThis will contain detailed instuctions on how to use")
    print("this application.")
    main()


def input_parser(user_input):
    """
    Parse user query and execute relevant functions.
    """
    print(user_input)
    if user_input == "/help":
        display_instructions()
    elif user_input == "/leave":
        print("Goodbye...")
        print("Thank you for using the Movie Database!")
        sys.exit()
    else:
        title = style = genre = director = score = year = years = "*"
        queries = user_input.split("&")
        for query in queries:
            query = query.split(",")
            if query[0] == "/title":
                title = query[1]
                print(f"Title: {title}")
            elif query[0] == "/style":
                style = query[1]
                print(f"Style: {style}")
            elif query[0] == "/genre":
                genre = query[1]
                print(f"Genre: {genre}")
            elif query[0] == "/director":
                director = query[1]
                print(f"Director: {director}")
            elif query[0] == "/score":
                score = query[1]
                print(f"Score: {score}")
            elif query[0] == "/year":
                year = query[1]
                print(f"Year: {year}")
            elif query[0] == "/years":
                years = [query[1], query[2]]
                print(f"Years: {years[0]} - {years[1]}")
            else:
                print(f"{query[0]} is not a valid query.")
    
    return [title, style, genre, director, score, year, years]


def data_retrieval(parsed_input):
    """
    Retrieve appropriate rows from worksheet
    based on parsed user input.
    """
    query = parsed_input
    # cells = database.findall(query)
    # results.clear()
    # first_row = ["Title:", "Style:", "Genre:", "Director:", "Year:", "Score:"]
    # results.append_row(first_row)
    # for i in cells:
    #     i = str(i)
    #     i = i.split(" ")
    #     i = i[1]
    #     i = i[1:][:-2]
    #     result = database.row_values(i)
    #     print(result)
    #     results.append_row(result)
    # print("\nSearch results added to worksheet.")


def main():
    """
    Display welcome message.
    Run all program functions.
    """
    print("\nWelcome to the Movie Database!")
    print("/help for detailed instructions.")
    print("/leave to exit Movie Database")
    user_input = get_user_input()
    parsed_input = input_parser(user_input)
    print(parsed_input)
    # data_retrieval(parsed_input)


main()
