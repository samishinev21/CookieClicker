import pgzrun
import asyncio
import os

# Game settings
TITLE = "Cookie Clicker"
HEIGHT = 1296
WIDTH = 2289

os.environ['SDL_VIDEO_WINDOW_POS'] = 'center'

# Center position constants
CENTER_X = WIDTH / 2
CENTER_Y = HEIGHT / 2

# Global variables
clicks = 0

# Actor setup
cookie = Actor("cookie")
cookie.x = CENTER_X
cookie.y = CENTER_Y

# Pygame Zero draw function
def draw():
    screen.clear()
    screen.fill("cyan")
    cookie.draw()
    screen.draw.text(str(clicks), [CENTER_X, CENTER_Y - 350], color="black", fontsize=100)


# Pygame Zero mouse click detection
def on_mouse_down(pos):
    global clicks
    if cookie.collidepoint(pos):
        cookie.image = "cookie"  # Reset image after click
        clicks += 1


# Pygame Zero mouse release detection
def on_mouse_up(pos):
    cookie.image = "cookie"

pgzrun.go()
