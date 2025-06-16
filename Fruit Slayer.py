import pygame
import random
import sys

from pygame import MOUSEBUTTONDOWN

# Setup
pygame.init()
screen = pygame.display.set_mode((1000, 600))
pygame.display.set_caption("Fruit Slayer")
font = pygame.font.SysFont(None, 36)

run = True
score = 0
lives = 3

# # Load full and half apple
# apple = pygame.image.load("assets/apple.png")
# apple_half = pygame.image.load("assets/apple-half.png")
#
# # Resize
# apple = pygame.transform.scale(apple, (70, 80))
# apple_half = pygame.transform.scale(apple_half, (70, 80))

# # Apple position
# apple_x = 100
# apple_y = 100
# is_cut = False

fruit_names =["lemon","apple","avocado","pear","bomba"]
bg = pygame.image.load('../fruit ninja bbg.jpg')
bg = pygame.transform.scale(bg, (1000,600))

full_images = {}
half_images = {}

for name in fruit_names:
    full = pygame.image.load("assets/"+name + ".png")   # assets/lemon.png
    half= pygame.image.load("assets/" + name + "-half.png")  # assets/lemon-half.png

    full_images[name]= pygame.transform.scale(full,(80,80))
    half_images[name] = pygame.transform.scale(half, (80,80))


print(full_images)
print(half_images)


fruits = [] # empty
spawn_timer = 0 #zero


def add_fruit(fruit_list):
    name = random.choice(fruit_names)
    x = random.randint(50,700)
    y = 700
    v =-random.randint(20,28)
    g = 0.5

    fruit = {
        'name' : name,
        'x' : x,
        'y' : y,
         'v' : v,
        'g' : g,
        'cut': False,
        'timer' : 0

    }
    fruit_list.append(fruit)


def draw_fruit(fruit_list):
    for fruit in fruit_list:

        name =fruit['name'] # gets the name of the fruit

        x = fruit['x']
        y = fruit['y']

        if fruit['cut'] == True:
            img =half_images[name]
        else:
            img = full_images[name]


        if name == 'bomba':
            img = pygame.transform.scale(img, (90,100))

        screen.blit(img,(x,y))
def move_fruit(fruit_list):
    for fruit in fruit_list:
        fruit['v'] += fruit['g']
        fruit['y'] += fruit['v']

def check_click(fruit_list, pos, score, lives):
    fx, fy = pos

    for fruit in fruit_list:
        if not fruit['cut'] and fruit['name'] != 'bomba':
            if fruit ['x'] < fx < fruit['x'] + 70 and fruit['y'] < fy < fruit['y']+80:
                fruit['cut'] = True
                score += 1
                fruit['timer'] = 10
        if not fruit['cut'] and fruit['name'] == 'bomba':
            if fruit ['x'] < fx < fruit['x'] + 70 and fruit['y'] < fy < fruit['y']+80:
                fruit['cut'] = True
                fruit['timer'] = 10
                lives -= 1
    return score, lives

def gamescore(score):
    font = pygame.font.SysFont(None, 35)
    text = 'SCORE:' + str(score)
    t = font.render(text, True, 'white')
    screen.blit(t, (500, 60))

def gamelives(lives):
    font = pygame.font.SysFont(None, 35)
    text2 = 'LIVES:' + str(lives)
    tu = font.render(text2, True, 'white')
    screen.blit(tu, (650, 60))


    # print(fruit_list)

while run:
    pygame.time.delay(30)
    #screen.fill((30, 30, 30))
    screen.blit(bg, (0,0))

    spawn_timer +=1

    if spawn_timer > 30:
        add_fruit(fruits)
        spawn_timer = 0


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            score, lives = check_click(fruits, pygame.mouse.get_pos(), score, lives)
            if lives == 0:
                #run = False
                screen.fill("white")
                font = pygame.font.SysFont('comic sans ms', 75)
                text = font.render("Game over!", True, "Red")
                screen.blit(text, (300, 270))
                font2 = pygame.font.Font('../NotoSansJP-VariableFont_wght.ttf', 75)
                text2= font2.render("ゲームオーバー!", True, "Black")
                screen.blit(text2, (300, 350))
                pygame.display.update()
                pygame.time.wait(3000)
                pygame.quit()
                sys.exit()

    #
    # screen.blit(full_images['onion'], (100,100))
    # screen.blit(half_images['onion'], (200, 100))
    draw_fruit(fruits)
    gamescore(score)
    move_fruit(fruits)
    gamelives(lives)
    pygame.display.update()
    pygame.time.delay(25)