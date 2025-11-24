import pygame
import random
import tkinter as tk
from tkinter import simpledialog


temp_root = tk.Tk()
temp_root.withdraw()


usr_id = simpledialog.askstring("Player Name", "Enter your name:")

if not usr_id:
    usr_id = "Unknown"

temp_root.destroy()

pygame.init()


W = 800
H = 600
win = pygame.display.set_mode((W, H))
pygame.display.set_caption("Dodge Game - Pandit ji Edition")


bg_col = (247, 197, 142)
floor_col = (217, 160, 104)
ink = (0, 0, 0)

# Fonts
sys_font = pygame.font.Font(None, 36)
big_font = pygame.font.Font(None, 72)

try:
    hero_pic = pygame.image.load("Pandit.jpg").convert_alpha()
    hero_pic = pygame.transform.scale(hero_pic, (50, 50))
    
    item_pic = pygame.image.load("Bell.jpg").convert_alpha()
    item_pic = pygame.transform.scale(item_pic, (40, 40))
except:
    
    print("Images not found, using placeholders")
    hero_pic = pygame.Surface((50,50))
    hero_pic.fill((0,0,255))
    item_pic = pygame.Surface((40,40))
    item_pic.fill((255,0,0))


my_box = hero_pic.get_rect()
my_box.centerx = W // 2
my_box.bottom = H - 10

step_size = 7


drops = []
drop_dy = 5
freq = 20 
points = 0

def spawn_new():
    r_x = random.randrange(0, W - 40)
    box = pygame.Rect(r_x, -40, 40, 40)
    drops.append(box)

def show_hero():
    win.blit(hero_pic, my_box)

def show_drops():
    for d in drops:
        win.blit(item_pic, (d.x, d.y))

def update_pos():
    global points, drop_dy
    
  
    if points > 50: drop_dy = 7
    if points > 100: drop_dy = 9
    if points > 150: drop_dy = 12

    for i in reversed(range(len(drops))):
        drops[i].y += drop_dy

        if drops[i].y > H:
            drops.pop(i)
            points += 1

def is_hit():
    for d in drops:
        if my_box.colliderect(d):
            return True
    return False

def ui_score():
    lbl = sys_font.render(f"Score: {points}", True, ink)
    win.blit(lbl, (10, 10))


win.fill(bg_col)
intro = big_font.render("LET'S BEGIN!", True, ink)
intro_box = intro.get_rect(center=(W // 2, H // 2))
win.blit(intro, intro_box)
pygame.display.flip()
pygame.time.delay(2000)

play = True
timer = pygame.time.Clock()
tick_count = 0
dead = False


while play:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            play = False

    if not dead:
        pressed = pygame.key.get_pressed()
    
        if pressed[pygame.K_LEFT] and my_box.left > 0:
            my_box.x -= step_size

        if pressed[pygame.K_RIGHT] and my_box.right < W:
            my_box.x += step_size

        tick_count += 1
        if tick_count % freq == 0:
            spawn_new()

        update_pos()
        
        if is_hit():
            dead = True
            
    win.fill(bg_col)
  
    pygame.draw.rect(win, floor_col, (0, H // 1.4, W, H))

    if not dead:
        show_hero()
        show_drops()
        ui_score()
    else:
        msg1 = big_font.render("OH SHIT!", True, ink)
        msg2 = sys_font.render(f"Final Score: {points}", True, ink)
        msg3 = sys_font.render(f"Player: {usr_id}", True, ink)

        win.blit(msg1, (W//2 - 120, H//2 - 60))
        win.blit(msg2, (W//2 - 100, H//2 + 10))
        win.blit(msg3, (W//2 - 100, H//2 + 50))

    pygame.display.flip()
    timer.tick(60)

pygame.quit()

with open("scores.txt", "a") as f:
    f.write(f"{usr_id} : {points}\n")

print("saved.")
