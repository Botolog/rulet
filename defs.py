import os
from time import sleep as wait
import random as rnd

def initBarrel(n):
  return [False]*(n-1)+[True]

def randomizeArrayOrder(array):
  for i in range(len(array)):
    j = rnd.randint(0, len(array) - 1)
    array[i], array[j] = array[j], array[i]
  return array*10000

def clear():
  os.system('cls' if os.name == 'nt' else 'clear')
  # print(chr(27) + "[2J")
  # print("\n"*5)
  # print("\r", end="")

def show(img):
  clear()
  print("\r"+img)
  
def Sprint(text, sound, dur=3):
  printed = ""
  for char in text:
    printed+=char
    sound.play()
    print(printed, end="                                            \r                          ")
    
    mod = 0
    if char == "." or char == "!" or char == "?":
      mod = 0.7
    elif char == ",":
      mod = 0.4
    elif char == " ":
      mod = -1
    wait(max(dur / len(text) + mod, 0))
  wait(1)
  print()
  
def kill():
  os._exit(0)