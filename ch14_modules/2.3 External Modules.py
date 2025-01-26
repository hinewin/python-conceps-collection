# use python -m pip install {module name} to install external pkg

from colorama import init
from termcolor import colored
init()
print (colored("HI THERE!",color ='yellow',on_color ='on_red',attrs= ['blink']))