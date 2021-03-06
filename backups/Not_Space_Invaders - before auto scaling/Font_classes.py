class Label:
    def __init__(self, font, text, color, position, anchor="topleft"):
        self.text = text
        self.image = font.render(self.text, 1, color)
        self.rect = self.image.get_rect()
        setattr(self.rect, anchor, position)
        print(self.rect)

    def draw(self, surface):
        surface.blit(self.image, self.rect)