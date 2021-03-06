# ๐ppang ๊ฒ์

import pygame  # ํ์ด์ฌ ๋ผ์ด๋ธ๋ฌ๋ฆฌ์ธ pygame์ ์ด์ฉ
import os  # ํ์ผ์์น๋ฅผ ๋ฐํํด์ฃผ๊ธฐ ์ํด ํ์

#############################################################################################

## ๊ธฐ๋ณธ ์ด๊ธฐํ (๋ฐ๋์ ํด์ผ ํ๋ ๊ฒ๋ค)

pygame.init()

# ํ๋ฉด ํฌ๊ธฐ ์ค์ 
screen_width = 640    # ๊ฐ๋กํฌ๊ธฐ
screen_height = 480   # ์ธ๋กํฌ๊ธฐ
screen = pygame.display.set_mode((screen_width, screen_height))  # ์ง์ ํด์ค ํฌ๊ธฐ๋ก ํ๋ฉด ํฌ๊ธฐ์ค์ 

# ํ๋ฉด ํ์ดํ ์ค์ 
pygame.display.set_caption("ppang game")

# FPS
clock = pygame.time.Clock()

#############################################################################################

## 1. ์ฌ์ฉ์ ๊ฒ์ ์ด๊ธฐํ (๋ฐฐ๊ฒฝํ๋ฉด, ๊ฒ์์ด๋ฏธ์ง, ์ขํ, ์๋, ํฐํธ ๋ฑ)

# ์ด๋ฏธ์ง ๊ฒฝ๋ก ์ง์ 
current_path = os.path.dirname(__file__)  # ํ์ฌํ์ผ ์์น ๋ฐํ
image_path = os.path.join(current_path, "images")  # images ํด๋ ์์น ๋ฐํ

# ๋ฐฐ๊ฒฝ ๋ง๋ค๊ธฐ
background = pygame.image.load(os.path.join(image_path, "background.png"))

# ์คํ์ด์ง ๋ง๋ค๊ธฐ
stage = pygame.image.load(os.path.join(image_path, "stage.png"))
stage_size = stage.get_rect().size
stage_height = stage_size[1]  # ์คํ์ด์ง์ ๋์ด ์์ ์บ๋ฆญํฐ๋ฅผ ๋๊ธฐ ์ํจ

# ์บ๋ฆญํฐ ๋ง๋ค๊ธฐ
character = pygame.image.load(os.path.join(image_path, "character.png"))
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width/2) - (character_width/2)
character_y_pos = screen_height - stage_height - character_height

# ๐น์บ๋ฆญํฐ ์ด๋๋ฐฉํฅ
character_to_x = 0  # ์ข์ฐ ์ด๋

# ๐น์บ๋ฆญํฐ ์ด๋์๋
character_speed = 5

# ๐น๋ฌด๊ธฐ ๋ง๋ค๊ธฐ
weapon =  pygame.image.load(os.path.join(image_path, "weapon.png"))
weapon_size = weapon.get_rect().size
weapon_width = weapon_size[0]  # width๊ฐ๋ง ๊ฐ์ ธ์ค๋ ์ด์ ๋ ์บ๋ฆญํฐ๊ฐ ๋ฌด๊ธฐ๋ฅผ ์ ๋ ์์น๋ฅผ ์ก์์ฃผ๊ธฐ ์ํด์

# ๐น๋ฌด๊ธฐ ํ๋ฒ์ ์ฌ๋ฌ๋ฒ ๋ฐ์ฌ ๊ฐ๋ฅ
weapons = []

# ๐น๋ฌด๊ธฐ ์ด๋์๋
weapon_speed = 10


