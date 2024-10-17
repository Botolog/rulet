import os
from time import sleep as wait
import random as rnd

def randomizeArrayOrder(array):
  for i in range(len(array)):
    j = rnd.randint(0, len(array) - 1)
    array[i], array[j] = array[j], array[i]
  return array

def clear():
  os.system('cls' if os.name == 'nt' else 'clear')
  # print(chr(27) + "[2J")

def show(img):
  clear()
  print(img)
  
def Sprint(text, sound, dur=3):
  printed = ""
  for char in text:
    printed+=char
    sound.play()
    print(printed, end="                                            \r                          ")
    
    mod = 0
    if char == "." or char == "!" or char == "?":
      mod = 1
    elif char == ",":
      mod = 0.7
    elif char == " ":
      mod = -1
    wait(max(dur / len(text) + mod, 0))
  wait(1)
  print()