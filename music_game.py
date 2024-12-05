import os
import random
import pygame

def choose_random_file(directory):
    '''Chooses a random file from directory'''
    # List all files in the given directory
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
    # Set up directory to the correct place
    script_dir = os.path.dirname(__file__)
    mp3_dir = os.path.join(script_dir, "mp3_lib")
    random_file = choose_random_file(mp3_dir)
    print(f"Randomly selected file: {random_file}")
    play_music(random_file)
main()