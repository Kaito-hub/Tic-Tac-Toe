import pygame
pygame.init()

window = pygame.display.set_mode((600,600))

pygame.display.set_caption("Tic Tac Toe")
white = (255,255,255)
Circle = pygame.image.load('Cross.png')
Cross = pygame.image.load('Circle.png')
clicks = []

load1 = False
load2 = False
load3 = False
load4 = False
load5 = False
load6 = False
load7 = False
load8 = False
load9 = False
load10 = False
load11 = False
load12 = False
load13 = False
load14 = False
load15 = False
load16 = False
load17 = False
load18 = False

def Background():
    window.fill(white)
    pygame.draw.rect(window, (0,0,0),( 198,0,4,600))
    pygame.draw.rect(window, (0,0,0),( 398,0,4,600))
    pygame.draw.rect(window, (0,0,0),( 0,198,600,4))
    pygame.draw.rect(window, (0,0,0),( 0,398,600,4))

pygame.display.flip()
run = True

while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    mouse = pygame.mouse.get_pressed()[0]
    mouse_x,mouse_y = pygame.mouse.get_pos()
    if len(clicks)%2 != 0:
        if mouse:
            if mouse_x > 0 and mouse_x < 198 and mouse_y > 0 and mouse_y < 198:
                clicks.append(mouse)
                load1 = True
                
            elif mouse_x > 0 and mouse_x < 198 and mouse_y > 202 and mouse_y < 398:
                clicks.append(mouse)
                load2 = True

            elif mouse_x > 0 and mouse_x < 198 and mouse_y > 402 and mouse_y < 600:
                clicks.append(mouse)
                load3 = True

            elif mouse_x > 202 and mouse_x < 398 and mouse_y > 0 and mouse_y < 198:
                clicks.append(mouse)
                load4 = True

            elif mouse_x > 202 and mouse_x < 398 and mouse_y > 202 and mouse_y < 398:
                clicks.append(mouse)
                load5 = True

            elif mouse_x > 202 and mouse_x < 398 and mouse_y > 402 and mouse_y < 600:
                clicks.append(mouse)
                load6 = True

            elif mouse_x > 402 and mouse_x < 600 and mouse_y > 0 and mouse_y < 198:
                clicks.append(mouse)
                load7 = True

            elif mouse_x > 402 and mouse_x < 600 and mouse_y > 202 and mouse_y < 398:
                clicks.append(mouse)
                load8 = True

            elif mouse_x > 402 and mouse_x < 600 and mouse_y > 402 and mouse_y < 600:
                clicks.append(mouse)
                load9 = True

    elif len(clicks)%2 == 0:
        if mouse:
            if mouse_x > 0 and mouse_x < 198 and mouse_y > 0 and mouse_y < 198:
                clicks.append(mouse)
                load10 = True
                
            elif mouse_x > 0 and mouse_x < 198 and mouse_y > 202 and mouse_y < 398:
                clicks.append(mouse)
                load11 = True
                
            elif mouse_x > 0 and mouse_x < 198 and mouse_y > 402 and mouse_y < 600:
                clicks.append(mouse)
                load12 = True

            elif mouse_x > 202 and mouse_x < 398 and mouse_y > 0 and mouse_y < 198:
                clicks.append(mouse)
                load13 = True

            elif mouse_x > 202 and mouse_x < 398 and mouse_y > 202 and mouse_y < 398:
                clicks.append(mouse)
                load14 = True

            elif mouse_x > 202 and mouse_x < 398 and mouse_y > 402 and mouse_y < 600:
                clicks.append(mouse)
                load15 = True

            elif mouse_x > 402 and mouse_x < 600 and mouse_y > 0 and mouse_y < 198:
                clicks.append(mouse)
                load16 = True

            elif mouse_x > 402 and mouse_x < 600 and mouse_y > 202 and mouse_y < 398:
                clicks.append(mouse)
                load17 = True

            elif mouse_x > 402 and mouse_x < 600 and mouse_y > 402 and mouse_y < 600:
                clicks.append(mouse)
                load18 = True
    if load1:
        window.blit(Circle, (0,0))

    if load2:
        window.blit(Circle, (0,201))

    if load3:
        window.blit(Circle, (0,401))

    if load4:
        window.blit(Circle, (201,0))

    if load5:
        window.blit(Circle, (201,201))

    if load6:
        window.blit(Circle, (201,401))
    
    if load7:
        window.blit(Circle, (401,0))
    
    if load8:
        window.blit(Circle, (401,201))
    
    if load9:
        window.blit(Circle, (401,401))
    
    if load10:
        window.blit(Cross, (0,0))
        
    if load11:
        window.blit(Cross, (0,201))

    if load12:
        window.blit(Cross, (0,401))

    if load13:
        window.blit(Cross, (201,0))

    if load14:
        window.blit(Cross, (201,201))

    if load15:
        window.blit(Cross, (201,401))

    if load16:
        window.blit(Cross, (401,0))
        
    if load17:
        window.blit(Cross, (401,201))

    if load18:
        window.blit(Cross, (401,401))

    if ((load1 and load2 and load3) or (load2 and load5 and load8) or (load3 and load6 and load9) or (load1 and load4 and load7) or (load4 and load5 and load6) or
            (load7 and load8 and load9) or (load1 and load5 and load9) or (load3 and load5 and load7)):
        print("Circle Wins")

    elif ((load10 and load11 and load12) or (load13 and load14 and load15) or (load16 and load17 and load18) or (load10 and load13 and load16) or
            (load11 and load14 and load17) or(load12 and load15 and load18) or (load10 and load14 and load18) or (load13 and load14 and load16)):
        print("Cross Wins")

    
    
    pygame.display.update()

    Background()



pygame.quit()
