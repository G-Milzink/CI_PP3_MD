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
messages = SHEET.worksheet("messages")
registered_users = SHEET.worksheet("users")


def user_authentication() -> bool:
    """
    Request username/pasword and check to see if
    combination exists in worksheet.
    If true continue..else repeat request.
    """
    user_name = input("Enter user-name:\n")
    list_of_users = registered_users.col_values(1)
    if user_name in list_of_users:
        print("User recognized")
        user_row = registered_users.findall(user_name)
        user_row = str(user_row).split(" ")[1]
        user_row = user_row[1:][:-2]
        logged_password = registered_users.cell(user_row, 2).value
        password = input("Enter password:\n")
        if password == logged_password:
            print(f"Hello {user_name}")
            login = True
        else:
            print("Unknown username/password combination...")
            print("Please try again.")
            user_authentication()
    else:
        print("Username not recognized...")
        print("Please try again.")
        user_authentication()
    return login


def get_user_input():
    """
    Wait for user input and return received query as a string.
    """
    print("\nPlease enter a query:")
    user_input = input(">>>\n")
    return user_input


def display_welcome():
    """
    Read welcome txt from worksheet and display to user.
    """
    welcome_txt = messages.col_values(1)
    print("")
    for line in welcome_txt:
        print(line)


def display_instructions():
    """
    Display detailed instructions on application functionality and syntax.
    """
    instructions = messages.col_values(2)
    print("")
    for line in instructions:
        print(line)
    input("Hit 'Enter' to continue...\n")
    main()


def leave_database():
    """
    Display 'goodbye' message and exit application.
    """
    print("Goodbye...")
    print("Thank you for using the Movie Database!")
    sys.exit()


def input_parser(user_input):
    """
    Parse user query and execute relevant functions.
    """
    title = style = genre = director = score = year = "_no_data*"
    if user_input == "/help":
        display_instructions()
    elif user_input == "/leave":
        leave_database()
    else:
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
            else:
                print(f"{query[0]} is not a valid query.")

    parsed_input = [title, style, genre, director, score, year]
    return parsed_input


def data_retrieval(parsed_input):
    """
    Prompt user to clear/save previous search results.
    Retrieve appropriate rows from worksheet
    based on parsed user input.
    """
    print("Clear results from previous query? (y/n)")
    clear = input(">>>\n")
    if clear == "y":
        print("Clearing all previous search data...")
        results.clear()
        results.append_row(["Title", "Style", "Genre", "Director", "Year", "Score"])
    else:
        print("Previous search results have been saved.")

    cells_to_compare = []
    print("Processing.....")

    for query in parsed_input:
        if query != "_no_data*":
            cell_list = database.findall(query)
            relevant_cells = []
            for cell in cell_list:
                cell = str(cell).split(" ")[1]
                cell = cell[1:][:-2]
                relevant_cells.append(cell)
            cells_to_compare.append(relevant_cells)
    if len(cells_to_compare) > 0:
        result = list(set.intersection(*map(set, cells_to_compare)))
        for i in result:
            results.append_row(database.row_values(i))
        print("Data written to worksheet.")
    else:
        print("No valid query received...")
        print("Please try again.")
        main()


def main():
    """
    Run all program functions.
    """
    display_welcome()
    user_input = get_user_input()
    parsed_input = input_parser(user_input)
    data_retrieval(parsed_input)


print("Please login to use Movie Database")
if user_authentication():
    main()
