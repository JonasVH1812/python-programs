import pygame
gegeveninput = 0

pygame.mixer.init()
while True:
    gegeveninput = str(input("ja of nee: "))
    if gegeveninput.lower() == "ja":
        pygame.mixer.music.load('allah.mp3')
        pygame.mixer.music.play()
        input('press enter to exit')
    else:
        print("ok")
    gegeveninput = "niks"