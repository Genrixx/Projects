#моя игра про кликер
import pygame as pg
width = 400
height = 400
score = 0
mouse_count_click = 1
pg.font.init() 
my_font = pg.font.SysFont('Comic Sans MS', 30)

run = True
white = (255, 255, 255)
window = pg.display.set_mode((width, height))
title = pg.display.set_caption('Clicker')



while run:
    
    text_surface = my_font.render(str(score), True, white)
    window.blit(text_surface, (190, 50))
    pg.display.update()
    


    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        if event.type == pg.MOUSEBUTTONDOWN :
            if event.button == 1:
                score += mouse_count_click
                window.fill(pg.Color("black"))
            

        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_q and score >= 100:
                mouse_count_click += 9
                score -= 100
                window.fill(pg.Color("black"))
            elif event.key == pg.K_w and score >= 5000:
                mouse_count_click += 100
                score -= 5000
                window.fill(pg.Color("black"))
            elif event.key == pg.K_e and score >= 50000:
                mouse_count_click += 1000
                score -= 50000
                window.fill(pg.Color("black"))
            elif event.key == pg.K_s and score >= 500000:
                mouse_count_click += 10000
                score -= 500000
                window.fill(pg.Color("black"))
            elif event.key == pg.K_a and score >= 5000000:
                mouse_count_click += 100000
                score -= 5000000
                window.fill(pg.Color("black"))
            elif event.key == pg.K_d and score >= 500000000:
                mouse_count_click += 10000000
                score -= 500000000
                window.fill(pg.Color("black"))
            


pg.quit()