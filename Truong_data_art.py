"""This script will create classes that will draw pygame objects baseson on imported CSV data.
spotify_songs.csv is needed to run this code"""

""" AI Assistance: I initially used Claude to explain concepts and functions I did not understand
like bllit(), flip() and snippets of the coffee shop example. Claude was then used to help generate code that
I was unsure how to properly write.

AI Generated Snippets:
self.x = random.randint(1,599)
self.y = random.randint(1,799)

screen.blit(scaled_image, (self.x, self.y)) """

import csv
import pygame 
import random


#==========================================================
# Setting up Pygame
#==========================================================
screen = pygame.display.set_mode((600,800))
pygame.display.set_caption("Spotify Songs")

clock = pygame.time.Clock()
FPS = 60
#sets the frame rate 

# Colors
BLACK = (0,0,0)
WHITE = (255,255,255)

# Game control
running = True

#=================================================================
# Setting up class and functions 
#=================================================================

class musicNote:
    def __init__(self,danceability, energy, tempo):
        # x and y are set to random numbers so music notes appear sporadically
        self.x = random.randint(1,599)
        self.y = random.randint(1,799)
        self.danceability = danceability
        self.energy = energy
        self.tempo = tempo
         

    def determineColor(self):
        """Determines the color of the music note based on the danceability rating.
        Danceability ranges from .3 to 1. Danceability rating from .3 - .65 = Green, .65 - 1 = Pink"""
        if self.danceability < .65:
            self.color = "green"
        else:
            self.color = "pink"

    def determineSize(self):
        """Determines size of music note based on the energy rating. Energy ranges fron .2 - .6.
        Energy rating from .2 - .4 = 30 pixels, .4 - .6 = 100 pixels"""
        if self.energy < .4:
            self.size = "small"
        else:
            self.size = "big"

    def determineType(self):
        """Determines weather music note will be a quarter note ir eighth note. Tempo ranges from 68 - 180.
        Tempo rating 68 - 124 = quarter note, 124 - 180 = eigth note"""
        if self.tempo <= 124:
            self.type = "quarter"
        else:
            self.type = "eigth"


    def drawImages(self):
        """Loads the note images based on type of note and color and sizes them as well"""
        if self.type == "quarter":
        
            if self.color == "green":
                quarterNote = pygame.image.load("./greenQuarterNote.png")
            else:
                quarterNote = pygame.image.load("./pinkQuarterNote.png")
        if self.type == "eigth":
        
            if self.color == "green":
                quarterNote = pygame.image.load("./greenEigthNote.png")
            else:
                quarterNote = pygame.image.load("./pinkEigthNote.png")



        if self.size == "small":
            scaled_image = pygame.transform.scale(quarterNote, (30, 30))
        else:
            scaled_image = pygame.transform.scale(quarterNote, (100, 100))

        screen.blit(scaled_image, (self.x, self.y))


# ===========================================================
# Reading in data 
# ===========================================================
musicNoteData = [] #Creating an emppty list to store the data 
#Grabbing danceability, energy and tempo from the data set 
with open("KPoP.csv", encoding='utf-8',newline='') as csvfile:
    file = csv.reader(csvfile, delimiter = ',',quotechar = '"')
    next(file)
# Creating a for loop to loop through the data 
    for row in file:
        danceability = float(row[12])
        energy = float(row[13])
        tempo = float(row[22])
        musicNoteData.append(musicNote(danceability, energy, tempo)) #Appending the musicNoteDataList and calling musicNote class



if __name__ == "__main__":
    while running:
# ----------------------------------------
# EVENT HANDLING
# ----------------------------------------
        for event in pygame.event.get():
                # Check if user wants to quit
                if event.type == pygame.QUIT:
                    running = False


        screen.fill(WHITE) #changing the background to white so the notes pop more 

        for note in musicNoteData: #Looping through the musicNoteData list and calling all functions to draw notes 
            note.determineColor()
            note.determineSize()
            note.determineType()
            note.drawImages()
        pygame.display.flip()
        clock.tick(FPS)



 # ========================================
 # CLEANUP - End the game properly
# ========================================
    pygame.quit()
    sys.exit()



