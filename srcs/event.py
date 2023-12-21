import pygame
from pygame.locals import *

class EventHandler:
    def __init__(self):
        self.keydown = None
        self.keyup = None
        self.pressed = set()
        self.shouldquit = False

    def getEvents(self):
        self.keydown = None
        self.keyup = None
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                self.keydown = event.key
                self.pressed.add(event.key) 
            elif event.type == KEYUP:
                self.keyup = event.key
                self.pressed.discard(event.key)

            elif event.type == QUIT:
                self.shouldquit = True 
