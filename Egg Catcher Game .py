# egg catcher game

    
from itertools import cycle
from random import randrange
from tkinter import Canvas, Tk, messagebox, font

canvas_width = 800
canvas_height = 400

root = Tk()
c = Canvas(root, width=canvas_width, height=canvas_height, background="deep sky blue")
c.create_rectangle(-5, canvas_height-100, canvas_width+5, canvas_height+5, fill="sea green", width=0)
c.create_oval(-80, -80, 120, 120, fill='orange', width=0)
c.pack()

color_cycle = cycle(["light blue", "light green", "light pink", "light yellow", "light cyan"])
egg_width = 45
egg_height = 55
egg_score = 10
egg_speed = 500
egg_interval = 4000
difficulty = 0.95
catcher_color = "blue"
catcher_width = 100
catcher_height = 100
catcher_startx = canvas_width / 2 - catcher_width / 2
catcher_starty = canvas_height - catcher_height - 20
catcher_startx2 = catcher_startx + catcher_width
catcher_starty2 = catcher_starty + catcher_height

catcher = c.create_arc(catcher_startx, catcher_starty, catcher_startx2, catcher_starty2, start=200, extent=140, style="arc", outline=catcher_color, width=3)
game_font = font.nametofont("TkFixedFont")
game_font.config(size=18)


score = 0
score_text = c.create_text(10, 10, anchor="nw", font=game_font, fill="darkblue", text="Score: "+ str(score))

lives_remaining = 3
lives_text = c.create_text(canvas_width-10, 10, anchor="ne", font=game_font, fill="darkblue", text="Lives: "+ str(lives_remaining))

eggs = []

def create_egg():
    x = randrange(10, 740)
    y = 40
    new_egg = c.create_oval(x, y, x+egg_width, y+egg_height, fill=next(color_cycle), width=0)
    eggs.append(new_egg)
    root.after(egg_interval, create_egg)

def move_eggs():
    for egg in eggs:
        (eggx, eggy, eggx2, eggy2) = c.coords(egg)
        c.move(egg, 0, 10)
        if eggy2 > canvas_height:
            egg_dropped(egg)
    root.after(egg_speed, move_eggs)

def egg_dropped(egg):
    eggs.remove(egg)
    c.delete(egg)
    lose_a_life()
    if lives_remaining == 0:
        messagebox.showinfo("Game Over!", "Final Score: "+ str(score))
        root.destroy()

def lose_a_life():
    global lives_remaining
    lives_remaining -= 1
    c.itemconfigure(lives_text, text="Lives: "+ str(lives_remaining))

def check_catch():
    (catcherx, catchery, catcherx2, catchery2) = c.coords(catcher)
    for egg in eggs:
        (eggx, eggy, eggx2, eggy2) = c.coords(egg)
        if catcherx < eggx and eggx2 < catcherx2 and catchery2 - eggy2 < 40:
            eggs.remove(egg)
            c.delete(egg)
            increase_score(egg_score)
    root.after(100, check_catch)

def increase_score(points):
    global score, egg_speed, egg_interval
    score += points
    egg_speed = int(egg_speed * difficulty)
    egg_interval = int(egg_interval * difficulty)
    c.itemconfigure(score_text, text="Score: "+ str(score))

def move_left(event):
    (x1, y1, x2, y2) = c.coords(catcher)
    if x1 > 0:
        c.move(catcher, -20, 0)

def move_right(event):
    (x1, y1, x2, y2) = c.coords(catcher)
    if x2 < canvas_width:
        c.move(catcher, 20, 0)

c.bind("<Left>", move_left)
c.bind("<Right>", move_right)
c.focus_set()
root.after(1000, create_egg)
root.after(1000, move_eggs)
root.after(1000, check_catch)
root.mainloop()


# from itertools import cycle
# from random import randrange
# import tkinter as tk
# from tkinter import messagebox, font

# # Constants
# CANVAS_WIDTH = 800
# CANVAS_HEIGHT = 400
# EGG_WIDTH = 45
# EGG_HEIGHT = 55
# EGG_SCORE = 10
# EGG_SPEED = 500
# EGG_INTERVAL = 4000
# DIFFICULTY = 0.95
# CATCHER_COLOR = "blue"
# CATCHER_WIDTH = 100
# CATCHER_HEIGHT = 100
# LIVES_REMAINING = 3

# # Initialize tkinter
# root = tk.Tk()
# root.title("Egg Catcher")

# # Set up canvas
# canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg="deep sky blue")
# canvas.pack()

# # Game fonts
# game_font = font.Font(family='Helvetica', size=18, weight='bold')

# # Variables
# score = 0
# lives_remaining = LIVES_REMAINING
# eggs = []
# color_cycle = cycle(["light blue", "light green", "light pink", "light yellow", "light cyan"])

# # Functions
# def create_egg():
#     x = randrange(10, CANVAS_WIDTH - EGG_WIDTH - 10)
#     y = 40
#     egg = canvas.create_oval(x, y, x + EGG_WIDTH, y + EGG_HEIGHT, fill=next(color_cycle))
#     eggs.append(egg)
#     root.after(EGG_INTERVAL, create_egg)

# def move_eggs():
#     for egg in eggs:
#         canvas.move(egg, 0, 10)
#         x1, y1, x2, y2 = canvas.coords(egg)
#         if y2 > CANVAS_HEIGHT:
#             egg_dropped(egg)
#     root.after(EGG_SPEED, move_eggs)

# def egg_dropped(egg):
#     eggs.remove(egg)
#     canvas.delete(egg)
#     lose_a_life()
#     if lives_remaining == 0:
#         messagebox.showinfo("Game Over!", f"Final Score: {score}")
#         root.destroy()

# def lose_a_life():
#     global lives_remaining
#     lives_remaining -= 1

# def check_catch():
#     catcher_coords = canvas.coords(catcher)
#     for egg in eggs:
#         egg_coords = canvas.coords(egg)
#         if catcher_coords[0] < egg_coords[0] and catcher_coords[2] > egg_coords[2] and \
#                 catcher_coords[3] - egg_coords[3] < 40:
#             eggs.remove(egg)
#             canvas.delete(egg)
#             increase_score(EGG_SCORE)
#     root.after(100, check_catch)

# def increase_score(points):
#     global score, EGG_SPEED, EGG_INTERVAL
#     score += points
#     EGG_SPEED = int(EGG_SPEED * DIFFICULTY)
#     EGG_INTERVAL = int(EGG_INTERVAL * DIFFICULTY)

# def move_left(event):
#     x1, _, _, _ = canvas.coords(catcher)
#     if x1 > 0:
#         canvas.move(catcher, -20, 0)

# def move_right(event):
#     _, _, x2, _ = canvas.coords(catcher)
#     if x2 < CANVAS_WIDTH:
#         canvas.move(catcher, 20, 0)

# # Create catcher
# catcher = canvas.create_arc(CANVAS_WIDTH / 2 - CATCHER_WIDTH / 2, CANVAS_HEIGHT - CATCHER_HEIGHT - 20,
#                             CANVAS_WIDTH / 2 + CATCHER_WIDTH / 2, CANVAS_HEIGHT - 20,
#                             start=200, extent=140, style="arc", outline=CATCHER_COLOR, width=3)

# # Bind keyboard events
# root.bind("<Left>", move_left)
# root.bind("<Right>", move_right)
# canvas.focus_set()

# # Start game
# root.after(1000, create_egg)
# root.after(1000, move_eggs)
# root.after(1000, check_catch)

# # Run the game
# root.mainloop()
