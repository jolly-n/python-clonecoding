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

# ์บ๋ฆญํฐ ์ด๋๋ฐฉํฅ
character_to_x = 0  # ์ข์ฐ ์ด๋

# ์บ๋ฆญํฐ ์ด๋์๋
character_speed = 5

# ๋ฌด๊ธฐ ๋ง๋ค๊ธฐ
weapon =  pygame.image.load(os.path.join(image_path, "weapon.png"))
weapon_size = weapon.get_rect().size
weapon_width = weapon_size[0]  # width๊ฐ๋ง ๊ฐ์ ธ์ค๋ ์ด์ ๋ ์บ๋ฆญํฐ๊ฐ ๋ฌด๊ธฐ๋ฅผ ์ ๋ ์์น๋ฅผ ์ก์์ฃผ๊ธฐ ์ํด์

# ๋ฌด๊ธฐ ์ ๋ณด 
weapons = []  # ํ๋ฒ์ ์ฌ๋ฌ๋ฒ ๋ฐ์ฌ ๊ฐ๋ฅํ๊ธฐ ๋๋ฌธ์ ๋ฆฌ์คํธ๋ก ๊ด๋ฆฌ

# ๋ฌด๊ธฐ ์ด๋์๋
weapon_speed = 10

# ๊ณต ๋ง๋ค๊ธฐ (4๊ฐ ํฌ๊ธฐ์ ๋ํด ๋ฐ๋ก ์ฒ๋ฆฌ)
ball_images = [
    pygame.image.load(os.path.join(image_path, "balloon1.png")),
    pygame.image.load(os.path.join(image_path, "balloon2.png")),
    pygame.image.load(os.path.join(image_path, "balloon3.png")),
    pygame.image.load(os.path.join(image_path, "balloon4.png"))
]

# ๊ณต ํฌ๊ธฐ์ ๋ฐ๋ฅธ ์ต์ด ์๋
ball_speed_y = [-18, -15, -12, -9]  # index 0,1,2,3์ ํด๋นํ๋ ์๋๊ฐ

# ๊ณต ์ ๋ณด
balls = []

# ์ฒ์ ๋ง๋ค์ด์ง๋ ํฐ ๊ณต ์ถ๊ฐ
balls.append({
    "pos_x" : 50,  # ๊ณต์ x์ขํ 
    "pos_y" : 50,  # ๊ณต์ y์ขํ
    "img_idx" : 0,  # ball_image ์ธ๋ฑ์ค
    "to_x": 3,  # ๊ณต์ x์ถ ์ด๋๋ฐฉํฅ (-3์ด๋ฉด ์ผ์ชฝ์ผ๋ก, 3์ด๋ฉด ์ค๋ฅธ์ชฝ์ผ๋ก ์ด๋)
    "to_y": -6, # ๊ณต์ y์ถ ์ด๋๋ฐฉํฅ
    "init_spd_y" : ball_speed_y[0]  # y์ถ์ผ๋ก์ ๊ณต์ ์ต์ด์๋
})

# ์ฌ๋ผ์ง ๊ณต, ๋ฌด๊ธฐ ์ ๋ณด ์ ์ฅ๋ณ์
weapon_to_remove = -1  # โ์ฌ๊ธฐ์ ์ -1๋ก ์ค์ ์ ํด๋์ง?/ ์ ๊ณต ์ข๋ฅ๋ 4๊ฐ๊ณ  ๊ทธ ๊ณต์ ํด๋นํ๋ ์ธ๋ฑ์ค ๊ฐ์ 0,1,2,3 ๋ฐ์ ์์
ball_to_remove = -1

# ๊ฒ์ํฐํธ ์ ์
game_font = pygame.font.Font(None, 40)

# ๊ฒ์์๊ฐ ์ ์
total_time = 100
start_tics = pygame.time.get_ticks()  # ์์ ์๊ฐ ์ ์

