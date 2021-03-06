# ๐ppang ๊ฒ์

import pygame  # ํ์ด์ฌ ๋ผ์ด๋ธ๋ฌ๋ฆฌ์ธ pygame์ ์ด์ฉ
import os  # ํ์ผ์์น๋ฅผ ๋ฐํํด์ฃผ๊ธฐ ์ํด ํ์

#############################################################################################

## ๊ธฐ๋ณธ ์ด๊ธฐํ (๋ฐ๋์ ํด์ผ ํ๋ ๊ฒ๋ค)

pygame.init()

# ๐นํ๋ฉด ํฌ๊ธฐ ์ค์ 
screen_width = 640    # ๊ฐ๋กํฌ๊ธฐ
screen_height = 480   # ์ธ๋กํฌ๊ธฐ
screen = pygame.display.set_mode((screen_width, screen_height))  # ์ง์ ํด์ค ํฌ๊ธฐ๋ก ํ๋ฉด ํฌ๊ธฐ์ค์ 

# ๐นํ๋ฉด ํ์ดํ ์ค์ 
pygame.display.set_caption("ppang game")

# FPS
clock = pygame.time.Clock()

#############################################################################################

## 1. ์ฌ์ฉ์ ๊ฒ์ ์ด๊ธฐํ (๋ฐฐ๊ฒฝํ๋ฉด, ๊ฒ์์ด๋ฏธ์ง, ์ขํ, ์๋, ํฐํธ ๋ฑ)

# ๐น์ด๋ฏธ์ง ๊ฒฝ๋ก ์ง์ 
current_path = os.path.dirname(__file__)  # ํ์ฌํ์ผ ์์น ๋ฐํ
image_path = os.path.join(current_path, "images")  # images ํด๋ ์์น ๋ฐํ

# ๐น๋ฐฐ๊ฒฝ ๋ง๋ค๊ธฐ
background = pygame.image.load(os.path.join(image_path, "background.png"))

# ๐น์คํ์ด์ง ๋ง๋ค๊ธฐ
stage = pygame.image.load(os.path.join(image_path, "stage.png"))
stage_size = stage.get_rect().size
stage_height = stage_size[1]  # ์คํ์ด์ง์ ๋์ด ์์ ์บ๋ฆญํฐ๋ฅผ ๋๊ธฐ ์ํจ

# ๐น์บ๋ฆญํฐ ๋ง๋ค๊ธฐ
character = pygame.image.load(os.path.join(image_path, "character.png"))
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width/2) - (character_width/2)
character_y_pos = screen_height - stage_height - character_height


running = True
while running:
    dt = clock.tick(30)
    
    ## 2. ์ด๋ฒคํธ ์ฒ๋ฆฌ (ํค๋ณด๋, ๋ง์ฐ์ค ๋ฑ)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    ## 3. ๊ฒ์ ์บ๋ฆญํฐ ์์น ์ ์


    ## 4. ์ถฉ๋ ์ฒ๋ฆฌ
    
    ## ๐น5. ํ๋ฉด์ ๊ทธ๋ฆฌ๊ธฐ
    screen.blit(background, (0,0))  # ๋ฐฐ๊ฒฝ ๊ทธ๋ฆฌ๊ธฐ
    screen.blit(stage, (0,screen_height-stage_height))  # ์คํ์ด์ง ๊ทธ๋ฆฌ๊ธฐ
    screen.blit(character, (character_x_pos,character_y_pos))  # ์บ๋ฆญํฐ ๊ทธ๋ฆฌ๊ธฐ
    
    # ๊ฒ์ํ๋ฉด ์๋ฐ์ดํธ
    pygame.display.update()

# game ์ข๋ฃ
pygame.quit()

#############################################################################################