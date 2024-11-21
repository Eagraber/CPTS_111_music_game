# CPTS_111_music_game
Trivia music game
Modulo info
pip install pydub simpleaudio
To play 30 seconds from an MP3 song, you can use the pydub library along with simpleaudio for playback. First, you need to install pydub and simpleaudio:
Here is an example of how to play 30 seconds from an MP3 file:
This script:
Uses pydub to load the MP3 file.
Extracts the first 30 seconds of the song.
Plays the extracted segment using pydub.playback.play.
Make sure to replace "path/to/your/song.mp3" with the actual path to your MP3 file.

void Display game menu()
- prints game rules
- plays game
- exit
- option input
non-void chops(mp3 library)
- takes 30sec snippet from middle of the song
- returns snipet


def display_game_menu():
    """
    Display the game menu.
    """
    print("Welcome to the 30-Second Music Trivia Game!")
    print("Please select an option:")
    print("1. Display Game Rules")
    print("2. Play Game")
    print("3. Exit")

    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        display_game_rules()
    elif choice == '2':
        print("Starting the game... (This is where the game logic would go)")
        # Add game logic here
    elif choice == '3':
        print("Exiting the game. Goodbye!")
    else:
        print("Invalid choice. Please select a valid option.")

def display_game_rules():
    """
    Display the game rules.
    """
    print("\nGame Rules:")
    print("The objective of the game is to correctly guess the artist and song title of a music clip within 30 seconds.")
    print("You will receive 1 point for guessing the correct artist and 1 point for the correct song title.")
    print("After 30 seconds, the song will end, and you will type in your guess.")
    print("Your points will be awarded accordingly based on the accuracy of your guess.")
    print("The next music clip will be played, and the process will continue repeating.\n")
    

