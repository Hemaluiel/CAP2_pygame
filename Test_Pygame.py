import pygame
import sys
import random
import unittest
#import game  

# game code
class Apple(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((60, 40))  
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect(midbottom=(random.randint(0, 576), 0))

    def update(self):
        self.rect.y += 4
        if self.rect.y > 345:
            self.rect.y = 0
            self.rect.x = random.randint(0, 625)


class Basket(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((60, 40))  
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect(center=(550, 399))


class GameState:
    def __init__(self):
        self.state = "intro"


# Unit tests for game logic
class TestGame(unittest.TestCase):
    def test_apple_update(self):
        apple = Apple()
        initial_y = apple.rect.y
        apple.update()
        self.assertEqual(apple.rect.y, initial_y + 4)

    def test_basket_update(self):
        basket = Basket()
        initial_x = basket.rect.x
        basket.update()
        self.assertEqual(basket.rect.x, initial_x)

    def test_apple_reset_position(self):
        apple = Apple()
        apple.rect.y = 350
        apple.update()
        self.assertEqual(apple.rect.y, 0)

if __name__ == "__main__":
    unittest.main()

