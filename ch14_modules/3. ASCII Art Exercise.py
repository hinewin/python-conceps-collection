from pyfiglet import figlet_format
from termcolor import colored

def print_art(msg,color):
    valid_colors = ("red","green","yellow","blue","magenta","cyan")
    
    if color not in valid_colors:
        color= "magenta"
    art = figlet_format(msg)
    colored_art = colored(art, color= color)
    print (colored_art)

msg = input("What message do you want to print? ")
color = input("What color? ")

print (print_art(msg,color))