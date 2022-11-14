# Movie Database
(Developed by G.Milzink)

![Screenshot](docs/images/movie_database_startscreen.webp)

[Live Site](https://https://movie-database-gm.herokuapp.com/)

## Table of Contants

1. [Project Goals](#project-goals)
    1. [User Goals](#user-goals)
    2. [Site Owner Goals](#site-owner-goals)
2. [User Experience](#user-experience)
    1. [Target Audience](#target-audience)
    2. [User Stories](#user-stories)
    3. [User Manual](#user-manual)
3. [Technical Design](#technical-design)
    1. [Flowchart](#flow-chart)
    2. [Design](#design)   
4. [Technologies Used](#technologies-used)
    1. [Languages](#languages)
    2. [Frameworks and Tools](#frameworks-and-tools)
5. [Features](#features)
6. [Testing](#validation)
    1. [Python Validation](#Python-validation)
    2. [Testing user stories](#testing-user-stories)
7. [Bugs](#Bugs)
8. [Deployment](#deployment)
9. [Credits](#credits)
10. [Acknowledgements](#acknowledgements)

## Project Goals

- The projects main goal is to provide the user with an easy way to search an external database of movies using specific criteria such as "director" and year of release.
- The application will allow the user to string together queries to perform complex searches inside the database.
- The application will allow the user to keep/review/delete previous search results.
- The application will allow the user to enter movies into the database.
- The application will allow any registered user to add a new user to the system.

### User Goals

- The abillity to search a database for one or more movies based on certain specific criteria.
- The abillity to keep/review.delete past search results.
- The abillity to add movies to the database.

### Site owner goals
- Create an application that allows the user to easily find or add movies in a database and create a personal list of movies wich can be reviewed later.
- Create an application that is easy to use and provides clear feedback to the user.

## User Experience

### Target Audience
- Movie Enthousiasts.

### User Stories

#### User
1. As a first-time user I want to easily learn how the application works.
2. As a user I want to be able to search for a specific movie based on given data and see the results immediatly.
3. As a user I want to be able to build a personal database of search results.
4. As a user I want to be able to review my previous search results.
5. As a user I want to have the option to delete previous search results.
6. As a user I want to be able to add a new movie to the database.

#### Site Owner
7. As the site owner I want users to be able to easily search the database.
8. As the site owner I want search results to be stored inside a google sheet.
9. As the site owner I want user to be able to add Movies to the database.
10. As the site owner I want to be able to add a new user to the system.
11. As the site owner I want every new entry to follow the correct format.
12. As the site owner I want restrict use of the application to registered users.

### User Manual

<details><summary>Instruction manual</summary>

#### Overview

The Movie Database has been designed to allow the user to easily search a large database of movies based on parameters such as  the movies title, director and year of release among others.
The application also allows the user to add movies to the database.
Upon running the application, the user is first greeted by the logo screen.

#### Login

Below the logo screen the user will find a prompt asking for a user name.
This request will repeat untill a valid user name is provided.
Once a valid user name is received the application will prompt the user to enter the associated pasword. Upon receiving a valid password the application wil continue.
If the password provided is not valid the login process will reset to allow the user to try again.

For testing purposes and initial setup the following login has been provided.
User name: md_admin
Password: md_password

#### Main Interface

After login a welcome message will be displayed followed by instructions on the basic syntax for the interface.
The application will then prompt the user to provide instructions.

The Main Interface accepts the following top level commands:
- **/help** will display detailed instructions on program operation
- **/results** displays all previous search results.
- **/clear** will prompt the user to delete *all* previous search data.
- **/add** allows the user to add a movie to the database.
(movie title *must* be unique)
- **/add** to add a new user acount.
- **/leave** will exit Movie Database.

The Main Interface accepts the following search parameters:
- **/title**
any movie title. *case sensitive*
- **/genre**
horror,sci-fi,drama,comedy,documentary
- **/style**
live-action,animation,stop-motion,found-footage
- **/director**
any director. *case sensitive*
- **/year**
any year
- **/score**
0.0 through 10.0

Queries and parameters should be seperated by comma's:
- /genre,horror
- /director,Peter Jackson

Queries can be combined by using "&"
examples:
- /genre,horror&/year,2004
- /style,live-action&/genre,fantasy&/director,Peter Jackson

#### Add Movie

#### Clear Results Prompt

</details>

[Back to Table Of Contents](#table-of-contents)

## Technical Design

### Flow Chart

<details><summary>Flowchart</summary>
<img src="docs/images/md_flowchart.png"></details>

### Design

The application uses a google spreadsheet to store data externally.
This includes: The actual database, instructions, welcome message, user login details and personal search results.

## Technologies Used

### Languages

- [Python3](https://python.org)

### Frameworks and Tools

1. [GitPod](https://gitpod.io) - Cloudbased Development Environment
2. [GitHub](https://github.com) - GitHub was used as a remote repository to store project code.
3. [LucidChart](https://lucid.app) - LucidChart was used to create the flowchart for the application
4. [Google Sheets](https://www.google.co.uk/sheets/about/) - was used to store data externaly.
5. [Google Cloud Platform](https://cloud.google.com/cloud-console/) - was used to manage access and permissions to the google services, google auth, sheets etc.

#### Libraries

1. sys - used to allow user to terminate the program.
2. getpass - used to hide User password during/after entry.

### Third party libraries

1. [Colorama](https://pypi.org/project/colorama/) - JUSTIFICATION: Used to add color to the terminal improving application feedback and overall readability and improve the user experience.

2. [gspread](https://docs.gspread.org/en/latest/) - JUSTIFICATION: Used to store main body of data comprising the database, messages to display to user, search results and user login details in a googlew spreadsheet.
3. [Google Cloud Platform](https://cloud.google.com/cloud-console/) - JUSTIFICATON: Used to manage access and permissions to the google services, google auth, sheets etc.

[Back to Table Of Contents](#table-of-contents)

## Features

### Logo

<img src="docs/images/md_logo.webp">

### Login Screen

<img src="docs/images/md_login.webp">

User stories covered by this screen:
3, 12

### Main Interface

<img src="docs/images/md_main_interface.webp">

User stories covered by this screen:
1, 2, ,5, 6, 7, 9, 10

### Detailed Instructions

<img src="docs/images/md_detailed_instructions.webp">

User stories covered by this screen:
1,7

### Clear Results Prompt

<img src="docs/images/md_clear_results_prompt.webp">

User storie covered by this screen:
5

### Add New Movie Menu

<img src="docs/images/md_add_movie_menu.webp">

User stories covered by this screen:
6, 9

### Add New Movie Process

<img src="docs/images/md_add_movie_proces.webp">
<img src="docs/images/md_add_movie_proces_2.webp">

6, 9, 11

[Back to Table Of Contents](#table-of-contents)

## Validation

### Python Validation
All Python code  was validated using PEP8 Validation Service.  All Code passed with 0 errors.

<details><summary>run.py</summary>
<img src="docs/images/md_validation.webp">
</details>

### Testing user stories

1. As a first-time user I want to easily learn how the application works.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
|Main interface|type /help | User is presented with detailed instructions|works as expected|

2. As a user I want to be able to search for a specific movie based on given data and see the results immediatly.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
|Main interface|enter query| Search results are displayed|works as expected|

3. As a user I want to be able to build a personal database of search results.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
|Login Screen|Enter login| Personal worksheet accessed|works as expected|

4. As a user I want to be able to review my previous search results.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
|Main interface|type /results| Previous searches are displayed|works as expected|

5. As a user I want to have the option to delete previous search results.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
|Main interface|type /clear| Previous searches are deleted|works as expected|

6. As a user I want to be able to add a new movie to the database.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
|Main interface|type /add_movie| Go to add movie menu|works as expected|
|Add movie menu|Select option 1 |Start entering movie detials| Works as expected|

7. As the site owner I want users to be able to easily search the database.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
|Main interface|Enter search parameters| Results are displayed|works as expected|

8. As the site owner I want search results to be stored inside a google sheet.

9. As the site owner I want user to be able to add Movies to the database.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
|Main interface|type /add| Go to add movie menu|works as expected|
|Add movie menu|Select option 1 |Start entering movie detials| Works as expected|

10. As the site owner I want to be able to add a new user to the system.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
|Main interface|Type: /add_user|Go to add user menu|works as expected|
|Add user menu|Enter valid user details|User is created| Works as expected|

11. As the site owner I want every new entry to follow the correct format.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
|Add movie menu|Select option 1 |Receive instruction on new movie entry| Works as expected|

12. As the site owner I want restrict use of the application to registered users.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
|Login Screen|Enter valid login|Login accepted |works as expected|
|Login Screen|Enter invalid login|Login rejected |works as expected|

[Back to Table Of Contents](#table-of-contents)

## Deployment

### Heroku

This application has been deployed from Github using Heroku. Here's how:

1. Create an account at heroku.com
2. Create a new app, add app name and your region
3. Click on create app
4. Go to "Settings"
5. Under Config Vars, add your sensitive data (creds.json for example)
6. For this project, I set buildpacks to "Python" and "NodeJS" in that order.
7. Go to "Deploy" and at "Deployment method", click on "Connect to Github"
8. Enter your repository name and click on it when it shows below
9. Choose the branch you want to buid your app from
10. If desired, click on "Enable Automatic Deploys", which keeps the app up to date with your Github repository

### Forking the GitHub Repository 

By forking this GitHub repository you are creating a copy to view or make changes without affecting the original. You can do this by following these steps...

1. Log into your GitHub account and find the [repository](https://github.com/G-Milzink/CI_PP3_MD).
2. Click 'Fork' (last button on the top right of the repository page).
3. You will then have a copy of the repository in your own GitHub account. 

### Making a Local Clone

1. Log into your GitHub account and find the [repository](https://github.com/G-Milzink/CI_PP3_MD).
2. Click on the 'Code' button (next to 'Add file'). 
3. To clone the repository using HTTPS, under clone with HTTPS, copy the link.
4. Then open Git Bash.
5. Change the current working directory to where you want the cloned directory to be made.
6. In your IDE's terminal type 'git clone' followed by the URL you copied.
7. Press Enter. 
8. Your local clone will now be made.

## Credits

### Code

- **Code Institute** - for git template IDE and heroku deployment instructions.
- **Google** - for library [gspread](https://docs.gspread.org/en/latest/) and [APIS](https://developers.google.com/sheets/api)

## Acknowledgements
I would like to take the opportunity to thank:
- My mentor Mo Shami for his feedback, advice, guidance and support.
- My partner Geertje van der Zalm for her support, inspiration and patience.
- My mother Anne Rijsdijk and her husband Mickel Pereira for helping me persue this dream.
- Anyone who spends time on the internet making tutorials, awnsering questions or otherwise helping others to learn.

[Back to Table Of Contents](#table-of-contents)