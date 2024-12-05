import os
import random
import pygame
#get the mp3 in the files current dir C:\Users\ellie\Desktop\sandbox_111\vscode\Music_trivia

directory= os.chdir("C:/Users/ellie/Desktop/sandbox_111/vscode/Music_trivia/mp3_lib")
#print(os.getcwd())
# Initialize the mixer module
#pass
def choose_random_file(directory):
    # List all files in the given directory
    files = os.listdir(directory)
    
    # Filter out directories, only keep files
    files = [f for f in files if os.path.isfile(os.path.join(directory, f))]
    
    # Randomly select a file from the list
    random_file = random.choice(files)
    
    return random_file

# Example usage
directory = "C:/Users/ellie/Desktop/sandbox_111/vscode/Music_trivia/mp3_lib"
random_file = choose_random_file(directory)
print(f"Randomly selected file: {random_file}")
pygame.mixer.init()
# Implement the file
#with open("mp3_lib", 'r') as file_in:
	#pass  # Add code here to process the file if needed
# Load an MP3 file
#pygame.mixer.music.load('C:/Users/ellie/Desktop/sandbox_111/vscode/Music_trivia/mp3_file/')



