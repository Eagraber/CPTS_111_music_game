import os
import random
import pygame
def choose_random_file(directory):
    '''Chooses a random file from directory'''
    # List all files in the given directory
    files = os.listdir(directory)
    
    # Filter out directories, only keep files
    f = []
    for f in files:
        if os.path.isfile(os.path.join(directory, f)):#checks if the file is a file
            files.append(f)
    
    # Randomly select a file from the list
    random_file = random.choice(files)
    random_file = os.path.join(directory, random_file)
    return random_file
def directory_config(random_file):
    '''Configures the directory to the correct file path'''
    files= os.listdir(random_file)
    for file in files:
       selection = os.path.join(random_file, file)#joins the directory with the file
    return selection
def play_music(random_file):
    '''Plays the music file'''
    pygame.mixer.init()#initialises the mixer
    pygame.mixer.music.load(random_file)#loads the music file
    pygame.mixer.music.play()#plays the music file
    # Wait for the music to finish playing
    while pygame.mixer.music.get_busy():#checks if the music is still playing
        pygame.time.Clock().tick(10)#10 is the quality of the music
    pygame.mixer.quit()#quits the mixer
    return
def display_game_menu():
    ''' Displays menu for the game welcoming people to music trivia and giving them the options
        1.Print game rules 2.Play game 3.Exit
        if one is selected it will print the rules to music trivia and return to menu if 2 is selected it will 
        run main pass if three is selected it will write a goodbye message
    '''
    print("Welcome to Music Trivia")
    print("1. Print game rules")
    print("2. Play game")
    print("3. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        print("Welcome to Music Trivia. The rules are simple. ")
        print("You will be presented with a song and you will have to guess the artist and the song name.")
        print("The game will run 5 times and allocate scores 1pt for artist and 1pt for song. Good luck!")#prints correct rules
        display_game_menu()
    elif choice == "2":
        os.system("cls")
        pass
    elif choice == "3":
        print("Goodbye!")
        exit()#exists the program
    else:
        print("Invalid choice. Please try again.Option 1-3.")
        display_game_menu()
    return
def questions():
    '''Asks the user for the artist and song name'''
    artistg = input("Enter the artist name: ")
    songg = input("Enter the song name: ")
    return artistg,songg
def check_answer(artistg,songg,random_file):
    ''' 
    The answer matches the file structure.Makes artistg and songg lowercase.
    Extract file name from file path and remove underscores and makes it lower case assigning it to artist and song.
    Then runs comparison to see if artistg is the same as artist and songg is the same as song 
    then allocates point to score if they match.
    '''
    score=0
    artistg=artistg.lower()
    songg=songg.lower()
    artist_split = random_file.split("\\")[-3].split("_")#changed index for file path format
    if len(artist_split) > 1:#if the artist has more than one word joins them into one string then lowers
        artist=' '.join(artist_split)
        artist=artist.lower()#changed for read ability
    else:#if the artist is one word just lowers the string
        artist=artist_split[-1].lower()
    song_split = random_file.split("\\")[-2].split("_")#changed index for file path format
    if len(song_split) > 1:#if the song has more than one word joins them into one string then lowers
        song=' '.join(song_split)
        song= song.lower()#changed for read ability
    else:#if the song is one word just lowers the string
        song=song_split[-1].lower()
    if artistg == artist:#checks that they match allocates one point
        score += 1
        print("Artist is correct")
    else:
        print("Artist is incorrect")
    if songg == song:#checks that they match allocates one point
        score += 1
        print("Song is correct")
    else:
        print("Song is incorrect")
    return score

def main():
    # Set up directory to the correct place
    os.chdir("mp3_lib")#changes the directory to the mp3_lib
    script_dir = os.path.dirname(__file__)#gets the directory of the file
    mp3_dir = os.path.join(script_dir, "mp3_lib")#joins the directory of the file with the mp3_lib
    #score accumulator
    score_total=0
    #display game menu
    display_game_menu()
    for i in range(5):
        print(f"Song {i+1}!")#prints the song number +1 because index is 0
        artistg=""#initialise players artist guess so the list can be checked per song
        songg=""#intaialise players song guess so the list can be checked per song
        random_file = choose_random_file(mp3_dir)# generates a random artist
        random_mp3=directory_config(random_file)#configures the directory to the correct file path
        song=directory_config(random_mp3)#configures the directory to the correct file path for mp3
        play_music(song)#plays the mp3 file
        artistg,songg=questions()#asks user input for artist and song
        score_total+= check_answer(artistg,songg,song)#checks and allocates points   
        
    print(f"Here is your score: {score_total}")#prints score
    print("Great Job!")#prints great job
    print("")
    display_game_menu()
main()