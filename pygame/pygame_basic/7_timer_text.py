# ðì¶ìµì ì¤ë½ì¤ ê²ì ë§ë¤ê¸°
import pygame  # íì´ì¬ ë¼ì´ë¸ë¬ë¦¬ì¸ pygameì ì´ì©

pygame.init()  # ì´ê¸°í (ë°ëì íì)


# íë©´ í¬ê¸° ì¤ì 
screen_width = 480    # ê°ë¡í¬ê¸°
screen_height = 640   # ì¸ë¡í¬ê¸°
screen = pygame.display.set_mode((screen_width, screen_height))   # íë©´ í¬ê¸°ì¤ì í ê²ì ë³ìë¡ ë°ìì´


# íë©´ íì´í ì¤ì 
pygame.display.set_caption("Nado Game")   # ê²ìì´ë¦ ì¤ì 


# FPS
clock = pygame.time.Clock()


# ë°°ê²½ ì´ë¯¸ì§ ë¶ë¬ì¤ê¸°
background = pygame.image.load("C:/Users/anneu/Desktop/study/clonecoding/ì¤ë½ì¤ê²ì/pygame_basic/background.png")


# ìºë¦­í°(ì¤íë¼ì´í¸) ë§ë¤ê¸°
character = pygame.image.load("C:/Users/anneu/Desktop/study/clonecoding/ì¤ë½ì¤ê²ì/pygame_basic/character.png")
# ìºë¦­í°ë¥¼ ìì§ì´ê¸° ìí ì½ëìì±
character_size = character.get_rect().size   # ìºë¦­í°ì´ë¯¸ì§ì í¬ê¸°ë¥¼ ê°ì ¸ì´
character_width = character_size[0]   # ìºë¦­í°ì ê°ë¡í¬ê¸°
character_height = character_size[1]   # ìºë¦­í°ì ì¸ë¡í¬ê¸°
character_x_pos = (screen_width/2) - (character_width/2) # ìºë¦­í°ì ê°ë¡ìì¹(x position)ê° íë©´ ê°ë¡í¬ê¸°ì ì ë°ì ìì¹íëë¡ ì§ì 
character_y_pos = screen_height - character_height   # ìºë¦­í°ì ì¸ë¡ìì¹(y position)ê° íë©´ ì¸ë¡í¬ê¸° ê°ì¥ ìëì ìì¹íëë¡ ì§ì 


# ìºë¦­í°ê° ì´ëí  ì¢í
to_x = 0
to_y = 0


# ìºë¦­í° ì´ë ìë
character_speed = 0.6


# ì (enemy) ìºë¦­í° ë§ë¤ê¸°
enemy = pygame.image.load("C:/Users/anneu/Desktop/study/clonecoding/ì¤ë½ì¤ê²ì/pygame_basic/enemy.png")
# ì ìºë¦­í°ë¥¼ ìì§ì´ê¸° ìí ì½ëìì±
enemy_size = enemy.get_rect().size   # ì ìºë¦­í°ì´ë¯¸ì§ì í¬ê¸°ë¥¼ ê°ì ¸ì´
enemy_width = enemy_size[0]   # ì ìºë¦­í°ì ê°ë¡í¬ê¸°
enemy_height = enemy_size[1]   # ì ìºë¦­í°ì ì¸ë¡í¬ê¸°
enemy_x_pos = (screen_width/2) - (enemy_width/2) # ì ìºë¦­í°ì ê°ë¡ìì¹(x position)ê° íë©´ ê°ë¡í¬ê¸°ì ì ë°ì ìì¹íëë¡ ì§ì 
enemy_y_pos = (screen_height/2) - (enemy_height/2)   # ì ìºë¦­í°ì ì¸ë¡ìì¹(y position)ê° íë©´ ì¸ë¡í¬ê¸°ì ì ë°ì ìì¹íëë¡ ì§ì 


# ð¹í°í¸ ì¤ì 
game_font = pygame.font.Font(None, 40)  # ê²ìí°í¸ ê°ì²´ ìì± (í°í¸,í¬ê¸°)/ âì¬ê¸°ì ê°ì²´ì ë³ìì ì°¨ì´ë ë¬´ì?


# ð¹ê²ì ì´ìê°
total_time = 10


# ð¹ê²ì ìììê°
start_ticks = pygame.time.get_ticks()   # íì¬ tick(ë»:ëë±ê±°ë¦¬ë¤)ì ê°ì ¸ì´


