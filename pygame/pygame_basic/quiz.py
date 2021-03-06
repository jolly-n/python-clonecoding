# ðë¥í¼íê¸° ê²ì

import pygame  # íì´ì¬ ë¼ì´ë¸ë¬ë¦¬ì¸ pygameì ì´ì©
import random  # ë¥ì ìì¹ë¥¼ ëë¤ì¼ë¡ íê¸° ìí¨

#############################################################################################

## ê¸°ë³¸ ì´ê¸°í (ë°ëì í´ì¼ íë ê²ë¤)

pygame.init()

# íë©´ í¬ê¸° ì¤ì 
screen_width = 480    # ê°ë¡í¬ê¸°
screen_height = 640   # ì¸ë¡í¬ê¸°
screen = pygame.display.set_mode((screen_width, screen_height))  # ì§ì í´ì¤ í¬ê¸°ë¡ íë©´ í¬ê¸°ì¤ì 

# íë©´ íì´í ì¤ì 
pygame.display.set_caption("ë¥ í¼íê¸°")

# FPS
clock = pygame.time.Clock()

#############################################################################################

## 1. ì¬ì©ì ê²ì ì´ê¸°í (ë°°ê²½íë©´, ê²ìì´ë¯¸ì§, ì¢í, ìë, í°í¸ ë±)
# ë°°ê²½ ë§ë¤ê¸°
background = pygame.image.load('C:\\Users\\anneu\\Desktop\\study\\clonecoding\\ì¤ë½ì¤ê²ì\\pygame_basic\\background.png')

# ìºë¦­í°(dog) ë§ë¤ê¸°
dog = pygame.image.load('C:\\Users\\anneu\\Desktop\\study\\clonecoding\\ì¤ë½ì¤ê²ì\\pygame_basic\\dog.png')
dog_size = dog.get_rect().size
dog_width = dog.get_rect().size[0]
dog_height = dog.get_rect().size[1]
dog_x_pos = (screen_width/2) - (dog_width/2)
dog_y_pos = screen_height - dog_height

to_x = 0  # ìºë¦­í° ì´ë
dog_speed = 10  # ìºë¦­í° ì´ëìë

# ë¥ ë§ë¤ê¸°
ddong = pygame.image.load('C:\\Users\\anneu\\Desktop\\study\\clonecoding\\ì¤ë½ì¤ê²ì\\pygame_basic\\ddong.png')
ddong_size = ddong.get_rect().size
ddong_width = ddong.get_rect().size[0]
ddong_height = ddong.get_rect().size[1]
ddong_x_pos = random.randint(0, screen_width-ddong_width)  # ë¥ì ìì¹ë ëë¤/ randint(): ììê°ê³¼ ëê°ì ëª¨ë í¬í¨íë ê° ì¤ ëë¤ê°ì ì¶ë ¥
ddong_y_pos = 0

ddong_speed = 10  # ë¥ ì´ëìë


running = True
while running:
    dt = clock.tick(60)
    
    ## 2. ì´ë²¤í¸ ì²ë¦¬ (í¤ë³´ë, ë§ì°ì¤ ë±)
    for event in pygame.event.get():
        # ë§ì°ì¤
        if event.type == pygame.QUIT:
            running = False

        # í¤ë³´ë
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= dog_speed
            elif event.key == pygame.K_RIGHT:
                to_x += dog_speed

        if event.type == pygame.KEYUP:
            if event.type == pygame.K_LEFT or pygame.K_RIGHT:
                to_x = 0


    ## 3. ê²ì ìºë¦­í° ìì¹ ì ì
    dog_x_pos += to_x  # ë°©í¥í¤ì ë°ë¥¸ ìºë¦­í° ìì¹ ë³í
    ddong_y_pos += ddong_speed  # ë¥ì ìì¹ ë³í

    if dog_x_pos < 0:  # ìºë¦­í°ì ì´ëë²ì ì§ì  (íë©´ë°ì¼ë¡ ëê°ì§ ìëë¡)
        dog_x_pos = 0
    elif dog_x_pos > (screen_width - dog_width):
        dog_x_pos = (screen_width - dog_width)

    if ddong_y_pos > screen_height:  # ë¥ì ì´ëë²ì ì§ì 
        ddong_y_pos = 0
        ddong_x_pos = random.randint(0, screen_width-ddong_width)
    

    ## 4. ì¶©ë ì²ë¦¬
    dog_rect = dog.get_rect()  # ìºë¦­í° rectì ë³´ ê°ì ¸ì¤ê¸°
    dog_rect.left = dog_x_pos
    dog_rect.top = dog_y_pos

    ddong_rect = ddong.get_rect()  # ë¥ rectì ë³´ ê°ì ¸ìê¸°
    ddong_rect.left = ddong_x_pos
    ddong_rect.top = ddong_y_pos

    if dog_rect.colliderect(ddong_rect):  # ìºë¦­í°ì ë¥ê³¼ ì¶©ëíë©´ ê²ìì¢ë£
        print('ì¶©ëíì´ì')
        running = False


    ## 5. íë©´ì ê·¸ë¦¬ê¸°
    screen.blit(background, (0,0))
    screen.blit(dog, (dog_x_pos,dog_y_pos))

    screen.blit(ddong, (ddong_x_pos,ddong_y_pos))
    

    # ê²ìíë©´ ìë°ì´í¸
    pygame.display.update()


## ê²ì ì¢ë£
pygame.quit()

#############################################################################################
