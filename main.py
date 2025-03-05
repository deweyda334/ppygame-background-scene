# Pygame game template

import pygame
import sys
import config # Import the config module

def init_game():
    pygame.init()
    screen = pygame.display.set_mode((config.WINDOW_WIDTH, config.WINDOW_HEIGHT)) # Use constants from config
    pygame.display.set_caption(config.TITLE)
    return screen

def handle_events ():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return False
    return True


def draw_line(screen, line_color, start_point, end_point, width):
    pygame.draw.line(screen, line_color, start_point, end_point, width) 






def main():
    screen = init_game()
    clock = pygame.time.Clock() # Initialize the clock here
    running = True
    while running:
        running = handle_events()
        screen.fill(config.WHITE) # Use color from config

        # Call the function that draws a line on the screen 

        # Arguments for first line
        start_pos1 = [150, 150]
        end_pos1 = [350, 500]
        line_color1 = config.GREEN
        line_thickness1 = 10

        start_pos2 = [400, 350]
        end_pos2 = [225, 450]
        line_color2 = config.RED
        line_thickness2 = 6

        
        start_pos3 = [405, 250]
        end_pos3 = [325, 250]
        line_color3 = config.BLACK
        line_thickness3 = 9


        draw_line(screen, line_color1, start_pos1, end_pos1, line_thickness1)
        draw_line(screen, line_color2, start_pos2, end_pos2, line_thickness2)
        draw_line(screen, line_color3, start_pos3, end_pos3, line_thickness3)



        pygame.display.flip()

            # Limit the frame rate to the specifiied frames per second (FPS) 
        clock.tick(config.FPS)

    
    pygame.quit()
    sys.exit()

if __name__== "__main__":
    main()