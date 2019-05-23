#astroids
#Jared M.

#imports

from superwires import games
import random, math


#Global info

games.init(screen_width = 1280, screen_height = 1000, fps = 60)





#Classes

class Asteroid(games.Sprite):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3
    images = {SMALL: games.load_image("images/astroid_Small.png"),
              MEDIUM: games.load_image("images/astroid_Medium.png"),
              LARGE: games.load_image("images/astroid_large.png"),}
    SPEED = 2

    def __init__(self, x, y, size):
        super(Asteroid, self).__init__(image = Asteroid.images[size],
                                      x = x,
                                      y = y,
                                      dx = random.choice([1,-1]) * Asteroid.SPEED *random.random()/size,
                                      dy=random.choice([1, -1]) * Asteroid.SPEED * random.random() / size)
        self.size = size

    def update(self):
        if self.left > games.screen.width:
            self.right = 0

        if self.right < 0:
            self.left = games.screen.width

        if self.bottom < 0:
            self.top = games.screen.height

        if self.top > games.screen.height:
            self.bottom = 0


class Ship(games.Sprite):
    image = games.load_image("images/ship.png")
    ROTATION_STEP = 3
    VELOCITY_STEP = .15
    sound = games.load_sound("Music/thruster.wav")

    def __init__(self):
        super(Ship,self).__init__(image = Ship.image,
                                  x=games.screen.width / 2,
                                  y=games.screen.height / 2)


    def update(self):
        if games.keyboard.is_pressed(games.K_LEFT) or games.keyboard.is_pressed(games.K_a):
            self.angle -= Ship.ROTATION_STEP

        if games.keyboard.is_pressed(games.K_RIGHT) or games.keyboard.is_pressed(games.K_d):
            self.angle += Ship.ROTATION_STEP

        if games.keyboard.is_pressed(games.K_w) or games.keyboard.is_pressed(games.K_UP):
            Ship.sound.play()
            angle = self.angle * math.pi/180
            self.dx += Ship.VELOCITY_STEP * math.sin(angle)
            self.dy += Ship.VELOCITY_STEP * -math.cos(angle)

        if self.left > games.screen.width:
            self.right = 0

        if self.right < 0:
            self.left = games.screen.width

        if self.bottom < 0:
            self.top = games.screen.height

        if self.top > games.screen.height:
            self.bottom = 0







#Main

def main():

    #load data
    bg_img = games.load_image("images/background.png", transparent=False)



    #Create objects
    for i in range(8):
        x = random.randrange(games.screen.width)
        y = random.randrange(games.screen.width)
        size = random.choice([Asteroid.SMALL, Asteroid.MEDIUM, Asteroid.LARGE])
        new_asteroid = Asteroid(x = x, y = y, size = size)
        games.screen.add(new_asteroid)

    #Create Ship
    the_ship = Ship()


    #draw objects
    games.screen.background = bg_img
    games.screen.add(the_ship)



    #games setup




    #start main loop
    games.screen.mainloop()




main()