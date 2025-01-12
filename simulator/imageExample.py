from PIL import Image

import simulator
PAUSE = 100 # milliseconds 
ANIMATION_PAUSE = 200
DOG_IMAGE="simulator/dog.png"
FRAME1="simulator/bird1.png"
FRAME2="simulator/bird2.png"

BIRD="simulator/bird3.png"
ROCKET="simulator/rocket.png"
ROCKET2="simulator/rocket2.png"

OUTPUT_RGB_VALS = "table.txt"
# https://www.pixilart.com/draw

def get_rgb_array(leds):
    # dismiss transparency channel
    values = [vals[:3] for vals in leds]
    return values

def rgb_to_hex(rb_values):
    """Return color as #rrggbb for the given color values."""
    return ['#%02x%02x%02x' % (red, green, blue) for (red, green, blue) in rb_values]

def save_rgb_matrix(leds):
    rgb_values = get_rgb_array(leds)
    hex_values = rgb_to_hex(rgb_values)
    hex_str = "{"
    while hex_values:
        vals = hex_values[:10]
        str_list = [f'{int(x)}' for x in vals]
        hex_str += ",".join(str_list) + ",\n"
        hex_values = hex_values[10:]
    hex_str += "};\n"
    with open(OUTPUT_RGB_VALS, 'w') as f:
        f.write(hex_str)


# Helper to shift all LEDs to the left.
def allStripsMove(leds, direction=None):
    if direction not in ['right', 'left']:
        raise ValueError()
    ledsPerStrip = len(leds) // 8
    for row_count in range(8):
        if direction == "left":
            # From 0 to  ledsPerStrip - 1, step = 1
            for j in range(0, ledsPerStrip - 1, 1):
                leds[row_count * ledsPerStrip + j] = leds[row_count * ledsPerStrip + j + 1]
        elif direction == "right":
            # reverse loop From ledsPerStrip to 0
            for j in range(ledsPerStrip -1, 0, -1):
                leds[row_count * ledsPerStrip + j] = leds[row_count * ledsPerStrip + j -1]

def load_image(image_path=None):
    im = Image.open(image_path) # Can be many different formats.
    width, height = im.size
    pixel_values = list(im.getdata())
    # for value in pixel_values:
    return pixel_values

def image_to_led(leds):
    # bird = FRAME3
    pixel_values = load_image(image_path=ROCKET)
    for idx in range(len(leds)):
        leds[idx] = pixel_values[idx]
    simulator.show(leds)
    simulator.delay(PAUSE)
    # for idx in range(150):
    #     allStripsMove(leds, direction="right")
    #     simulator.show(leds)
    #     simulator.delay(PAUSE)
    save_rgb_matrix(leds)


def animate(leds):
    pixel_values_1 = load_image(image_path=FRAME1)
    pixel_values_2 = load_image(image_path=FRAME2)
    for idx in range(len(leds)):
        leds[idx] = pixel_values_1[idx]
    simulator.show(leds)
    simulator.delay(ANIMATION_PAUSE)
    for idx in range(len(leds)):
        leds[idx] = pixel_values_2[idx]
    simulator.show(leds)
    simulator.delay(ANIMATION_PAUSE)
    save_rgb_matrix(leds)

if __name__ == "__main__":
    simulator.loop(image_to_led)
    # simulator.loop(animate)