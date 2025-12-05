""" This script creates 2 classes MusicNote and musicStaffLines. MusicNote has 3 attributes, danceability, energy and tempo. The value of danceability determines whether the music note generated
is pink or green. The value of energy determines the size of the music note. The value of tempo determines if the music note appears as a quarter note or eigth note. The music notes will be 
placed according to randmomized X and Y values"""


#=================================================================
# Setting up class and functions 
#=================================================================

import csv
import pygame 
import random



class musicNote:
    def __init__(self,danceability, energy, tempo):
        # x and y are set to random numbers so music notes appear sporadically
        self.x = random.randint(1,599) # Claude assisted or the syntax to randomize the numbers. The limits were set as 1 - 599 on the X Axis and 1 - 799, so the notes do not appear off screen
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


    def drawImages(self, screen):
        """Loads the note images based on type of note and color and sizes them as well"""
        if self.type == "quarter":
        
            if self.color == "green":
                quarterNote = pygame.image.load("./greenQuarterNote.png")
            else:
                quarterNote = pygame.image.load("./pinkQuarterNote.png")
        elif self.type == "eigth":
        
            if self.color == "green":
                quarterNote = pygame.image.load("./greenEigthNote.png")
            else:
                quarterNote = pygame.image.load("./pinkEigthNote.png")



        if self.size == "small":
            scaled_image = pygame.transform.scale(quarterNote, (30, 30)) #Claude was used here to figure out the documentation on how to scale the music notes 
        else:
            scaled_image = pygame.transform.scale(quarterNote, (100, 100))

        screen.blit(scaled_image, (self.x, self.y))

class musicStaffLines:
    def __init__(self, start, end, color, thickness):
        self.start = start
        self.end = end
        self.color = color
        self.thickness = thickness

    def drawLines(self, surface):
        """This function will draw in staff lines for the art at the end)"""
        pygame.draw.line(surface,self.color, self.start, self.end, self.thickness)





