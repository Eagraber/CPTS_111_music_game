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

GAME RULES:
The objective of the game is to correctly guess the artist and song title of a music clip within 30 seconds. You receive 1 point for guessing the correct artist and 1 point for the correct song title. After 30 seconds, the song will end, and you will type in your guess. Your points will be awarded accordingly based off the accuracy of your guess. The next music clip will be played and, the process will continue repeating. 
