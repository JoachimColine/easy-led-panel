import simulator

def myAwesomeProgram(leds):
    # This is an example program.
    # Each item of the leds array is defined by [red, green, blue]. 
    # You are free to edit them like you want.
    # When you are done, call simulator.show(leds) to update the display.
    # Call simulator.delay() to pause program execution.
    RED   = [255, 0, 0]
    GREEN = [0, 255, 0]
    PAUSE = 100 # milliseconds 
    for i in range(len(leds)): # gradually fill with red
        leds[i] = RED
        simulator.show(leds)
        simulator.delay(PAUSE)
    for i in range(len(leds)): # gradually fill with green
        leds[i] = GREEN
        simulator.show(leds)
        simulator.delay(PAUSE)
    
if __name__ == "__main__":
    # Call your program here
    simulator.loop(myAwesomeProgram)