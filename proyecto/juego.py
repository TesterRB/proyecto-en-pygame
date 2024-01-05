import pygame, sys, random

puntaje_jugador = 0
puntaje_oponente = 0

def ball_animation(pelota, jugador, oponente, screen_width, screen_height, velocidad_x, velocidad_y):
    global puntaje_jugador, puntaje_oponente

    pelota.x += velocidad_x
    pelota.y += velocidad_y
    
    if pelota.top <= 0 or pelota.bottom >= screen_height:
        velocidad_y *= -1
    if pelota.left <= 0 or pelota.right >= screen_width:
        if pelota.left <= 0:
            puntaje_jugador += 1
        elif pelota.right >= screen_width:
            puntaje_oponente += 1
        reiniciar(pelota, velocidad_x, velocidad_y, screen_width, screen_height)
    
    if pelota.colliderect(jugador) or pelota.colliderect(oponente):
        velocidad_x *= -1

    return velocidad_x, velocidad_y

def reiniciar(pelota, velocidad_x, velocidad_y, screen_width, screen_height):
    pelota.center = (screen_width/2, screen_height/2)
    velocidad_y *= random.choice((1, -1))
    velocidad_x *= random.choice((1, -1))

    return velocidad_x, velocidad_y

def movimiento_jugador(jugador, velocidad_del_jugador, screen_height):
    jugador.y += velocidad_del_jugador
    if jugador.top <= 0:
        jugador.top = 0
    if jugador.bottom >= screen_height:
        jugador.bottom = screen_height

def animacion_oponente(oponente, pelota, velocidad_del_oponente, screen_height):
    if oponente.top < pelota.y:
        oponente.top += velocidad_del_oponente
    if oponente.bottom > pelota.y:
        oponente.top -= velocidad_del_oponente
    if oponente.top <= 0:
        oponente.top = 0
    if oponente.bottom >= screen_height:
        oponente.bottom = screen_height

def run_game():
    #Configuracion del juego
    global puntaje_jugador, puntaje_oponente
    pygame.init()
    clock = pygame.time.Clock()

    #Configuracion de pantalla
    screen_width = 1280
    screen_height = 720
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Pong")

    pelota = pygame.Rect(screen_width / 2 - 15, screen_height / 2 - 15, 30, 30)
    jugador = pygame.Rect(screen_width - 20, screen_height / 2 - 70, 10, 140)
    opponent = pygame.Rect(10, screen_height / 2 - 70, 10, 140)

    #Configuracion del fondo
    fondo = pygame.image.load("proyecto/assets/fondo.png")
    fondo = pygame.transform.scale(fondo, (screen_width, screen_height))
    color_general = (255, 255, 255)

    velocidadb_x = 7 * random.choice((1, -1))
    velocidadb_y = 7 * random.choice((1, -1))
    velocidad_jugador = 0
    velocidad_oponente = 8

    # Bucle de ejecución del juego
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    velocidad_jugador += 8
                if event.key == pygame.K_UP:
                    velocidad_jugador -= 8
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN:
                    velocidad_jugador -= 8
                if event.key == pygame.K_UP:
                    velocidad_jugador += 8

        velocidadb_x, velocidadb_y = ball_animation(pelota, jugador, opponent, screen_width, screen_height, velocidadb_x, velocidadb_y)
        movimiento_jugador(jugador, velocidad_jugador, screen_height)
        animacion_oponente(opponent, pelota, velocidad_oponente, screen_height)

        # Visuales
        screen.blit(fondo, (0,0))
        pygame.draw.rect(screen, color_general, jugador)
        pygame.draw.rect(screen, color_general, opponent)
        pygame.draw.ellipse(screen, color_general, pelota)
        pygame.draw.aaline(screen, color_general, (screen_width / 2, 0), (screen_width / 2, screen_height))
        # Mostrar los contadores de puntos
        fuente = pygame.font.Font("proyecto/assets/font.ttf", 20)
        texto_pj = fuente.render(f"Tú: {puntaje_jugador}", True, (255, 255, 255))
        texto_po = fuente.render(f"Oponente: {puntaje_oponente}", True, (255, 255, 255))
        screen.blit(texto_pj, (screen_width - 150, 20))
        screen.blit(texto_po, (20, 20))

        pygame.display.flip()
        clock.tick(60)

# Ejecutar el juego
if __name__ == "__main__":
    run_game()