# ๊ฒ์ ์ข๋ฃ ๋ฉ์ธ์ง 
# Mission Complete(์ฑ๊ณต), Game Over(์ดํจ - ์บ๋ฆญํฐ ๊ณต์ ๋ง์), Time Over(์คํจ - ์๊ฐ์ด๊ณผ)
game_result = "Game Over"


running = True
while running:
    dt = clock.tick(30)
    
    ## 2. ์ด๋ฒคํธ ์ฒ๋ฆฌ (ํค๋ณด๋, ๋ง์ฐ์ค ๋ฑ)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # ํค๋ณด๋
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


    ## 3. ๊ฒ์ ์บ๋ฆญํฐ ์์น ์ ์
    character_x_pos += character_to_x

    if character_x_pos < 0:  # ๊ฒฝ๊ณ์ฒ๋ฆฌ(ํ๋ฉด์ ๋ฒ์ด๋์ง ์๋๋ก)
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width
    
    # ๋ฌด๊ธฐ ์์น ์ ์
    # ๋ฐ๋ณต๋ฌธ์ ๋๋ ค weapons์ ๋ด๊ธด ๋ฆฌ์คํธ๋ค์ w๋ก ํ๋์ฉ ๊ฐ์ ธ์ค๊ณ ,
    # w์ 0๋ฒ์งธ๊ฐ(์ฆ weapon_x_pos)๊ณผ 1๋ฒ์งธ๊ฐ(์ฆ weapon_y_pos)์ ๊ฐ์ ธ์ ์ฒ๋ฆฌ๋ฅผ ํ ๋ค ๋ค์ ๋ฆฌ์คํธ๋ก ๊ฐ์ธ weapons๋ผ๋ ๋ณ์์ ๋ฃ์ด์ค
    # ์ด๋ ๋ฌด๊ธฐ๋ ์๋ก ์ด์ง๋ฏ๋ก weapon_y_pos์์ weapon_speed๋งํผ ๋นผ์ฃผ๋ ์ฒ๋ฆฌ๊ฐ ํ์
    weapons = [ [w[0], w[1] - weapon_speed] for w in weapons]

    # ์ฒ์ฅ์ ๋ฟ์ผ๋ฉด ๋ฌด๊ธฐ ์์ ๊ธฐ
    weapons = [ [w[0], w[1]] for w in weapons if w[1] > 0]

    # ๊ณต ์์น ์ ์
    # enumerate(): balls ๋ฆฌ์คํธ์ ์๋ ๊ฐ์ ํ๋์ฉ ๊ฐ์ ธ์ค๋ฉด์,
    # ๋ช๋ฒ์งธ ์ธ๋ฑ์ค์ธ์ง(ball_idx) ๊ทธ ์ธ๋ฑ์ค์ ํด๋นํ๋ ๊ฐ(ball_val)์ ์ถ๋ ฅํ๋ค
    for ball_idx, ball_val in enumerate(balls):
        ball_x_pos = ball_val["pos_x"]
        ball_y_pos = ball_val["pos_y"]
        ball_img_idx = ball_val["img_idx"]

        ball_size = ball_images[ball_img_idx].get_rect().size
        ball_width = ball_size[0]
        ball_height = ball_size[1]

        # ๊ฐ๋ก ์์น
        # ๊ณต์ด ๊ฐ๋ก๋ฒฝ์ ๋ฟ์์ ๋ ๊ฐ๋ก ์ด๋๋ฐฉํฅ ๋ณ๊ฒฝ (ํ๊ฒจ ๋์ค๋ ํจ๊ณผ)
        if ball_x_pos < 0 or ball_x_pos > screen_width - ball_width:  
            ball_val["to_x"] = ball_val["to_x"] * -1  # -1์ ๊ณฑํด์ค ์ด๋๋ฐฉํฅ์ ๋ฐ๋๋ก ๋ฐ๊ฟ์ค 
        
        # ์ธ๋ก ์์น
        # ๊ณต์ด ์คํ์ด์ง์ ๋ฟ์์ ๋ ํ๊ฒจ ์ฌ๋ผ๊ฐ๋ ์ฒ๋ฆฌ
        if ball_y_pos >= screen_height - stage_height - ball_height:  # ๊ณต์ด ์ฒ์ ์คํ์ด์ง์ ๋ฟ์ ํ๊ฒจ์ ธ ์ฌ๋ผ๊ฐ ๊ฒฝ์ฐ ์ต์ด์๋ ์ ์
            ball_val["to_y"] = ball_val["init_spd_y"]  
        else:  # ๊ทธ ์ธ์ ๋ชจ๋  ๊ฒฝ์ฐ ๊ณต์ ์๋๋ฅผ ์ฆ๊ฐ
            ball_val["to_y"] += 0.5 

        ball_val["pos_x"] += ball_val["to_x"]
        ball_val["pos_y"] += ball_val["to_y"]


    ## 4. ์ถฉ๋ ์ฒ๋ฆฌ
    # ์บ๋ฆญํฐ rect ์ ๋ณด ๊ฐ์ ธ์ค๊ธฐ
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos
    
    # ๐น๊ณต๊ณผ ์บ๋ฆญํฐ ์ถฉ๋ ์ฒ๋ฆฌ
    for ball_idx, ball_val in enumerate(balls):
        ball_x_pos = ball_val["pos_x"]
        ball_y_pos = ball_val["pos_y"]
        ball_img_idx = ball_val["img_idx"]

        # ๊ณต rect ์ ๋ณด ๊ฐ์ ธ์ค๊ธฐ
        ball_rect = ball_images[ball_img_idx].get_rect()
        ball_rect.left = ball_x_pos
        ball_rect.top = ball_y_pos

        # ๊ณต๊ณผ ์บ๋ฆญํฐ ์ถฉ๋ ์ฒดํฌ
        if character_rect.colliderect(ball_rect):
            running = False  # ์ถฉ๋์ ๊ฒ์์ข๋ฃ
            break  # ๊ฒ์์ด ์ข๋ฃ๋๋ฉด์ for๋ฌธ ํ์ถ

        # ๊ณต๊ณผ ๋ฌด๊ธฐ ์ถฉ๋ ์ฒ๋ฆฌ
        for weapon_idx, weapon_val in enumerate(weapons):
            weapon_x_pos = weapon_val[0]
            weapon_y_pos = weapon_val[1]

            # ๋ฌด๊ธฐ rect ์ ๋ณด ๊ฐ์ ธ์ค๊ธฐ
            weapon_rect = weapon.get_rect()
            weapon_rect.left = weapon_x_pos
            weapon_rect.top = weapon_y_pos

            # ๊ณต๊ณผ ๋ฌด๊ธฐ ์ถฉ๋ ์ฒดํฌ
            if weapon_rect.colliderect(ball_rect):
                weapon_to_remove = weapon_idx  # ํด๋น๋ฌด๊ธฐ๋ฅผ ์์ ๊ธฐ ์ํ ๊ฐ ์ค์ / โ์ฌ๊ธฐ์ ์ ์ธ๋ฑ์ค ๊ฐ์ ๋ฃ์ด์ฃผ๋?
                ball_to_remove = ball_idx  # ํด๋น๊ณต์ ์์ ๊ธฐ ์ํ ๊ฐ ์ค์ / โball_img_idx๋ฅผ ๊ฐ์ ธ์์ผํ๋๊ฑฐ ์๋๊ฐ?
                
                # ๊ฐ์ฅ ์์ ๊ณต์ด ์๋๋ผ๋ฉด ์ถฉ๋ ์ ๋ค์ ๋จ๊ณ์ ๊ณต์ผ๋ก ๋๋ ์ฃผ๊ธฐ
                if ball_img_idx < 3:
                    # ํ์ฌ์ ๊ณตํฌ๊ธฐ ์ ๋ณด ๊ฐ์ ธ์ด
                    ball_width = ball_rect.size[0]
                    ball_height = ball_rect.size[1]

                    # ๋๋ ์ง ๊ณต ์ ๋ณด
                    small_ball_rect = ball_images[ball_img_idx +1].get_rect()  # ํ์ฌ๊ณตํฌ๊ธฐ๋ณด๋ค ํ๋จ๊ณ ๋ ์์์ง ๊ณตํฌ๊ธฐ์ rect์ ๋ณด๋ฅผ ๊ฐ์ ธ์ด
                    small_ball_width = small_ball_rect.size[0]
                    small_ball_height = small_ball_rect.size[1]

                    # ์ผ์ชฝ์ผ๋ก ํ๊ฒจ๋๊ฐ๋ ์์ ๊ณต
                    balls.append({
                        "pos_x" : ball_x_pos + (ball_width/2) - (small_ball_width/2),
                        "pos_y" : ball_y_pos + (ball_height/2) - (small_ball_height/2), 
                        "img_idx" : ball_img_idx +1,
                        "to_x": -3,  # ๊ณต์ x์ถ ์ด๋๋ฐฉํฅ (-3์ด๋ฉด ์ผ์ชฝ์ผ๋ก, 3์ด๋ฉด ์ค๋ฅธ์ชฝ์ผ๋ก ์ด๋)
                        "to_y": -6, # ๊ณต์ y์ถ ์ด๋๋ฐฉํฅ
                        "init_spd_y" : ball_speed_y[ball_img_idx +1]  # y์ถ์ผ๋ก์ ๊ณต์ ์ต์ด์๋
                    })

                    # ์ค๋ฅธ์ชฝ์ผ๋ก ํ๊ฒจ๋๊ฐ๋ ์์ ๊ณต
                    balls.append({
                        "pos_x" : ball_x_pos + (ball_width/2) - (small_ball_width/2),
                        "pos_y" : ball_y_pos + (ball_height/2) - (small_ball_height/2), 
                        "img_idx" : ball_img_idx +1,
                        "to_x": 3,  # ๊ณต์ x์ถ ์ด๋๋ฐฉํฅ (-3์ด๋ฉด ์ผ์ชฝ์ผ๋ก, 3์ด๋ฉด ์ค๋ฅธ์ชฝ์ผ๋ก ์ด๋)
                        "to_y": -6, # ๊ณต์ y์ถ ์ด๋๋ฐฉํฅ
                        "init_spd_y" : ball_speed_y[ball_img_idx +1]  # y์ถ์ผ๋ก์ ๊ณต์ ์ต์ด์๋
                    })  
                break  # ์์ชฝ for๋ฌธ ํ์ถ

        else:  #๐น ์์ชฝ for๋ฌธ ์กฐ๊ฑด์ด ๋ง์ง ์์ผ๋ฉด
            continue  # ๊ฒ์ ๊ณ์์งํ (๋ฐ๊นฅ์ชฝ for๋ฌธ ๊ณ์ ์ํ)
        break  # ์์ชฝ for๋ฌธ์์ break๋ฅผ ๋ง๋๋ฉด ์ฌ๊ธฐ๋ก ์ง์ํด ๋ฐ๊นฅ์ชฝ for๋ฌธ๋ ํ์ถ

    # for ๋ฐ๊นฅ์กฐ๊ฑด:
    #     ๋ฐ๊นฅ๋์
    #     for ์์ชฝ์กฐ๊ฑด:
    #         ์์ชฝ๋์
    #         if ์ถฉ๋ํ๋ฉด:
    #             break
    #     else:
    #         continue
    #     break

    # ์ถฉ๋๋ ๊ณต or ๋ฌด๊ธฐ ์์ ๊ธฐ
    if ball_to_remove > -1:  # ball_to_remove ๊ฐ์ 0,1,2,3 ์ค ํ๋ (๊ณต ์ข๋ฅ 4๊ฐ)
        del balls[ball_to_remove]  # ํด๋น ์ธ๋ฑ์ค์ ๊ณต์ ์์ค๋ค
        ball_to_remove = -1

    if weapon_to_remove > -1:  # weapon_to_remove ๊ฐ์ 0 ํ๋ (๋ฌด๊ธฐ ์ข๋ฅ 1๊ฐ)
        del weapons[weapon_to_remove]  # ๋ฌด๊ธฐ๋ฅผ ์์ค๋ค
        weapon_to_remove = -1

    # ๋ชจ๋  ๊ณต์ ์์ค ๊ฒฝ์ฐ ๊ฒ์ ์ข๋ฃ (์ฑ๊ณต)
    if len(balls) == 0:
        game_result = "Mission Complete"
        running = False


    ## 5. ํ๋ฉด์ ๊ทธ๋ฆฌ๊ธฐ (์ฝ๋ ์์๋๋ก ๊ทธ๋ ค์ง)
    screen.blit(background, (0,0))  # ๋ฐฐ๊ฒฝ ๊ทธ๋ฆฌ๊ธฐ

    for weapon_x_pos, weapon_y_pos in weapons:  # weapons๊ฐ ์ฌ๋ฌ๋ฒ ๋ค์ด๊ฐ๊ธฐ ๋๋ฌธ์ ๋ฐ๋ณต๋ฌธ ์ฌ์ฉ
        screen.blit(weapon, (weapon_x_pos,weapon_y_pos))

    for idx, val in enumerate(balls):
        ball_x_pos = val["pos_x"]
        ball_y_pos = val["pos_y"]
        ball_img_idx = val["img_idx"]
        screen.blit(ball_images[ball_img_idx], (ball_x_pos,ball_y_pos))  # ๊ณต ๊ทธ๋ฆฌ๊ธฐ

    screen.blit(stage, (0,screen_height-stage_height))  # ์คํ์ด์ง ๊ทธ๋ฆฌ๊ธฐ
    screen.blit(character, (character_x_pos,character_y_pos))  # ์บ๋ฆญํฐ ๊ทธ๋ฆฌ๊ธฐ

    # ํ์ด๋จธ ๋ง๋ค๊ธฐ
    elapsed_time = (pygame.time.get_ticks() - start_tics) / 1000  # ๊ฒฝ๊ณผ์๊ฐ ๊ณ์ฐ (ms -> s)
    timer = game_font.render("Time : {}".format(int(total_time-elapsed_time)), True, (255,255,255))
    screen.blit(timer, (10,10))  # ํ์ด๋จธ ๊ทธ๋ฆฌ๊ธฐ

    # ์๊ฐ์ด๊ณผํ๋ฉด ๊ฒ์์ข๋ฃ๋๋ ์ฝ๋ ์์ฑ
    if total_time - elapsed_time <= 0:
        game_result = "Time Over"
        running = False

    # ๊ฒ์ํ๋ฉด ์๋ฐ์ดํธ
    pygame.display.update()

# ๊ฒ์ ์ค๋ฒ ๋ฉ์ธ์ง ์ถ๋ ฅ
msg = game_font.render(game_result, True, (255,0,0))  # ๋นจ๊ฐ์
msg_rect = msg.get_rect(center = (int(screen_width/2), int(screen_height/2)))

screen.blit(msg, msg_rect)

pygame.display.update()  # ๋ฉ์ธ์ง๊ฐ ๋์ค๋ ค๋ฉด ํ๋ฉด ์๋ฐ์ดํธ ํ์
pygame.time.delay(2000)  # ๊ฒ์์ข๋ฃ ์  2์ด ๋๊ธฐ

# pygame ์ข๋ฃ
pygame.quit()

#############################################################################################