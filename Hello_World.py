import displaylink

# Initialize the DisplayLink screens
display1 = displaylink.DisplayLink(index=0)
display2 = displaylink.DisplayLink(index=1)
display1.begin()
display2.begin()

# Set the cursor position for each screen
display1.setCursor(0, 0)
display2.setCursor(0, 0)

# Display the text on each screen
display1.print("Hello, World!")
display2.print("Hello, World!")
