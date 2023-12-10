import random
import os
import pyfiglet


# Create a PyFiglet object
font = pyfiglet.Figlet(font='slant')

# Generate the ASCII art for the word "fortifyscan"
text1 = font.renderText("fortilistner")


# Create a PyFiglet object
font = pyfiglet.Figlet(font='banner')

# Generate the ASCII art for the word "fortifyscan"
text2 =   font.renderText("fortilistner")

    
# Create a PyFiglet object
font = pyfiglet.Figlet(font='slant')

# Generate the ASCII art for the word "fortifyscan"
text3 = font.renderText("fortilistner")

# Create a PyFiglet object
font = pyfiglet.Figlet(font='banner')

# Generate the ASCII art for the word "fortifyscan"
text4 = font.renderText("fortilistner")

# Create a PyFiglet object
font = pyfiglet.Figlet(font='banner')

# Generate the ASCII art for the word "fortifyscan"
text5 = font.renderText("fortilistner")

rand = random.randrange(1,5)

if rand == 1:
	print(text1)
elif rand == 2:
	print(text2)
elif rand == 3:
	print(text3)
elif rand == 4:
	print(text4)
elif rand == 5:
	print(text5)