import pygame, sys, random
score, lives=0,10
class Apple(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("apple.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (60,40))
        self.rect = self.image.get_rect(midbottom = (random.randint(0,576), 0))
        self.mask = pygame.mask.from_surface(self.image)
    def update(self):
        global score
        self.rect.y+=4
        if self.rect.y>345:
            self.rect.y=0 
            self.rect.x=random.randint(0,625)
            global lives 
            lives -= 1
class Basket(pygame.sprite.Sprite):
    def __init__(self) :
        super().__init__()
        self.image = pygame.image.load("wicker-basket.png").convert_alpha()
        self.rect = self.image.get_rect(center=(550,399))
        self.mask = pygame.mask.from_surface(self.image)
        self.image = pygame.transform.scale(self.image, (60,40))
    def update(self):
        if pygame.key.get_pressed()[pygame.K_LEFT]:
            self.rect.x-=10
        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            self.rect.x+=10
        if pygame.key.get_pressed()[pygame.K_a]:
            self.rect.x-=10
        if pygame.key.get_pressed()[pygame.K_d]:
            self.rect.x+=10
        if self.rect.x>=575:
            self.rect.x=575
        if self.rect.x<=-5:
            self.rect.x=-5
class GameState():
    def __init__(self):
        self.state="intro"
    def intro(self):
        global score
        global lives
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
                score = 0
                lives = 10
        if pygame.key.get_pressed()[pygame.K_SPACE]:
            self.state="main_game"
        screen.blit(ready_text, (0,0))
        pygame.display.update()
    def main_game(self):
        global score
        global lives
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
                score=0
                lives=10
        screen.fill("White")
        screen.blit(ground, (0, 300))
        apple_grp.draw(screen)
        apple_grp.update()
        basket.draw(screen)
        basket.update()
        score_txt = text_font.render(f"Score: {score}", 1, "#16213E")
        lives_txt = text_font.render(f"Lives: {lives}", 1, "#16213E")
        screen.blit(score_txt, (5, 10))
        screen.blit(lives_txt, (630//2+150, 10))
        if lives==0:
            self.state="over"
        pygame.display.update()
    def over(self):
        global score
        global lives
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
        if pygame.key.get_pressed()[pygame.K_SPACE]:
            global score
            global lives
            score = 0
            lives = 10
            self.state="main_game"
        screen.fill("White")
        screen.blit(over_text, (0,0))
        score2_txt = text_font.render(f"Score: {score}", 1, "#16213E")
        screen.blit(score2_txt, (630//2+50,360//2+10))
        pygame.display.update()
    def state_manager(self):
        global lives
        if self.state=="intro":
            self.intro()
        if self.state=="main_game":
            self.main_game()
        if self.state=="over":
            if lives==0:
                self.over()
pygame.init()
pygame.mixer.init()
screen_width = 630
screen_height = 360
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Apple catcher")
text_font = pygame.font.SysFont("monospace", 25)
ready_text = pygame.image.load("Apple Catcher.png").convert_alpha()
ground = pygame.image.load("ground.png").convert_alpha()
over_text = pygame.image.load("over_screen.png").convert_alpha()
basket = pygame.sprite.GroupSingle(Basket())
apple_grp = pygame.sprite.Group()
def create_apple(num):
    for i in range(1,num+1):
        apple=Apple()
        apple_grp.add(apple)
create_apple(2)
clock = pygame.time.Clock()
game_state = GameState()
while True:
    game_state.state_manager()
    if pygame.sprite.spritecollide(basket.sprite, apple_grp, True, pygame.sprite.collide_mask):
            score+=1
            new_apple = Apple()
            apple_grp.add(new_apple)
            sound = pygame.mixer.Sound("water drop.mp3")
            sound.play()
    clock.tick(60)