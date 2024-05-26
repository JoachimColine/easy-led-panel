import pygame
import sys
import time

parameters = { 
              'num_leds'     : 800,  # total leds count (multiple of 8)
              'window_width' : 950, # pygame window width (pixels)
              'window_height': 130,  # pygame window height (pixels)
              'led_size'     : 7,    # individual led size (pixels) 
              'led_spacing'  : 1     # spacing between leds (pixels)
             }

def loop(program):
    # Initialize leds array
    leds = []
    color = [0,0,0]
    for i in range(parameters['num_leds']):
        leds.append(color)

    # Initialize Pygame
    pygame.init()

    # Set up the window dimensions
    window = pygame.display.set_mode((parameters['window_width'], parameters['window_height']))
    pygame.display.set_caption("LED simulator")

    # Main game loop
    while True:
        # Handle events
        handleEvents()

        # Run the program
        program(leds)
 
def show(leds):
    # leds array length should be a multiple of 8. 
    if (len(leds) % 8):
        return
        
    # Read display parameters
    led_spacing = parameters['led_spacing']
    led_size = parameters['led_size']
    center_x = parameters['window_width'] // 2   # Centered horizontally
    center_y = parameters['window_height'] // 2  # Centered vertically
    leds_per_strip = len(leds) // 8
    
    # Paint window using leds array
    for i in range(8):
        for j in range(leds_per_strip):
            current_position_x = center_x - ((leds_per_strip // 2) - j) * (led_size + 2 * led_spacing)
            current_position_y = center_y - (4 - i) * (led_size + 2 * led_spacing)
            pygame.draw.rect(pygame.display.get_surface(), leds[i * leds_per_strip + j], 
                             (current_position_x, current_position_y, led_size, led_size))

    # Update the display
    pygame.display.update()
    
    # Handle events
    handleEvents()
            
def delay (milliseconds):
    time.sleep(milliseconds * 0.001)
    
def handleEvents():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()