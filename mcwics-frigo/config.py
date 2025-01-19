import pygame
from helper import nextButton

WIDTH = 723
HEIGHT = 800

WHITE = (0, 0, 0)
screen = pygame.display.set_mode([WIDTH, HEIGHT])
fps = 60
timer = pygame.time.Clock()

next_button = nextButton("images/menu_buttons/next.png", (screen.get_width() - 140) // 2, 700)

## LEVEL 1

level1_items = {
    "banana": {"type": "veggies", "file": "images/fridge_items/banana.png", "position": (100, 100)},
    "orange": {"type": "veggies", "file": "images/fridge_items/orange.png", "position": (100, 200)},
    "cucumber": {"type": "veggies", "file": "images/fridge_items/cucumber.png", "position": (100, 300)},
    "lettuce": {"type": "veggies", "file": "images/fridge_items/lettuce.png", "position": (200, 100)},
    "bread": {"type": "wholeGrains", "file": "images/fridge_items/bread.png", "position": (200, 200)},
    "oats": {"type": "wholeGrains", "file": "images/fridge_items/oats2.png", "position": (200, 300)},
    "tofu": {"type": "protein", "file": "images/fridge_items/tofu.png", "position": (300, 100)},
    "ham": {"type": "protein", "file": "images/fridge_items/ham.png", "position": (300, 200)}
}

## LEVEL 2

level2_items = {
    "banana": {"type": "veggies", "file": "images/fridge_items/banana.png", "position": (100, 100)},
    "orange": {"type": "veggies", "file": "images/fridge_items/orange.png", "position": (100, 200)},
    "cucumber": {"type": "veggies", "file": "images/fridge_items/cucumber.png", "position": (100, 300)},
    "lettuce": {"type": "veggies", "file": "images/fridge_items/lettuce.png", "position": (200, 100)},
    "strawberry": {"type": "veggies", "file": "images/fridge_items/strawberry.png", "position": (200, 100)},
    "tomato": {"type": "veggies", "file": "images/fridge_items/tomato.png", "position": (200, 100)},
    "bread": {"type": "wholeGrains", "file": "images/fridge_items/bread.png", "position": (200, 200)},
    "oats": {"type": "wholeGrains", "file": "images/fridge_items/oats2.png", "position": (200, 300)},
    "brown rice": {"type": "wholeGrains", "file": "images/fridge_items/brownrice.png", "position": (200, 100)},
    "tofu": {"type": "protein", "file": "images/fridge_items/tofu.png", "position": (300, 100)},
    "ham": {"type": "protein", "file": "images/fridge_items/ham.png", "position": (300, 200)},
    "chicken": {"type": "protein", "file": "images/fridge_items/chicken.png", "position": (200, 100)},
}

## LEVEL 3

level3_items = {}

