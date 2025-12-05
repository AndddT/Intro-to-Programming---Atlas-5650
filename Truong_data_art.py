
""" 
AI Assistance: I initially used Claude to explain concepts and functions I did not understand like bllit(), flip(), the coffee shop example and then how to use the template
from lab 8 in the While Loop. Claude was then used to help generate code that I was unsure how to properly write.

AI Generated Snippets:
self.x = random.randint(1,599)
self.y = random.randint(1,799)

with open("KPoP.csv", encoding='utf-8',newline='') as csvfile: (Claude was used here since I was unsure why my data was not being read in properly)

screen.blit(scaled_image, (self.x, self.y)) (Claude was used here since I loaded my images but did not know how to reshape them) """

# Importing everything necessary
import csv
import pygame 
import random
import visual_objects
import sys




#==========================================================
# Setting up Pygame
#==========================================================
screen = pygame.display.set_mode((600,800))
pygame.display.set_caption("Kpop Music")

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
# Importing in the classes from visual_objects 
from visual_objects import musicNote, musicStaffLines


# ===========================================================
# Reading in data 
# ===========================================================
musicNoteData = [] #Creating an emppty list to store the data 
#Grabbing danceability, energy and tempo from the data set 
with open("KPoP.csv", encoding='utf-8',newline='') as csvfile: #Claude assisted since I was unsure why the file was not being read in properly
    file = csv.reader(csvfile, delimiter = ',',quotechar = '"')
    next(file)
# Creating a for loop to loop through the data 
    for row in file: 
        danceability = float(row[12]) 
        energy = float(row[13])
        tempo = float(row[22])
        musicNoteData.append(musicNote(danceability, energy, tempo)) #Appending the musicNoteDataList and calling musicNote class. 

#Creates a list of lines, that will appear across the image like a music staff
linePositions = []
linePositions.append(musicStaffLines((0,50), (600,50), BLACK, 10)) #The staff lines will go across the screen, be black and have a thickness of 10. The image will looks like it has 3 groupings of staff lines
linePositions.append(musicStaffLines((0,100), (600,100), BLACK, 10)) # This is group 1 across the top 
linePositions.append(musicStaffLines((0,150), (600, 150), BLACK, 10))

linePositions.append(musicStaffLines((0,400), (600,400), BLACK, 10)) # This is group 2 across the middle 
linePositions.append(musicStaffLines((0,350), (600,350), BLACK, 10))
linePositions.append(musicStaffLines((0,450), (600, 450), BLACK, 10))


linePositions.append(musicStaffLines((0,650), (600,650), BLACK, 10)) # This is group 3 across the bottom 
linePositions.append(musicStaffLines((0,700), (600,700), BLACK, 10))
linePositions.append(musicStaffLines((0,750), (600, 750), BLACK, 10))



if __name__ == "__main__":
    while running:
# ----------------------------------------
# EVENT HANDLING
# ----------------------------------------
# Taken from the templkate for Lab 8 
        for event in pygame.event.get():
                # Check if user wants to quit
                if event.type == pygame.QUIT:
                    running = False


        screen.fill(WHITE) #Changing the background to white so the notes pop more 

      

        for note in musicNoteData: #Looping through the musicNoteData list and calling all functions to draw notes 
            note.determineColor() # First figures out the color of the note
            note.determineSize() # Then checks the size of the note 
            note.determineType() # Then checks the type of the note 
            note.drawImages(screen) #Then draws the note itself 

        for line in linePositions: #Looping through the list of line positions and then drawing them to the screen 
            line.drawLines(screen)
        
    
        pygame.display.flip() 
        clock.tick(FPS)
    


 # ========================================
 # CLEANUP - End the game properly
# ========================================
    pygame.quit()
    sys.exit()
