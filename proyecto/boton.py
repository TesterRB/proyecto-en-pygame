class Boton():
    def __init__(self, pos, texto, fuente, color_base, resaltado):
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.fuente = fuente
        self.base_color, self.resaltado = color_base, resaltado
        self.text_input = texto
        self.text = self.fuente.render(self.text_input, True, self.base_color)
        self.rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

    def actualizar(self, screen):
        screen.blit(self.text, self.rect)

    def interaccion(self, position):
        return self.rect.collidepoint(position)

    def cambio_color(self, position):
        if self.rect.collidepoint(position):
            self.text = self.fuente.render(self.text_input, True, self.resaltado)
        else:
            self.text = self.fuente.render(self.text_input, True, self.base_color)