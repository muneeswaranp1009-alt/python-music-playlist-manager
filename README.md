# Python Music Playlist Manager

A beginner-friendly Python project that enables users to manage a music playlist via a simple command-line interface.
The application utilizes a Python list to store the songs and offers several options for users to choose from. These options include adding a song, removing a song, and viewing the current playlist.

## Features
- Add songs to the playlist.
- Remove songs from the playlist.
- View all the songs in the playlist.
- Display song numbers using enumeration.
- Handle the attempt to remove a song that's not in the playlist.
- Display a message indicating that the playlist is empty.
- Menu option that enables the user to exit the application.
  
## Technologies
- Python
- List
- Functions
- Loops
- Conditional statements
  
## Overview
The above application was created using Python programming language. It works by first prompting the user to choose an option. Upon selecting an option, the relevant function will be triggered. For instance, the add_song() function will be triggered when the user chooses the option to add a song to the playlist.
The application will continue to prompt the user for actions to take until the exit option is selected. Some of the actions that the application can perform are:

- Adding songs to the playlist
- Removing songs from the playlist
- Viewing the playlist (displaying songs with their corresponding numbers)
The application uses lists to store the songs. Moreover, it uses loops to display the songs and their numbers. Additionally, it also uses conditional statements to check if a song is in the playlist before removing it.

## Project Structure
python-music-playlist-manager/
├── Music playlist manager.py

## Running the code
The following steps should be undertaken to run the above Python application:
1. Ensure that Python is installed in your system
2. Clone the repo
3. Access project folder in your terminal
4. Run the following command:
python "Music playlist manager.py"
5. Choose an option from the menu to start managing your playlist
   
## Sample Output
Mini Music Playlist Manager
Options: [1] Add Song [2] Remove Song [3] View Playlist [4] Exit
Enter your option: 1
Enter the song name: Perfect
'Perfect' song was Added to Playlist Successfully

## What did I learn?
From this project, I learned how to:
- Create and use a Python list
- Create and call functions
- Add and remove list elements
- Display items in a list with their numbers using enumerate()
- Create a menu-driven console application
- Use loops and conditional statements
- Perform error-handling and input validation
- 
## Project Background
I created this project as part of my Python learning journey to understand how to use lists, functions, and menu-driven console applications to create interactive command-line applications.

### Future Enhancements
Some of the features that I would like to add to the application are:
- Avoid allowing users to add empty song names
- Ability to search for songs
- Avoid allowing users to add songs that already exist in the playlist if duplicates are not allowed
- Ability to save a playlist to a file
- Ability to load a playlist
- Store additional information about a song such as the artist and album.
  
## Author
This project is part of my Python learning journey.
