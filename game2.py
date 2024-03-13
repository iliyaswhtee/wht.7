import os
import pygame
from pygame import mixer

pygame.init()

mixer.init()

songs = ["C:\pp2 lab 7\song1.piano.mp3", "C:\pp2 lab 7\mocart-tureckijj-marsh.mp3", "C:\pp2 lab 7\Sia_Snowman.mp3"]
song_index = 0

def play_song(song_index):
    mixer.music.load(songs[song_index])
    mixer.music.play()

while True:
    command = input("Enter command (p: play, s: stop, n: next, b: previous, x: exit, u: pause, r: resume ): ")
    if command == 'p':  
        play_song(song_index)
    elif command == 's':  
        mixer.music.stop()
    elif command == 'u':
        mixer.music.pause()
    elif command == 'r':
        mixer.music.unpause()
    elif command == 'n':  
        song_index = (song_index + 1) % len(songs)
        play_song(song_index)
    elif command == 'b': 
        song_index = (song_index - 1) % len(songs)
        play_song(song_index)
    elif command == 'x': 
        mixer.music.quit()