# ì´ë²¤í¸ ë£¨í
# íë¡ê·¸ë¨ì´ ì¢ë£ëì§ ìëë¡ ëìì ê³ì ê²ì¬íë ì´ë²¤í¸ë£¨íë¥¼ ë§ë¤ì´ì¤ì¼ íë¤
running = True   # ê²ìì´ ì§íì¤ì¸ê°ë¥¼ íì¸íë ë³ì (True:ê²ì ì§íì¤ì ìë¯¸)
while running:
    dt = clock.tick(60)   # ê²ìíë©´ì ì´ë¹ íë ì ìë¥¼ ì¤ì 
    # print("fps: "+ str(clock.get_fps()))   # íì¬ íë ìì ì¶ë ¥

    # ìºë¦­í°ê° 100ë§í¼ ì´ë í´ì¼í¨
    # 10fps : 1ì´ ëìì 10ë² ëì â¡ 1ë²ì 10ë§í¼ ì´ë (10*10=100)
    # 20fps : 1ì´ ëìì 20ë² ëì°© â¡ 1ë²ì 5ë§í¼ ì´ë (5*20=100)
    # íë ìë§ë¤ ì´ëíë ìëê° ë¬ë¼ì§ë©´ ìëê¸° ëë¬¸ì ì´ë¤ ì¡°ì¹ë¥¼ ì·¨í´ì¼ í¨

    for event in pygame.event.get():    # pygameì ì°ê¸° ìí´ìë ë°ëì íì/ ì´ë¤ ì´ë²¤í¸ê° ë°ìíë ê²½ì°
        if event.type == pygame.QUIT:   # ì¬ë¬ ì´ë²¤í¸ ì¤ ì°½ë«ê¸° ë²í¼ì ëë¥´ë ì´ë²¤í¸ê° ë°ìíë ê²½ì° â¡ ê²ì ì¢ë£
            running = False             # False:ê²ì ì§íì¤ ìëì ìë¯¸

        if event.type == pygame.KEYDOWN:      # í¤ê° ëë¦¬ë ì´ë²¤í¸ ë°ì (KEYDOWN:í¤ê° ëë¦°ìí)
            if event.key == pygame.K_LEFT:    # ì¼ìª½í¤ê° ëë¦¼ â¡ ìºë¦­í°ê° ì¼ìª½ì¼ë¡ ì´ë
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT: # ì¤ë¥¸ìª½í¤ê° ëë¦¼ â¡ ìºë¦­í°ê° ì¤ë¥¸ìª½ì¼ë¡ ì´ë
                to_x += character_speed
            elif event.key == pygame.K_UP:    # ìí¤ê° ëë¦¼ â¡ ìºë¦­í°ê° ìë¡ ì´ë
                to_y -= character_speed    # ì upì´ -ì§?
            elif event.key == pygame.K_DOWN:  # ìëí¤ê° ëë¦¼ â¡ ìºë¦­í°ê° ìëë¡ ì´ë
                to_y += character_speed

        if event.type == pygame.KEYUP:        # í¤ê° ë¼ì§ë ì´ë²¤í¸ ë°ì (KEYUP:í¤ê° ëë¦¬ì§ ìììí)
            if event.key == pygame.K_LEFT or event.key  == pygame.K_RIGHT:  # ì¼ìª½ì´ë ìëí¤ë¥¼ ë¼ë©´
                to_x = 0   # ìºë¦­í° ì¢ì°ì´ë ìì
            elif event.key == pygame.K_UP or event.key  == pygame.K_DOWN:   # ìë ìëí¤ë¥¼ ë¼ë©´
                to_y = 0   # ìºë¦­í° ìíì´ë ìì

    # ì¤ì  ìºë¦­í°ì ìì¹(position)
    # ë°©í¥í¤ë¥¼ ëë ìë ì¢íì´ë ê°ì to_x,yì ë´ìëê³ , íì¬ ìºë¦­í°ì ìì¹(position)ì ëí´ì¤ë¤
    character_x_pos += to_x * dt   # ì¢ì° í¤ë¥¼ ëë¥´ë©´ ìºë¦­í°ì ì¢ì° ìì¹ê° ì´ë / (* dt)ë¥¼ í´ì£¼ë ì´ì : íë ìë§ë¤ ìºë¦­í°ì ì´ëìëê° ë¬ë¼ì§ë ê²ì ë³´ì íê¸° ìí¨
    character_y_pos += to_y * dt   # ìí í¤ë¥¼ ëë¥´ë©´ ìºë¦­í°ì ìí ìì¹ê° ì´ë

    # ìºë¦­í°ì ì´ëë²ì ì§ì 
    # ìºë¦­í°ê° íë©´ë°ì¼ë¡ ëê°ì§ ëª»íê² íë ì½ë
    # ê°ë¡ ê²½ê³ê° ì²ë¦¬
    if character_x_pos < 0:                                  # ìºë¦­í°ê° ì¼ìª½ íë©´ë°ì¼ë¡ ëê°ë ê²½ì°
        character_x_pos = 0                                  # ìºë¦­í°ë ì¼ìª½ ëìì ë©ì¶¤
    elif character_x_pos > screen_width - character_width:   # ìºë¦­í°ê° ì¤ë¥¸ìª½ íë©´ë°ì¼ë¡ ëê°ë ê²½ì°
        character_x_pos = screen_width - character_width     # ìºë¦­í°ë ì¤ë¥¸ìª½ ëìì ë©ì¶¤
    # ì¸ë¡ ê²½ê³ê° ì²ë¦¬
    if character_y_pos < 0:                                  # ìºë¦­í°ê° ììª½ íë©´ë°ì¼ë¡ ëê°ë ê²½ì°
        character_y_pos = 0                                  # ìºë¦­í°ë ììª½ ëìì ë©ì¶¤
    elif character_y_pos > screen_height - character_height: # ìºë¦­í°ê° ìëìª½ íë©´ë°ì¼ë¡ ëê°ë ê²½ì°
        character_y_pos = screen_height - character_height   # ìºë¦­í°ë ìëìª½ ëìì ë©ì¶¤

    # ì¶©ë ì²ë¦¬ë¥¼ ìí rectì ë³´ ìë°ì´í¸
    character_rect = character.get_rect()   # rect = rectangle(ì¬ê°í)/ ì¤ì  ìºë¦­í°ì ì¬ê°í ì ë³´ë¥¼ ê°ì ¸ì´?
    character_rect.left = character_x_pos   # ìºë¦­í° ê¸°ì¤ ì¼ìª½  
    character_rect.top = character_y_pos    # ìºë¦­í° ê¸°ì¤ ììª½

    enemy_rect = enemy.get_rect() 
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    # ì¶©ë ì²´í¬
    # colliderect():ì¬ê°í ê¸°ì¤ì¼ë¡ ì¶©ëì´ ìëì§ íì¸íë í¨ì
    if character_rect.colliderect(enemy_rect):  # ìºë¦­í°ì ì¬ê°íê³¼ ì ì ì¬ê°íê³¼ ì¶©ëì´ ìë ê²½ì°
        print('ì¶©ëíì´ì')
        running = False  # ì¶©ëíë©´ ê²ì ì¢ë£

    # ë°°ê²½ ê·¸ë¦¬ê¸°
    screen.blit(background, (0,0))    # blit():ì¤ì ë¡ ê·¸ë ¤ì£¼ë í¨ì/ (ê·¸ë¦´ë³ì, ê·¸ë¦¬ë ìì¹ì¢í)

    # ìºë¦­í° ê·¸ë¦¬ê¸°
    screen.blit(character, (character_x_pos,character_y_pos))  # ë´ìºë¦­í° ê·¸ë¦¬ê¸°
    screen.blit(enemy, (enemy_x_pos,enemy_y_pos))              # ì ìºë¦­í° ê·¸ë¦¬ê¸°
    
    # ð¹íì´ë¨¸ ë§ë¤ê¸°
    # ê²½ê³¼ìê° ê³ì°
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000  # ê²½ê³¼ìê°(ms)ì 1000ì¼ë¡ ëë  ì´ë¨ì(s)ë¡ íì

    # render(): ì¤ì ë¡ ê¸ìë¥¼ ê·¸ë ¤ì£¼ë í¨ì
    # (ì¶ë ¥í  ê¸ì, True, ê¸ììì)
    timer = game_font.render(str(int(total_time-elapsed_time)), True, (255,255,255))
    screen.blit(timer, (10,10))   # íì´ë¨¸ ê·¸ë¦¬ê¸°

    # ð¹ìê°ì´ê³¼íë©´ ê²ìì¢ë£ëë ì½ë ìì±
    if total_time - elapsed_time <= 0:
        print('íììì')
        running = False
    # ì¢ë£ ì  ì ì ëê¸°
    pygame.time.delay(2000)  # 2ì´ ì ë ëê¸°(2000ms)
    

    # ê²ìíë©´ ìë°ì´í¸
    pygame.display.update()  # ê²ìíë©´ ë¤ì ê·¸ë¦¬ê¸° â¡ while ë°ë³µë¬¸ì ê³ì ëë©´ì íë©´ì ìë¡ ê·¸ë ¤ì¤ë¤


# pygame ì¢ë£
# running = Falseê° ëë©´ ê²ìì ì¢ë£íë¤
pygame.quit()