import pygame
from helper import nextButton

WIDTH = 723
HEIGHT = 800

WHITE = (0, 0, 0)
screen = pygame.display.set_mode([WIDTH, HEIGHT])
fps = 60
timer = pygame.time.Clock()

next_button = nextButton("images/menu_buttons/next.png", 610, 250)
next_button.image = pygame.transform.scale(next_button.image, (100, 100))  # Scale to 100x100
next_button.rect = next_button.image.get_rect(topleft=(1000, 500))


## LEVEL 1

level1_items = {
    "banana": {"type": "veggies", "file": "images/fridge_items/banana.png", "position": (160, 270)},
    "orange": {"type": "veggies", "file": "images/fridge_items/orange.png", "position": (220, 275)},
    "cucumber": {"type": "veggies", "file": "images/fridge_items/cucumber.png", "position": (275, 275)},
    "lettuce": {"type": "veggies", "file": "images/fridge_items/lettuce.png", "position": (160, 375)},

    "bread": {"type": "wholeGrains", "file": "images/fridge_items/bread.png", "position": (220, 375)},
    "oats": {"type": "wholeGrains", "file": "images/fridge_items/oats.png", "position": (275, 380)},

    "tofu": {"type": "protein", "file": "images/fridge_items/tofu.png", "position": (180, 460)},
    "ham": {"type": "protein", "file": "images/fridge_items/ham.png", "position": (250, 465)}
}

## LEVEL 2

level2_items = {
    "banana": {"type": "veggies", "file": "images/fridge_items/banana.png", "position": (160, 270)},
    "orange": {"type": "veggies", "file": "images/fridge_items/orange.png", "position": (220, 275)},
    "cucumber": {"type": "veggies", "file": "images/fridge_items/cucumber.png", "position": (275, 275)},
    "lettuce": {"type": "veggies", "file": "images/fridge_items/lettuce.png", "position": (160, 375)},
    "strawberry": {"type": "veggies", "file": "images/fridge_items/strawberry.png", "position": (220, 375)},
    "tomato": {"type": "veggies", "file": "images/fridge_items/tomato.png", "position": (275, 380)},

    "bread": {"type": "wholeGrains", "file": "images/fridge_items/bread.png", "position": (180, 460)},
    "oats": {"type": "wholeGrains", "file": "images/fridge_items/oats.png", "position": (250, 465)},
    "brown rice": {"type": "wholeGrains", "file": "images/fridge_items/brownrice.png", "position": (420, 295)},

    "tofu": {"type": "protein", "file": "images/fridge_items/tofu.png", "position": (500, 295)},
    "ham": {"type": "protein", "file": "images/fridge_items/ham.png", "position": (420, 375)},
    "chicken": {"type": "protein", "file": "images/fridge_items/chicken.png", "position": (500, 375)},
}

## LEVEL 3

level3_items = {
    "banana": {"type": "veggies", "file": "images/fridge_items/banana.png", "position": (160, 270)},
    "orange": {"type": "veggies", "file": "images/fridge_items/orange.png", "position": (220, 275)},
    "cucumber": {"type": "veggies", "file": "images/fridge_items/cucumber.png", "position": (275, 275)},
    "lettuce": {"type": "veggies", "file": "images/fridge_items/lettuce.png", "position": (160, 375)},
    "strawberry": {"type": "veggies", "file": "images/fridge_items/strawberry.png", "position": (220, 375)},
    "tomato": {"type": "veggies", "file": "images/fridge_items/tomato.png", "position": (275, 380)},
    "carrot": {"type": "veggies", "file": "images/fridge_items/carrot.png", "position": (275, 460)},

    "bread": {"type": "wholeGrains", "file": "images/fridge_items/bread.png", "position": (160, 460)},
    "oats": {"type": "wholeGrains", "file": "images/fridge_items/oats.png", "position": (220, 465)},
    "brown rice": {"type": "wholeGrains", "file": "images/fridge_items/brownrice.png", "position": (400, 295)},
    "quinoa": {"type": "wholeGrains", "file": "images/fridge_items/quinoa.png", "position": (460, 375)},

    "tofu": {"type": "protein", "file": "images/fridge_items/tofu.png", "position": (520, 295)},
    "ham": {"type": "protein", "file": "images/fridge_items/ham.png", "position": (400, 375)},
    "chicken": {"type": "protein", "file": "images/fridge_items/chicken.png", "position": (520, 375)},
    "salmon": {"type": "protein", "file": "images/fridge_items/salmon.png", "position": (460, 295)},
    "egg": {"type": "protein", "file": "images/fridge_items/egg.png", "position": (460, 460)}
}