running = True
while running:
    dt = clock.tick(60)
    
    ## 2. ์ด๋ฒคํธ ์ฒ๋ฆฌ (ํค๋ณด๋, ๋ง์ฐ์ค ๋ฑ)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # ๐นํค๋ณด๋
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:  # ์ผ์ชฝํค ๋๋ฅด๋ฉด ์บ๋ฆญํฐ๊ฐ ์ผ์ชฝ์ผ๋ก ์ด๋
                character_to_x -= character_speed
            elif event.key == pygame.K_RIGHT:  # ์ค๋ฅธ์ชฝํค ๋๋ฅด๋ฉด ์บ๋ฆญํฐ๊ฐ ์ค๋ฅธ์ชฝ์ผ๋ก ์ด๋
                character_to_x += character_speed
            elif event.key == pygame.K_SPACE:  # ์คํ์ด์ค ๋๋ฅด๋ฉด ๋ฌด๊ธฐ๋ฐ์ฌ
                weapon_x_pos = character_x_pos + (character_width/2) - (weapon_width/2)  # ๋ฌด๊ธฐ์ ์์น๋ฅผ ์บ๋ฆญํฐ ์ค์์ ์์นํ๋๋ก ๊ณ์ฐํ์ฌ ์ง์ 
                weapon_y_pos = character_y_pos
                weapons.append([weapon_x_pos,weapon_y_pos])        

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:  # ์ข์ฐํค๋ฅผ ๋ผ๋ฉด ์บ๋ฆญํฐ ์ด๋ ์ํจ
                character_to_x = 0


    ## ๐น3. ๊ฒ์ ์บ๋ฆญํฐ ์์น ์ ์
    character_x_pos += character_to_x

    if character_x_pos < 0:  # ์์น๋ฒ์ ์ง์  (ํ๋ฉด์ ๋ฒ์ด๋์ง ์๋๋ก)
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width
    
    # ๐น๋ฌด๊ธฐ ์์น์กฐ์ 
    # ๋ฐ๋ณต๋ฌธ์ ๋๋ ค weapons์ ๋ด๊ธด ๋ฆฌ์คํธ๋ค์ w๋ก ํ๋์ฉ ๊ฐ์ ธ์ค๊ณ ,
    # w์ 0๋ฒ์งธ๊ฐ(์ฆ weapon_x_pos)๊ณผ 1๋ฒ์งธ๊ฐ(์ฆ weapon_y_pos)์ ๊ฐ์ ธ์ ์ฒ๋ฆฌ๋ฅผ ํ ๋ค ๋ค์ ๋ฆฌ์คํธ๋ก ๊ฐ์ธ weapons๋ผ๋ ๋ณ์์ ๋ฃ์ด์ค
    # ์ด๋ ๋ฌด๊ธฐ๋ ์๋ก ์ด์ง๋ฏ๋ก weapon_y_pos์์ weapon_speed๋งํผ ๋นผ์ฃผ๋ ์ฒ๋ฆฌ๊ฐ ํ์
    weapons = [ [w[0], w[1] - weapon_speed] for w in weapons]

    # ๐น์ฒ์ฅ์ ๋ฟ์ผ๋ฉด ๋ฌด๊ธฐ ์์ ๊ธฐ
    weapons = [ [w[0], w[1]] for w in weapons if w[1] > 0]


    ## 4. ์ถฉ๋ ์ฒ๋ฆฌ
    

    ## ๐น5. ํ๋ฉด์ ๊ทธ๋ฆฌ๊ธฐ (์ฝ๋ ์์๋๋ก ๊ทธ๋ ค์ง)
    screen.blit(background, (0,0))  # ๋ฐฐ๊ฒฝ ๊ทธ๋ฆฌ๊ธฐ

    for weapon_x_pos, weapon_y_pos in weapons:  # weapons๊ฐ ์ฌ๋ฌ๋ฒ ๋ค์ด๊ฐ๊ธฐ ๋๋ฌธ์ ๋ฐ๋ณต๋ฌธ ์ฌ์ฉ
        screen.blit(weapon, (weapon_x_pos,weapon_y_pos))

    screen.blit(stage, (0,screen_height-stage_height))  # ์คํ์ด์ง ๊ทธ๋ฆฌ๊ธฐ
    screen.blit(character, (character_x_pos,character_y_pos))  # ์บ๋ฆญํฐ ๊ทธ๋ฆฌ๊ธฐ
    
    # ๊ฒ์ํ๋ฉด ์๋ฐ์ดํธ
    pygame.display.update()

# pygame ์ข๋ฃ
pygame.quit()

#############################################################################################