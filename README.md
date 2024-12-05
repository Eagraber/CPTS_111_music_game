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
#Prints the game menu with options to display game rules, play the game, or exit. 
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
#Prints the game rules.
    """
    Display the game rules

    """
    print("\nGame Rules:")
    print("The objective of the game is to correctly guess the artist and song title of a music clip within 30 seconds.")
    print("You will receive 1 point for guessing the correct artist and 1 point for the correct song title.")
    print("After 30 seconds, the song will end, and you will type in your guess.")
    print("Your points will be awarded accordingly based on the accuracy of your guess.")
    print("The next music clip will be played, and the process will continue repeating.\n")
    
def play_game():
    total_points = 0
    for song in songs:
        print("\nPlaying a song snippet...")
        play_song(song["file"])
        
#Wait for 30 seconds
        time.sleep(30)
        artist_guess = input("Guess the artist: ")
        title_guess = input("Guess the song title: ")

#Song data for the game
songs = [
    {"file": r"mp3_lib/ACDC/Back in Black/ACDC - Back In Black (Lyrics) [ ezmp3.cc ].mp3", "artist": "AC/DC", "title": "Back in Black"},
    {"file": r"mp3_lib/Arctic Monkeys/Arabella/Arabella - Arctic Monkeys LYRICS [ ezmp3.cc ].mp3", "artist": "Arctic Monkeys", "title": "Arabella"},
    {"file": r"mp3_lib/Beyonce/Hold up/Beyoncé - Hold Up (With Lyrics) [ ezmp3.cc ].mp3", "artist": "Beyoncé", "title": "Hold Up"},
    {"file": r"mp3_lib/Billie Eilish/Happier than ever/Billie Eilish - Happier Than Ever (Official Lyric Video) [ ezmp3.cc ].mp3", "artist": "Billie Eilish", "title": "Happier Than Ever"},
    {"file": r"mp3_lib/Chappell Roan/Good Luck Babe/Chappell Roan - Good Luck, Babe! (Official Lyric Video) [ ezmp3.cc ].mp3", "artist": "Chappell Roan", "title": "Good Luck, Babe!"},
    {"file": r"mp3_lib/Demi Lovato/Heart attack/Demi Lovato - Heart Attack (Lyrics) [ ezmp3.cc ].mp3", "artist": "Demi Lovato", "title": "Heart Attack"},
    {"file": r"mp3_lib/Dua Lipa/Cold Heart/Elton John & Dua Lipa - Cold Heart (PNAU Remix) [ ezmp3.cc ].mp3", "artist": "Dua Lipa", "title": "Cold Heart"},
    {"file": r"mp3_lib/Eagles/Hotel California/Hotel California - Eagle (Lyric) [ ezmp3.cc ].mp3", "artist": "Eagles", "title": "Hotel California"},
    {"file": r"mp3_lib/Hinder/Lips of an angel/Lips Of An Angel - Hinder (Lyrics) [ ezmp3.cc ].mp3", "artist": "Hinder", "title": "Lips of an Angel"},
    {"file": r"mp3_lib/Hozier/From eden/Hozier _ From Eden Lyrics [ ezmp3.cc ].mp3", "artist": "Hozier", "title": "From Eden"},
    {"file": r"mp3_lib/Justin Bieber/Ghost/Justin Bieber - Ghost (Lyrics) [ ezmp3.cc ].mp3", "artist": "Justin Bieber", "title": "Ghost"},
    {"file": r"mp3_lib/Kacey Musgraves/Anime Eyes/Kacey Musgraves - Anime Eyes (Official Audio) [ ezmp3.cc ].mp3", "artist": "Kacey Musgraves", "title": "Anime Eyes"},
    {"file": r"mp3_lib/Khalid/Young Dumb & Broke/Khalid - Young Dumb & Broke (Lyrics) [ ezmp3.cc ].mp3", "artist": "Khalid", "title": "Young Dumb & Broke"},
    {"file": r"mp3_lib/Lana Del Rey/Blue Jeans/Blue Jeans - Lana Del Rey (Lyrics) [ ezmp3.cc ].mp3", "artist": "Lana Del Rey", "title": "Blue Jeans"},
    {"file": r"mp3_lib/Lorde/Mood Ring/Lorde - Mood Ring (Lyric Video) [ ezmp3.cc ].mp3", "artist": "Lorde", "title": "Mood Ring"},
    {"file": r"mp3_lib/Metallica/Enter sandman/Metallica_ Enter Sandman (Official Music Video) [ ezmp3.cc ].mp3", "artist": "Metallica", "title": "Enter Sandman"},
    {"file": r"mp3_lib/Miley Cyrus/Used to be young/Miley Cyrus - Used To Be Young (Lyrics) [ ezmp3.cc ].mp3", "artist": "Miley Cyrus", "title": "Used To Be Young"},
    {"file": r"mp3_lib/Noah Kahan/Homesick/Noah Kahan - Homesick (Official Lyric Video) [ ezmp3.cc ].mp3", "artist": "Noah Kahan", "title": "Homesick"},
    {"file": r"mp3_lib/Rihanna/We found love/Rihanna - We Found Love (Lyrics) [ ezmp3.cc ].mp3", "artist": "Rihanna", "title": "We Found Love"},
    {"file": r"mp3_lib/Sabrina Carpenter/Juno/Sabrina Carpenter - Juno (Official Lyric Video) [ ezmp3.cc ].mp3", "artist": "Sabrina Carpenter",
     {"file": r"mp3_lib/Selena gomez/lose you to love me/Selena Gomez - Lose You To Love Me (Lyrics) [ ezmp3.cc ].mp3", "artist": "Selena Gomez", "title": "Lose You To Love Me"},
    {"file": r"mp3_lib/Shaboozey/A bar song/Shaboozey - A Bar Song (Tipsy) (Lyrics) [ ezmp3.cc ].mp3", "artist": "Shaboozey", "title": "A Bar Song"},
    {"file": r"mp3_lib/SZA/Saturn/@sza - Saturn (Lyrics) [ ezmp3.cc ].mp3", "artist": "SZA", "title": "Saturn"},
    {"file": r"mp3_lib/Taylor Swift/Cruel Summer/Taylor Swift - Cruel Summer (Lyrics) [ ezmp3.cc ].mp3", "artist": "Taylor Swift", "title": "Cruel Summer"},
    {"file": r"mp3_lib/teddy swims/lose control/Teddy Swims - Lose Control (Lyrics) [ ezmp3.cc ].mp3", "artist": "Teddy Swims", "title": "Lose Control"},
    {"file": r"mp3_lib/The 1975/somebody else/the 1975 - somebody else  lyrics [ ezmp3.cc ].mp3", "artist": "The 1975", "title": "Somebody Else"},
    {"file": r"mp3_lib/The Chainsmokers/Closer/The Chainsmokers - Closer (Lyrics) ft. Halsey [ ezmp3.cc ].mp3", "artist": "The Chainsmokers", "title": "Closer"},
    {"file": r"mp3_lib/The fray/You found me/The Fray - You Found Me (Lyrics) [ ezmp3.cc ].mp3", "artist": "The Fray", "title": "You Found Me"},
    {"file": r"mp3_lib/Thomas Rhett/Somethin' 'bout a woman/Thomas Rhett - Somethin’ ‘Bout A Woman (Lyric Video) [ ezmp3.cc ].mp3", "artist": "Thomas Rhett", "title": "Somethin' 'Bout A Woman"},
    {"file": r"mp3_lib/Zedd/the middle/Zedd, Maren Morris, Grey - The Middle (Lyrics) [ ezmp3.cc ].mp3", "artist": "Zedd", "title": "The Middle"},
]
