import pyfiglet
import termcolor

valid_colors = ("red", "green", "yellow", "blue", "magenta", "cyan", "white")

words = pyfiglet.figlet_format(input("What would you like to print? "))
col = input("What color?: ")
bc = input("What background?: ")

if col not in valid_colors:
    col = "magenta"
if bc not in valid_colors:
    bc = "yellow"

background = "on_" + bc
output = termcolor.colored(words, color=col, on_color=background)
print(output)
