import pygame
import random

pygame.init()
screen = pygame.display.set_mode((400, 400))

balloon_colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)] # red, green, blue
balloon_width = 20
balloon_height = 30
num_balloons = 10

# create a list to store the balloon rectangles
balloons = []

# draw the balloons
for i in range(num_balloons):
    x = random.randint(0, screen.get_width() - balloon_width)
    y = random.randint(screen.get_height() // 2, screen.get_height() - balloon_height)
    color = random.choice(balloon_colors)
    balloon_rect = pygame.draw.ellipse(screen, color, (x, y, balloon_width, balloon_height))
    
    # draw the tail
    tail_start_x = x + balloon_width // 2 
    tail_start_y = y + balloon_height 
    tail_end_x = tail_start_x 
    tail_end_y = tail_start_y + random.randint(10,+20) 
    pygame.draw.line(screen,color,(tail_start_x,tail_start_y),(tail_end_x,tail_end_y))
    
    balloons.append((balloon_rect,color))

# initialize the counter
counter = 0

# create a font object for displaying text
font = pygame.font.Font(None,36)

# update the display
pygame.display.flip()

# main game loop
while True:
    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        # handle mouse clicks
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            for i in range(len(balloons)):
                balloon_rect,color = balloons[i]
                if balloon_rect.collidepoint(mouse_pos):
                    # remove the balloon from the list
                    balloons.pop(i)
                    
                    # increment the counter
                    counter += 1
                    
                    break
    
    # move the balloons upwards
    for i in range(len(balloons)):
        balloon_rect,color = balloons[i]
        balloon_rect.move_ip(0,-5)
        if balloon_rect.bottom < 0:
            # move the balloon back to the bottom of the screen
            balloon_rect.bottom = screen.get_height()
    
    # clear the screen
    screen.fill((255,255,255))
    
    # redraw the balloons and their tails
    for i in range(len(balloons)):
        balloon_rect,color = balloons[i]
        
        pygame.draw.ellipse(screen,color,balloon_rect)
        
        # draw the tail attached to the bottom center of the balloon rectangle 
        tail_start_x = balloon_rect.x + balloon_width // 2 
        tail_start_y = balloon_rect.y + balloon_height 
        tail_end_x = tail_start_x 
        tail_end_y = tail_start_y + random.randint(10,+20) 
        pygame.draw.line(screen,color,(tail_start_x,tail_start_y),(tail_end_x,tail_end_y))
    
    # display the score on the screen
    score_text = font.render("Score: "+str(counter),True,(0,0,0))
    screen.blit(score_text,(5,5))
    
    # update the display
    pygame.display.flip()
    
    # wait for a while
    pygame.time.wait(100)
