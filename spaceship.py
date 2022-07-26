import pygame as pg
import random
screen_w = 950
screen_h = 532
white = (255, 255, 255)
black = (0, 0, 0)
class Meteorite(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load("meteorite.png").convert_alpha()
        self.rect = self.image.get_rect()
    
    def update(self):
        self.rect.y += 1
        if self.rect.y > screen_h:
            self.rect.y = -10
            self.rect.x = random.randrange(screen_w)
            
class Player(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load("player.png").convert_alpha()
        self.rect = self.image.get_rect()
    def update(self):
        self.rect.x, self.rect.y = pg.mouse.get_pos()
        
class Game(object):
    def __init__(self):
        self.score = 0
        self.run = True
        self.game_over = False
        self.meteorite_list = pg.sprite.Group()
        self.all_sprite_list = pg.sprite.Group()
        self.background = pg.image.load("background.jpg").convert()
        for i in range(50):
            meteorite = Meteorite()
            meteorite.rect.x = random.randrange(screen_w)
            meteorite.rect.y = random.randrange(screen_h)
            self.meteorite_list.add(meteorite)
            self.all_sprite_list.add(meteorite)
        self.player = Player()
        self.all_sprite_list.add(self.player)
    
    def process_events(self):
        
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                pg.display.quit()
                self.run = False
            if event.type == pg.MOUSEBUTTONDOWN:
                if self.game_over:
                    self.__init__()
    
    def run_logic(self):
        if no self.game_over:
            
            self.all_sprite_list.update()
            meteorite_hit_list = pg.sprite.spritecollide(self.player, self.meteorite_list, True)
            for meteorite in meteorite_hit_list:
                self.score += 1
                print(self.score)
            if len(self.metorite_list) == 0:
                self.game_over = True
            
    def display_frame(self, screen):
        
        if self.game_over:
            font = pygame.font.SysFont('serif', 25)
            text = font.render("Game over, Click to continue", True, black)
        screen.blit(self.background, [0, 0])
        self.all_sprite_list.draw(screen)
        pg.display.flip()
        
        
def main():
    pg.init()
    screen = pg.display.set_mode([screen_w, screen_h])
    clock = pg.time.Clock()
    game = Game()
    while game.run:
        game.run_logic()
        game.display_frame(screen)
        clock.tick(60)
        game.process_events()

if __name__ == "__main__":
    main()