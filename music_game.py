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
        if os.path.isfile(os.path.join(directory, f)):
            files.append(f)
    
    # Randomly select a file from the list
    random_file = random.choice(files)
    random_file = os.path.join(directory, random_file)
    return random_file
def directory_config(random_file):
    '''Configures the directory to the correct file path'''
    files= os.listdir(random_file)
    for file in files:
       selection = os.path.join(random_file, file)
    return selection
def play_music(random_file):
    '''Plays the music file'''
    pygame.mixer.init()
    pygame.mixer.music.load(random_file)
    pygame.mixer.music.play()
    # Wait for the music to finish playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)#10ms
    pygame.mixer.quit()
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
        print("Welcome to Music Trivia. The rules are simple. You will be presented with a song and you will have to guess the artist and the song name.")
        print("The game will run 5 times and allocate scores 1pt for artist and 1pt for song. Good luck!")#prints correct rules
        display_game_menu()
    elif choice == "2":
        os.system("cls")
        pass
    elif choice == "3":
        print("Goodbye!")
        display_game_menu()
    else:
        print("Invalid choice. Please try again.Option 1-3.")
        display_game_menu()
    return
def questions():
    '''Asks the user for the artist and song name'''
    artistg = input("Enter the artist name: ")
    songg = input("Enter the song name: ")
    return artistg,songg
def check_answer(artistg,songg,random_file,score):
    ''' 
    The answer matches the file structure.Makes artistg and songg lowercase.
    Extract file name from file path and remove underscores and makes it lower case assigning it to artist and song.
    Then runs comparison to see if artistg is the same as artist and songg is the same as song 
    then allocates point to score if they match.
    '''
    artistg=artistg.lower()
    songg=songg.lower()
    artist = random_file.split("\\")[-2].split("_")[0].lower()#changed for file format
    song = random_file.split("\\")[-1].split("_")[0].lower()#changed for file structure
    if artistg == artist:
        score += 1
        print("Artist is correct")
    else:
        print("Artist is incorrect")
    if songg == song:
        score += 1
        print("Song is correct")
    else:
        print("Song is incorrect")
    return score

def main():
    # Set up directory to the correct place
    os.chdir("mp3_lib")
    script_dir = os.path.dirname(__file__)
    mp3_dir = os.path.join(script_dir, "mp3_lib")
    #score accumulator
    score=0
    #display game menu
    display_game_menu()
    for i in range(5):
        random_file = choose_random_file(mp3_dir)
        random_mp3=directory_config(random_file)
        song=directory_config(random_mp3)
        play_music(song)
        artistg,songg=questions()
        score= check_answer(artistg,songg,random_mp3,score)
        os.system("cls")
    print(f"Here is your score: {score}")
    print("Great Job!")
main()