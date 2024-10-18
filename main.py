from artV2 import *

# from art import *
from time import sleep as wait
from pygame import mixer
from defs import *
clear()
print("\n"*10)

SPEED = 150
SLOW_RATE = 0.92
SPEED_LIMIT = 3
BARREL_CAPACITY =6

mixer.init()
mixer.music.load("au/BGmusic.mp3")
mixer.music.set_volume(0.1)
mixer.music.play(-1)
clock = mixer.Sound("au/BGtick.mp3")
clock.set_volume(1.5)
clock.play(-1)
rrr = mixer.Sound("au/BGsound.mp3")
rrr.set_volume(0.6)
rrr.play(-1)
hbeat = mixer.Sound("au/beat.mp3")
hbeat.set_volume(0.3)
hbeat.play(-1)
typer = mixer.Sound("au/typing.mp3")

win = mixer.Sound("au/win.mp3")
boom = mixer.Sound("au/bang1.mp3")
tick = mixer.Sound("au/tick.mp3")



def manipulateVolume(stressLevel):
  global mixer, clock, rrr, hbeat
  mixer.music.set_volume((1-stressLevel)/2)
  clock.set_volume(stressLevel)
  rrr.set_volume(stressLevel)
  hbeat.set_volume(stressLevel)
  
def animateRotation(barrel):
  Speed = SPEED
  while True:
    for space in range(len(barrel)):
      tick.play()
      
      if (barrel[space]):
        show(GUN_ROTATING1_BL)
      elif (barrel[space-1]):
        show(GUN_ROTATING1_PL)
      else:
        show(GUN_ROTATING1)
      wait(1/Speed/3)
      
      
      if (barrel[space]):
        show(GUN_LOADED)
      else:
        show(GUN_UNLOADED)
      wait(1/Speed/3)
      
      if (barrel[space+1]):
        show(GUN_ROTATING2_BL)
      elif (barrel[space]):
        show(GUN_ROTATING2_PL)
      else:
        show(GUN_ROTATING2)
      wait(1/Speed/3)
      
      
      last = barrel[space]
      Speed *= SLOW_RATE
      
      stress = 1 - Speed / SPEED
      manipulateVolume(stress)
      
      if (Speed < SPEED_LIMIT):
        wait(0.3)
        if (barrel[space]):
          show(GUN_LOADED)
        else:
          show(GUN_UNLOADED)
        return last
  


manipulateVolume(0.5)
Sprint("Welcome to my little game.", typer, 3)
Sprint("This is a game about luck.", typer, 3)
manipulateVolume(0.1)
Sprint("This is a game about a chance.", typer, 3)
manipulateVolume(0.15)
Sprint("This is a game about a gun.", typer, 4)
manipulateVolume(0.6)
Sprint("A loaded gun.", typer, 4)
manipulateVolume(0.7)
Sprint("...", typer, 1)
Sprint("Do you have luck?", typer, 3)
manipulateVolume(0.9)
Sinput(typer, 2)
manipulateVolume(0.95)
Sprint("Lets check it...", typer, 3)





BARREL = initBarrel(BARREL_CAPACITY)
last = None

while True:
  manipulateVolume(0.05)
  if (last!=None):
    input()
  manipulateVolume(0.5)
  
  last = animateRotation(randomizeArrayOrder(BARREL))
  
  if last:
    Sprint("G.G.", typer)
    boom.play()
    kill()
  else:
    Sprint("You are fine... try again (Enter)", typer)
    win.play()