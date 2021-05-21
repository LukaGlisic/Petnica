import pygame as pg
import pygamebg

(sirina, visina) = (300, 300) # otvaramo prozor
prozor = pygamebg.open_window(sirina, visina, "Zdravo svete!")

prozor.fill(pg.Color("darkred"))
font = pg.font.SysFont("Verdana", 40)
poruka = "sup"
tekst = font.render(poruka, True, pg.Color("white"))
(sirina_teksta, visina_teksta) = (tekst.get_width(), tekst.get_height())
(x, y) = (20,30)
prozor.blit(tekst, (x, y))
pygamebg.wait_loop()
