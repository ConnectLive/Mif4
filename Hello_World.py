import evdi
import numpy as np

# Define screen size
SCREEN_WIDTH = 1440
SCREEN_HEIGHT = 240

# Define message to be displayed
message = "Hello World"

# Create numpy array of the message to be displayed
message_array = np.zeros((SCREEN_HEIGHT, SCREEN_WIDTH, 3), dtype=np.uint8)
evdi.drawText(message_array, message, 0, 0, 255, 255, 255)

# Initialize evdi display for both screens
with evdi.DisplayManager() as dm:
    screen1 = dm.get_display(0)
    screen2 = dm.get_display(1)
    
    # Set screen resolutions
    screen1.set_resolution(SCREEN_WIDTH, SCREEN_HEIGHT)
    screen2.set_resolution(SCREEN_WIDTH, SCREEN_HEIGHT)
    
    # Display message on both screens
    screen1.draw(message_array)
    screen2.draw(message_array)
