import os
import random
import pygame
#get the mp3 in the files current dir C:\Users\ellie\Desktop\sandbox_111\vscode\Music_trivia


#print(os.getcwd())
# Initialize the mixer module
#pass in the directory
def choose_random_file(directory):
    '''Chooses a random file from directory'''
    #changes directory and lists files
    files = os.listdir(directory)
    # Filter out directories, only keep files
    files = [f for f in files if os.path.isfile(os.path.join(directory, f))]
    
    # Randomly select a file from the list
    random_file = random.choice(files)
    print(f"Selected file: {random_file}")
    return os.path.join(directory, random_file)
def play_music(random_file):
    '''Plays the music file'''
    pygame.mixer.init()
    pygame.mixer.music.load(random_file)
    pygame.mixer.music.play()
    # Wait for the music to finish playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    pygame.mixer.quit()
    return
def main():
    #sets up directory to the correct place
    random_file = choose_random_file("C://Users//ellie//Desktop//sandbox_111//vscode//Music_trivia//mp3_lib")
    print(f"Randomly selected file: {random_file}")
    play_music(random_file)

main()