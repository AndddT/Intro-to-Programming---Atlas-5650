import pygame
import sys
import random

# Positive Engegament features is asking the user if they would like to take a break at game and telling them 
# what skills they learned and how they can improve.  A function is used to display the skills box

# Welcome to a new and exciting racing game! In this game you are a plant racing against obstacles as you
# try to make it across the finish line. Avoid other racers in Red to avoid being set back to the center lane
# and try to collect as many coins as you can to get a high score.!

# Initialize Pygame

pygame.init()

#=============================
# Initial Game Set up
#=============================
# Screen dimensions
screen_Width = 800
screen_Height = 600

# Set up the display window
screen = pygame.display.set_mode((screen_Width, screen_Height))
pygame.display.set_caption("Plant Racing Game")

# Set up the clock for controlling frame rate
clock = pygame.time.Clock()

# Colors (RGB format: Red, Green, Blue)
GREEN = (34,139,34)
WHITE = (255, 255, 255) 
RED = (255, 0, 0)
DARK_GREEN = (0, 200, 0)

# Create font 
font = pygame.font.Font(None, 36)

target_distance = 3000
race_complete = False 
large_font = pygame.font.Font(None, 72)


# ========================================
# CONSTANTS - Define once, use everywhere
# ========================================
lane_positions = [250, 400, 550]
current_lane = 1 
player_x = lane_positions[current_lane]
player_y = 450
player_width = 50
player_height = 50
distance = 0 
max_opponents = 5 
paused = False

# Target Distance 
# --------------------------------------
target_distance = 3000
race_complete = False

# Adding a question to see if the user wants to take a break 

first_completion = True
race_complete = False #Is this the first time finishing 
showing_break_prompt = False #Is the prompt currently displayed 
 

scroll_speed = 5 
markers = [0, 150, 300, 450]

# Player Speed
# ---------------------------------------
player_speed = 5 #Current Speed
min_speed = 2 #Can't go slower than this 
max_speed = 10 #how Quickly speed changes 
acceleration = 0.2 

# Create oppononents 
# ---------------------------------------
opponents = []
for i in range(max_opponents):
    lane = random.randint(0,2)
    y_pos = -100 - (i * 300)
    speed = random.randint(3,7)
    opponents.append([lane, y_pos, speed])


# Adding Items
#---------------------------------------------
# Item variables  
score = 0 
item_width = 30
item_height = 30
max_items = 8
items = []

#Create Items list
items = []
for i in range(max_items):
    lane = random.randint(0,2) # Random Lane (0,1 or 2)
    y_pos = -200 - (i *400) # Space 400 pixels apart
    items.append([lane, y_pos])

