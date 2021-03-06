# ๐์ถ์ต์ ์ค๋ฝ์ค ๊ฒ์ ๋ง๋ค๊ธฐ
import pygame  # ํ์ด์ฌ ๋ผ์ด๋ธ๋ฌ๋ฆฌ์ธ pygame์ ์ด์ฉ

pygame.init()  # ์ด๊ธฐํ (๋ฐ๋์ ํ์)


# ํ๋ฉด ํฌ๊ธฐ ์ค์ 
screen_width = 480    # ๊ฐ๋กํฌ๊ธฐ
screen_height = 640   # ์ธ๋กํฌ๊ธฐ
screen = pygame.display.set_mode((screen_width, screen_height))   # ํ๋ฉด ํฌ๊ธฐ์ค์ ํ ๊ฒ์ ๋ณ์๋ก ๋ฐ์์ด


# ํ๋ฉด ํ์ดํ ์ค์ 
pygame.display.set_caption("Nado Game")   # ๊ฒ์์ด๋ฆ ์ค์ 


# ๋ฐฐ๊ฒฝ ์ด๋ฏธ์ง ๋ถ๋ฌ์ค๊ธฐ
background = pygame.image.load("C:/Users/anneu/Desktop/study/clonecoding/์ค๋ฝ์ค๊ฒ์/pygame_basic/background.png")


# ๐น์บ๋ฆญํฐ(์คํ๋ผ์ดํธ) ๋ถ๋ฌ์ค๊ธฐ
character = pygame.image.load("C:/Users/anneu/Desktop/study/clonecoding/์ค๋ฝ์ค๊ฒ์/pygame_basic/character.png")
# ์บ๋ฆญํฐ๋ฅผ ์์ง์ด๊ธฐ ์ํ ์ฝ๋
character_size = character.get_rect().size   # ์บ๋ฆญํฐ์ด๋ฏธ์ง์ ํฌ๊ธฐ๋ฅผ ๊ฐ์ ธ์ด
character_width = character_size[0]   # ์บ๋ฆญํฐ์ ๊ฐ๋กํฌ๊ธฐ
character_height = character_size[1]   # ์บ๋ฆญํฐ์ ์ธ๋กํฌ๊ธฐ
character_x_pos = (screen_width/2) - (character_width/2) # ์บ๋ฆญํฐ์ ๊ฐ๋ก์์น(x position)๊ฐ ํ๋ฉด ๊ฐ๋กํฌ๊ธฐ์ ์ ๋ฐ์ ์์นํ๋๋ก ์ง์ 
character_y_pos = screen_height - character_height   # ์บ๋ฆญํฐ์ ์ธ๋ก์์น(y position)๊ฐ ํ๋ฉด ์ธ๋กํฌ๊ธฐ ๊ฐ์ฅ ์๋์ ์์นํ๋๋ก ์ง์ 


# ์ด๋ฒคํธ ๋ฃจํ
# ํ๋ก๊ทธ๋จ์ด ์ข๋ฃ๋์ง ์๋๋ก ๋์์ ๊ณ์ ๊ฒ์ฌํ๋ ์ด๋ฒคํธ๋ฃจํ๋ฅผ ๋ง๋ค์ด์ค์ผ ํ๋ค
running = True   # ๊ฒ์์ด ์งํ์ค์ธ๊ฐ๋ฅผ ํ์ธํ๋ ๋ณ์ (True:๊ฒ์ ์งํ์ค์ ์๋ฏธ)
while running:   
    for event in pygame.event.get():    # pygame์ ์ฐ๊ธฐ ์ํด์๋ ๋ฐ๋์ ํ์/ ์ด๋ค ์ด๋ฒคํธ๊ฐ ๋ฐ์ํ๋ ๊ฒฝ์ฐ
        if event.type == pygame.QUIT:   # ์ฌ๋ฌ ์ด๋ฒคํธ ์ค ์ฐฝ๋ซ๊ธฐ ๋ฒํผ์ ๋๋ฅด๋ ์ด๋ฒคํธ๊ฐ ๋ฐ์ํ๋ ๊ฒฝ์ฐ โก ๊ฒ์ ์ข๋ฃ
            running = False             # False:๊ฒ์ ์งํ์ค ์๋์ ์๋ฏธ

    # ๋ฐฐ๊ฒฝ ๊ทธ๋ฆฌ๊ธฐ
    screen.blit(background, (0,0))  # blit():์ค์ ๋ก ๊ทธ๋ ค์ฃผ๋ ํจ์/ (๊ทธ๋ฆด๋ณ์, ๊ทธ๋ฆฌ๋ ์์น์ขํ)
    # screen.fill((200,191,231))    # ๋ฐฐ๊ฒฝ์ด๋ฏธ์ง๋ฅผ ์ฃผ๋ ๊ฒ์ด ์๋๋ผ RGB๊ฐ์ผ๋ก ์์ ์ง์ ํด์ฃผ๋ ๋ฐฉ๋ฒ

    # ๐น์บ๋ฆญํฐ ๊ทธ๋ฆฌ๊ธฐ
    screen.blit(character, (character_x_pos,character_y_pos))
    
    
    # ๊ฒ์ํ๋ฉด ์๋ฐ์ดํธ
    pygame.display.update()    # ๊ฒ์ํ๋ฉด ๋ค์ ๊ทธ๋ฆฌ๊ธฐ โก while ๋ฐ๋ณต๋ฌธ์ ๊ณ์ ๋๋ฉด์ ํ๋ฉด์ ์๋ก ๊ทธ๋ ค์ค๋ค


# pygame ์ข๋ฃ
# running = False๊ฐ ๋๋ฉด ๊ฒ์์ ์ข๋ฃํ๋ค
pygame.quit()