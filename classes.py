class Human:
    """
    Human class which acts as each individual agent. Currently implementing the MVP of the class, which only considers basic movement and screen input.
    Later on have plans on incorporating more advanced behaviour.

    Basic Stage: 
        4 inputs: distance from top edge of display
                  distance from bottom edge of display
                  distance from left side of display
                  distance from right side of display
        5 outputs: move left
                   move right
                   move up
                   move down
                   no movement
    
    """
    # initialise class constants
    VEL = 5

    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.vel = self.VEL
        self.image = img

    def move_left(self):
        self.x -= 
    def move_right(self):
        self.x += 
    def move_up(self):
        self.y -=
    def move_down(self):
        self.y += 
    def draw(self, win):
        win.blit(self.image, (self.x, self.y))