# Frame rate
FPS = 60
#========================================
# Functions
#========================================
def display_skills_message(screen):
    line1_text = font.render("You have learned quick reflexes", True, WHITE)
    line1_rect = line1_text.get_rect(center=(screen_Width // 2, screen_Height // 2 + 100))
    screen.blit(line1_text, line1_rect)
    
    # Second line
    line2_text = font.render("but should work on completing the course faster.", True, WHITE)
    line2_rect = line2_text.get_rect(center=(screen_Width // 2, screen_Height // 2 + 140))
    screen.blit(line2_text, line2_rect)


# ========================================
# MAIN GAME LOOP
# ========================================

running = True
while running:
    # 1. EVENT HANDLING
    # ----------------------------------------
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #Adding Pause button
    #--------------------------------------------

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                paused = not paused 
        
        if event.type == pygame.KEYDOWN:
            if showing_break_prompt:
                if event.key == pygame.K_y:
                    print("Y pressed")
                    showing_break_prompt = False
                    paused = True
                if event.key == pygame.K_n:
                    print("N pressed")
                    showing_break_prompt = False

        # Only allow lane changes if race not complete 
        if event.type == pygame.KEYDOWN and not race_complete:
            if event.key == pygame.K_LEFT and current_lane > 0:
                current_lane -= 1
            if event.key == pygame.K_RIGHT and current_lane < 2:
                current_lane += 1
    
  
    # 2. GAME LOGIC
    # ----------------------------------------
    if not race_complete and not paused and not showing_break_prompt:
        #Speed control
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            player_speed += acceleration
        if keys[pygame.K_DOWN]:
            player_speed -= acceleration
    
        if player_speed < min_speed:
            player_speed = min_speed
        if player_speed > max_speed:
            player_speed = max_speed 
        # Update distance 
        distance += player_speed / 5

    
    #Check for finish
    #------------------------------------------
        if distance >= target_distance:
            race_complete = True

            if first_completion:
                showing_break_prompt = True 
                first_completion = False 


    # Updates player position and opponent's position
    # --------------------------------------------
        player_x = lane_positions[current_lane]

    # update track markers (scrollig effect)
        for i in range(len(markers)):
            markers[i] += player_speed
            if markers[i] > screen_Height:
                markers[i] = -50
    

    # Update opponents 
        for opponent in opponents:
            opponent[1] += opponent[2] + player_speed

            if opponent[1] > screen_Height:
                opponent[1] = random.randint( -500, -100)
                opponent[0] = random.randint(0,2)
                opponent[2] = random.randint(3,7)

    #Update Items
    # ---------------------------------------------------
        for item in items:
            item[1] += player_speed

            if item[1] > screen_Height:
                item[1] = random.randint(-500, -100)
                item[0] = random.randint(0, 2)

    # Remove off screen items 
        items_to_keep = []
        for item in items:
            if item[1] < screen_Height +50:
                items_to_keep.append(item)
        items = items_to_keep




    # Collision Checking
    # ---------------------------------------------

        for opponent in opponents:
            # Check if in the same lane 
            if current_lane == opponent[0]:
                if (player_y < opponent[1] + 50 and player_y + player_height > opponent[1]):
                    current_lane = 1
                    player_x = lane_positions[current_lane]

        for item in items:
            if current_lane == item[0]:
                if (player_y < item[1] + item_height and 
                    player_y + player_height > item[1]):
                    score += 10
                    item[1] = 10000

    # 3. DRAWING
    # ----------------------------------------\
    screen.fill(GREEN)
    
    #Draw Track Markers 
    for marker_y in markers:
        # Left Lane Divider 
        pygame.draw.rect(screen, WHITE, (300, marker_y, 10, 40))
        # Right Lane Divider 
        pygame.draw.rect(screen, WHITE, (490, marker_y, 10, 40))

    #Draw opponents 
    for opponent in opponents:
        opp_lane = opponent[0]
        opp_y = opponent[1]
        opp_x = lane_positions[opp_lane]
        pygame.draw.rect(screen, (255, 0, 0), (opp_x, opp_y, 50, 50))

    #Drawing items
    for item in items:
        item_lane = item[0]
        item_y = item[1]
        item_x = lane_positions[item_lane]
        pygame.draw.rect(screen, (255, 255, 0), (item_x, item_y, item_width, item_height))
    
    #Draw player 
    pygame.draw.rect(screen, (255, 0, 0), (player_x, player_y, 50, 50))

    # Draw stats
    distance_text = font.render("Distance: " + str(int(distance)), True, (255, 255, 255))
    screen.blit(distance_text, (10,10))

    speed_text = font.render("speed: " + str(int(player_speed)) , True, (255, 255, 255))
    screen.blit(speed_text, (10,50))

    #Draw score 
    score_text = font.render("Score: " + str(score), True, WHITE)
    screen.blit(score_text, (10, 90))

    if race_complete and not showing_break_prompt:
        complete_text = large_font.render("Race Complete!", True, (255,255,0))
        text_rect = complete_text.get_rect(center=(screen_Width // 2, screen_Height //2))
        screen.blit(complete_text, text_rect)

    # #Draw feedback message
        display_skills_message(screen)

    #Draw Break prompt
    if showing_break_prompt:
       prompt_text = large_font.render("Would you like a break?", True, (255, 255, 0))
       prompt_rect = prompt_text.get_rect(center=(screen_Width // 2, screen_Height // 2))
       screen.blit(prompt_text, prompt_rect)

       instruction_text = font.render("Press Y for Yes, N for No", True, WHITE)
       instruction_rect = instruction_text.get_rect(center=(screen_Width // 2, screen_Height // 2 + 80))
       screen.blit(instruction_text, instruction_rect)


    if paused:
        pause_text = large_font.render("PAUSED", True, (255, 255, 0))
        pause_rect = pause_text.get_rect(center=(screen_Width // 2, screen_Height//2))
        screen.blit(pause_text, pause_rect)
    
    
    # Update the display
    pygame.display.flip()
    clock.tick(FPS)


# ========================================
# CLEANUP - End the game properly
# ========================================
pygame.quit()
sys.exit()


