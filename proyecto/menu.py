import pygame, sys, random
from boton import Boton
from juego import run_game

pygame.init()

screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Menú")

bg = pygame.image.load("proyecto/assets/Background.png")

def obtener_fuente(tamaño):
    return pygame.font.Font("proyecto/assets/font.ttf", tamaño)

def jugar():
    while True:
        mouse_pos = pygame.mouse.get_pos()
        run_game()

def menu_principal():
    while True:
        screen.blit(bg, (0, 0))

        mouse_pos = pygame.mouse.get_pos()

        texto_menu = obtener_fuente(100).render("PONG :D", True, "#ffffff")
        rect_menu = texto_menu.get_rect(center=(640, 100))

        boton_jugar = Boton(pos=(640, 400), texto="JUGAR", fuente=obtener_fuente(75), color_base="#d7fcd4", resaltado=(56, 84, 134))
        boton_cerrar = Boton(pos=(640, 550), texto="CERRAR", fuente=obtener_fuente(75), color_base="#d7fcd4", resaltado=(56, 84, 134))

        screen.blit(texto_menu, rect_menu)

        botones = [boton_jugar, boton_cerrar]
        espacio_entre_botones = 20

        for i, boton in enumerate(botones):
            boton_rect = boton.text.get_rect(center=(640, 250 + i * (boton.text.get_height() + espacio_entre_botones)))
            boton.rect.topleft = boton_rect.topleft
            boton.cambio_color(mouse_pos)
            boton.actualizar(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if boton_jugar.interaccion(mouse_pos):
                    jugar()
                if boton_cerrar.interaccion(mouse_pos):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

menu_principal()
