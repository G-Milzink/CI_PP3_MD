"""
Commandline interface for google spreadsheet based movie database.
"""
import sys
import getpass
import pprint
from colorama import Fore, Style
import gspread
from google.oauth2.service_account import Credentials

pp = pprint.PrettyPrinter(width=80, compact=True)

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("movie_database")

DATABASE = SHEET.worksheet("data")
MESSAGES = SHEET.worksheet("messages")
REGISTERED_USERS = SHEET.worksheet("users")
RESULTS = SHEET.worksheet("empty")


def show_logo():
    """
    Read ASCII logo from worksheet and display to user.
    """
    ascii_logo = MESSAGES.col_values(3)
    col = 0
    for line in ascii_logo:
        if col == 0:
            print(Fore.RED + line)
        if col == 1:
            print(Fore.RED + line)
        if col == 2:
            print(Fore.YELLOW + line)
        if col == 3:
            print(Fore.GREEN + line)
        if col == 4:
            print(Fore.BLUE + line)
        if col == 5:
            print(Fore.BLUE + line)
        col += 1


def user_authentication() -> bool:
    """
    Request username/pasword and check to see if
    combination exists in worksheet.
    If true continue..else repeat request.
    """
    login = False
    user_name = input("Enter user-name:\n")
    list_of_users = REGISTERED_USERS.col_values(1)
    if user_name in list_of_users:
        print(Fore.GREEN + "User recognized")
        print(Style.RESET_ALL)
        user_row = REGISTERED_USERS.findall(user_name)
        user_row = str(user_row).split(" ")[1]
        user_row = user_row[1:][:-2]
        logged_password = REGISTERED_USERS.cell(user_row, 2).value
        password = getpass.getpass("Enter password:\n")
        if password == logged_password:
            print(f"Hello {user_name}")
            login = True
            try:
                global RESULTS
                RESULTS = SHEET.worksheet(user_name)
            except gspread.exceptions.WorksheetNotFound:
                print(Fore.RED + "Worksheet not found...")
                print(Fore.WHITE + "Creating New Worksheet...")
                RESULTS = SHEET.add_worksheet(title=user_name,
                                              rows=1000, cols=5)
                print(Fore.YELLOW + "New Empty Worksheet Created.")
                print(Fore.WHITE)
        else:
            print(Fore.RED + "Unknown username/password combination...")
            print(Style.RESET_ALL)
            print("Please try again.")
            login = False
    else:
        print(Fore.RED + "Username not recognized...")
        print(Style.RESET_ALL)
        print("Please try again.")
        login = False
    return login


def display_welcome():
    """
    Read welcome txt from worksheet and display to user.
    """
    welcome_txt = MESSAGES.col_values(1)
    print("")
    for line in welcome_txt:
        if line[0] == "/":
            print(Fore.YELLOW + line)
        else:
            print(Style.RESET_ALL + line)


def display_instructions():
    """
    Display detailed instructions on application functionality and syntax.
    """
    instructions = MESSAGES.col_values(2)
    print("")
    for line in instructions:
        if line[0] == "-":
            print(Fore.GREEN + line)
        elif line[0] == "/":
            print(Fore.YELLOW + line)
        elif line[0] == "!":
            print(Fore.RED + line)
        else:
            print(Style.RESET_ALL + line)
    input(Fore.WHITE + "Hit 'Enter' to continue...\n")
    main()


def leave_database():
    """
    Display 'goodbye' message and exit application.
    """
    print(Fore.YELLOW + "Thank you for using the Movie Database...")
    sys.exit()


def clear_results():
    """
    Prompt user to either delete or keep previous search results.
    """
    print(Fore.RED + "Clear results from previous query? (y/n)")
    print(Fore.WHITE)
    clear = input(">>>\n")
    if clear == "y":
        print(Fore.YELLOW + "Clearing all previous search data...")
        RESULTS.clear()
        first_row = ["Title", "Style", "Genre", "Director", "Year", "Score"]
        RESULTS.append_row(first_row)
    else:
        print("Previous search results have been saved.")


