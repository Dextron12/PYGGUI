import pygame, os

width,height = 1024, 748
window = pygame.display.set_mode((width,height), pygame.RESIZABLE)

file = "C:\\Users\\Ethan\\Programming\\Python\\Blunt-Wars\\"

fileList = os.listdir(file)

frame = pygame.Surface((width-40,height-20))
frame.set_alpha(200)

scroll = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.VIDEORESIZE:
            window = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
            width,height = event.w, event.h
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4:
                if scroll > 0:
                    scroll -= 64
            if event.button == 5:
                if scroll < height-172.5:
                    scroll += 64

    window.fill((0,255,0))
    frame.fill((49,79,79))

    # DRAW SCROLL BAR
    pygame.draw.rect(frame, (255,255,255), (width-80,40,30,height-80))
    pygame.draw.rect(frame, (49, 79, 79), (width-78, 42+scroll, 26, 64))

    # TOP BAR
    pygame.draw.rect(frame, (0,0,0), (0,0,width-40,30))
    pygame.draw.rect(frame, (255,0,0), (width-70,0,30,30)) # EXIT BUTTON
    pygame.draw.line(frame, (0,0,0), (width-70,0), (width-40,30), 2)
    pygame.draw.line(frame, (0,0,0), (width-40,0), (width-70,30), 2)

    # FORM
    pygame.draw.rect(frame, (0,0,0), (10, 40, width-100, 20))

    for file in range(9):
        pygame.draw.rect(frame, (0,0,255), (10+(96*file), 80+(scroll*64), 64, 64))

    window.blit(frame, (20,10))
    pygame.display.flip()


