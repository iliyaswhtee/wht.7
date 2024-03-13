import pygame
from pygame import mixer
import keyboard

pygame.init()

mixer.init()

songs = ["C:\pp2 lab 7\song1.piano.mp3", "C:\pp2 lab 7\mocart-tureckijj-marsh.mp3", "C:\pp2 lab 7\Sia_Snowman.mp3"]
song_index = 0

def play_song(song_index):
    mixer.music.load(songs[song_index])
    mixer.music.play()

while True:
    if keyboard.is_pressed('p'):  
        play_song(song_index)
    elif keyboard.is_pressed('x'):
        mixer.music.exit()
    elif keyboard.is_pressed('s'):  
        mixer.music.stop()
    elif keyboard.is_pressed('n'):  
        song_index = (song_index + 1) % len(songs)
        play_song(song_index)
    elif keyboard.is_pressed('b'):  
        song_index = (song_index - 1) % len(songs)
        play_song(song_index)