def get_user_input():
    """
    Wait for user input and return received query as a string.
    """
    print(Style.RESET_ALL + "\nPlease enter a query:")
    user_input = input(">>>\n")
    return user_input


def input_parser(user_input):
    """
    Parse user query and execute relevant functions.
    """
    title = style = genre = director = score = year = "_no_data*"
    if user_input == "/help":
        display_instructions()
    elif user_input == "/leave":
        leave_database()
    elif user_input == "/clear":
        clear_results()
        main()
    elif user_input == "/add_movie":
        add_movie_menu()
    elif user_input == "/add_user":
        add_user_menu()
    elif user_input == "/results":
        display_results()
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
    Retrieve appropriate rows from worksheet
    based on parsed user input.
    """
    cells_to_compare = []
    print("Processing.....")

    for query in parsed_input:
        if query != "_no_data*":
            cell_list = DATABASE.findall(query)
            relevant_cells = []
            for cell in cell_list:
                cell = str(cell).split(" ")[1]
                cell = cell[1:][:-2]
                relevant_cells.append(cell)
            cells_to_compare.append(relevant_cells)
    if len(cells_to_compare) >= 1:
        result = list(set.intersection(*map(set, cells_to_compare)))
        print(Fore.YELLOW + "Search complete.")
        print(Fore.WHITE + "Display results? (y/n)")
        if input(">>>") == "y":
            for i in result:
                row = ",".join(DATABASE.row_values(i))
                pp.pprint(row)
        print(Fore.YELLOW + "Store results in worksheet? (y/n)")
        print(Fore.WHITE)
        if input(">>>") == "y":
            for i in result:
                RESULTS.append_row(DATABASE.row_values(i))
        print(Fore.YELLOW + "Data written to worksheet.\n")
        main()
    else:
        print("No valid query received...")
        print("Please try again.")
        main()


def add_movie_menu():
    """
    Prompt user if they want to enter a new movie into the database
    """
    print(Fore.YELLOW + "Add  new movie to database:")
    print(Fore.WHITE + "1. Add new movie.")
    print("2. Stop adding movies.")
    menu_choice = input(">>>\n")
    if menu_choice == "1":
        add_movie()
    elif menu_choice == "2":
        main()
    else:
        print(Fore.RED + "Unknown menu selection please try again.\n")
        add_movie_menu()


def add_movie():
    """
    Allow user to enter new movie into database.
    Ask for new movie Title and check to see if title already exists.
    If so inform user go back to add_movie_menu()

    If no movie with given title exists move on to collect remaining
    information about movie and add to database when complete.
    """
    movie_list = DATABASE.col_values(1)
    print(Fore.YELLOW + "Enter movie title:")
    new_movie_title = input(Fore.WHITE + ">>>")
    if new_movie_title in movie_list:
        print(Fore.RED + "Movie is already in database.\n")
        add_movie_menu()
    else:
        while True:
            print(Fore.YELLOW + "Select movie style:")
            print(Fore.WHITE + "1. Live Action.")
            print("2. Found Footage.")
            print("3. Stop Motion.")
            print("4. Animation.")
            menu_choice = input(">>>\n")
            if menu_choice == "1":
                new_movie_style = "live-action"
                break
            elif menu_choice == "2":
                new_movie_style = "found-footage"
                break
            elif menu_choice == "3":
                new_movie_style = "stop-motion"
                break
            elif menu_choice == "4":
                new_movie_style = "animation"
                break
            else:
                print(f"{menu_choice} is not a valid selection")
                print(print("Please try again."))
    while True:
        print(Fore.YELLOW + "Select movie genre:")
        print(Fore.WHITE + "1. Action.")
        print("2. Horror.")
        print("3. Drama.")
        print("4. Science Fiction.")
        print("5. Fantasy.")
        print("6. Comedy.")
        menu_choice = input(">>>\n")
        if menu_choice == "1":
            new_movie_genre = "action"
            break
        if menu_choice == "2":
            new_movie_genre = "horror"
            break
        if menu_choice == "3":
            new_movie_genre = "drama"
            break
        if menu_choice == "4":
            new_movie_genre = "sci-fi"
            break
        if menu_choice == "5":
            new_movie_genre = "fantasy"
            break
        if menu_choice == "6":
            new_movie_genre = "comedy"
            break
        else:
            print(f"{menu_choice} is not a valid selection")
            print(print("Please try again."))
    print(Fore.YELLOW + "Enter movie director:")
    new_movie_dir = input(Fore.WHITE + ">>>")
    print(Fore.YELLOW + "Enter movie release year:")
    new_movie_year = input(Fore.WHITE + ">>>")
    while True:
        print(Fore.YELLOW + "Enter movie score:(0.0 through 10.0)")
        new_movie_score = input(Fore.WHITE + ">>>")
        if float(new_movie_score) >= 0.0 and float(new_movie_score) <= 10.0:
            break
        else:
            print(Fore.RED + "Invalid score...")
            print(Fore.WHITE + "Please try again.")

    new_movie_row = [new_movie_title, new_movie_style, new_movie_genre,
                     new_movie_dir, new_movie_year, new_movie_score]
    print(Fore.YELLOW + "New movie entry:\n")
    new_movie_row = ",".join(new_movie_row)
    print(new_movie_row)
    print(Fore.WHITE)
    if input("Add this movie to the database? (y/n)") == "y":
        print("Processing")
        DATABASE.append_row(new_movie_row)
        print(Fore.GREEN + "New movie has been added to the database.")
    else:
        print(Fore.RED + "Data was NOT entered into databse.")
    add_movie_menu()


def display_results():
    """
    Read and display previous search results from worksheet.
    """
    print(Fore.YELLOW + "Previous Search Results:")
    print(Fore.WHITE)
    if len(RESULTS.col_values(1)) > 1:
        line = 1
        for row in RESULTS.get_all_values():
            if line > 1:
                row = ",".join(row)
                pp.pprint(row)
            line += 1
    print("Hit 'Enter' to continue...")
    input(">>>\n")
    main()


def add_user_menu():
    """
    Prompt user if they want to enter a User to the system
    """
    admin = input("Please provide administrator password:\n")
    if admin != MESSAGES.acell("D1").value:
        print(Fore.RED + "Incorrect Password!")
        print(Fore.YELLOW + "Returning to main interface.")
        main()
    print(Fore.YELLOW + "Add  new user to database:")
    print(Fore.WHITE + "1. Add new user.")
    print("2. Stop adding users.")
    menu_choice = input(">>>\n")
    if menu_choice == "1":
        add_new_user()
    elif menu_choice == "2":
        main()
    else:
        print(Fore.RED + "Unknown menu selection please try again.\n")
        add_movie_menu()


def add_new_user():
    """
    Ask for new user name, check if available.
    If so: request a password and confirm with a second request.
    Display provided and ask user if new user should be added.
    """
    while True:
        print("Enter new user name:")
        new_user_name = input(">>>\n")
        list_of_users = REGISTERED_USERS.col_values(1)
        if new_user_name in list_of_users:
            print(Fore.RED + "Sorry!...That name is already taken.")
            print(Fore.WHITE)
            add_user_menu()
        else:
            break

    while True:
        print("Enter Password:")
        new_pass1 = input(">>>\n")
        print("Confirm Password:")
        new_pass2 = input(">>>\n")
        if new_pass1 == new_pass2:
            new_user_pass = new_pass1
            break

    new_user_row = [new_user_name, new_user_pass]
    REGISTERED_USERS.append_row(new_user_row)
    print("New user added...")
    print("Personal Worksheet will be created on first login.")
    main()


def main():
    """
    Run main program functions.
    """
    display_welcome()
    user_input = get_user_input()
    parsed_input = input_parser(user_input)
    data_retrieval(parsed_input)


show_logo()
print(Fore.YELLOW + "\nPlease login to use Movie Database")
print(Style.RESET_ALL)

while True:
    if user_authentication():
        break
main()
