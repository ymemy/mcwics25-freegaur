import pygame
from helper import nextButton

WIDTH = 723
HEIGHT = 800

WHITE = (0, 0, 0)
screen = pygame.display.set_mode([WIDTH, HEIGHT])
fps = 60
timer = pygame.time.Clock()

next_button = nextButton("images/img/NB.png", 640, 300)


## LEVEL 1

level1_items = {
    "banana": {"type": "veggies", "file": "images/fridge_items/banana.png", "position": (160, 270)},
    "orange": {"type": "veggies", "file": "images/fridge_items/orange.png", "position": (220, 275)},
    "cucumber": {"type": "veggies", "file": "images/fridge_items/cucumber.png", "position": (275, 270)},
    "lettuce": {"type": "veggies", "file": "images/fridge_items/lettuce.png", "position": (160, 370)},

    "bread": {"type": "wholeGrains", "file": "images/fridge_items/bread.png", "position": (220, 375)},
    "oats": {"type": "wholeGrains", "file": "images/fridge_items/oats2.png", "position": (275, 370)},

    "tofu": {"type": "protein", "file": "images/fridge_items/tofu.png", "position": (180, 460)},
    "ham": {"type": "protein", "file": "images/fridge_items/ham.png", "position": (250, 460)}
}

## LEVEL 2

level2_items = {
    "banana": {"type": "veggies", "file": "images/fridge_items/banana.png", "position": (160, 270)},
    "orange": {"type": "veggies", "file": "images/fridge_items/orange.png", "position": (220, 275)},
    "cucumber": {"type": "veggies", "file": "images/fridge_items/cucumber.png", "position": (275, 270)},
    "lettuce": {"type": "veggies", "file": "images/fridge_items/lettuce.png", "position": (160, 370)},
    "strawberry": {"type": "veggies", "file": "images/fridge_items/strawberry.png", "position": (220, 375)},
    "tomato": {"type": "veggies", "file": "images/fridge_items/tomato.png", "position": (275, 370)},

    "bread": {"type": "wholeGrains", "file": "images/fridge_items/bread.png", "position": (180, 460)},
    "oats": {"type": "wholeGrains", "file": "images/fridge_items/oats2.png", "position": (250, 460)},
    "brown rice": {"type": "wholeGrains", "file": "images/fridge_items/brownrice.png", "position": (420, 270)},

    "tofu": {"type": "protein", "file": "images/fridge_items/tofu.png", "position": (500, 270)},
    "ham": {"type": "protein", "file": "images/fridge_items/ham.png", "position": (420, 370)},
    "chicken": {"type": "protein", "file": "images/fridge_items/chicken.png", "position": (500, 370)},
}

## LEVEL 3

level3_items = {
    "banana": {"type": "veggies", "file": "images/fridge_items/banana.png", "position": (160, 270)},
    "orange": {"type": "veggies", "file": "images/fridge_items/orange.png", "position": (220, 275)},
    "cucumber": {"type": "veggies", "file": "images/fridge_items/cucumber.png", "position": (275, 270)},
    "lettuce": {"type": "veggies", "file": "images/fridge_items/lettuce.png", "position": (160, 370)},
    "strawberry": {"type": "veggies", "file": "images/fridge_items/strawberry.png", "position": (220, 375)},
    "tomato": {"type": "veggies", "file": "images/fridge_items/tomato.png", "position": (275, 370)},
    "carrot": {"type": "veggies", "file": "images/fridge_items/carrot.png", "position": (275, 465)},

    "bread": {"type": "wholeGrains", "file": "images/fridge_items/bread.png", "position": (160, 465)},
    "oats": {"type": "wholeGrains", "file": "images/fridge_items/oats2.png", "position": (220, 465)},
    "brown rice": {"type": "wholeGrains", "file": "images/fridge_items/brownrice.png", "position": (400, 270)},
    "quinoa": {"type": "wholeGrains", "file": "images/fridge_items/quinoa.png", "position": (460, 370)},

    "tofu": {"type": "protein", "file": "images/fridge_items/tofu.png", "position": (520, 270)},
    "ham": {"type": "protein", "file": "images/fridge_items/ham.png", "position": (400, 370)},
    "chicken": {"type": "protein", "file": "images/fridge_items/chicken.png", "position": (520, 370)},
    "salmon": {"type": "protein", "file": "images/fridge_items/salmon.png", "position": (460, 270)},
    "egg": {"type": "protein", "file": "images/fridge_items/egg.png", "position": (460, 460)}
}

