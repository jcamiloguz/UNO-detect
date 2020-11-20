import numpy as np
from playsound import playsound

def playCards(number, color, audiosPath):
    playsound(audiosPath[11][0])
    for audioPath in audiosPath:
        if audioPath[1] == str(number):
            playsound(audioPath[0])
        if audioPath[1] == color:
            playsound(audioPath[0])


