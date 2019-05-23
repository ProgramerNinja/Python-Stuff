#astroids
#Jared M.

#imports

from superwires import games
import random, math


#Global info

games.init(screen_width = 1280, screen_height = 1000, fps = 60)





#Classes

class Wrapper(games.Sprite):
    def update(self):
        if self.left > games.screen.width:
            self.right = 0

        if self.right < 0:
            self.left = games.screen.width

        if self.bottom < 0:
            self.top = games.screen.height

        if self.top > games.screen.height:
            self.bottom = 0

    def die(self):
        self.destroy()

class Collider(Wrapper):
    def update(self):
        """checking for overlapping sprites"""
        super(Collider, self).update()

        if self.overlapping_sprites:
            for sprite in self.overlapping_sprites:
                sprite.die()
            self.die()

    def die(self):
        #create explosion
        new_explosion = Explosion(obj_x = self.x, obj_y = self.y)

        #add explosion to screen
        games.screen.add(new_explosion)

        self.destroy()

class Explosion(games.Animation):
    sound = games.load_sound("Music/explosion.wav")
    expimages = ["animations/explosion1.png",
                       "animations/explosion2.png",
                       "animations/explosion3.png",
                       "animations/explosion4.png",
                       "animations/explosion5.png",
                       "animations/explosion6.png",
                       "animations/explosion7.png",
                       "animations/explosion8.png", ]
    def __init__(self, obj_x, obj_y):
        super(Explosion, self).__init__(images = Explosion.expimages,
                                      x=obj_x, y=obj_y,
                                      repeat_interval = 4,
                                      is_collideable = False,
                                      n_repeats = 1)
        Explosion.sound.play()


class Asteroid(Collider):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3
    images = {SMALL: games.load_image("images/astroid_Small.png"),
              MEDIUM: games.load_image("images/astroid_Medium.png"),
              LARGE: games.load_image("images/astroid_large.png"),}
    SPEED = 2
    SPAWN = 2


    def __init__(self, x, y, size):
        super(Asteroid, self).__init__(image = Asteroid.images[size],
                                      x = x,
                                      y = y,
                                      dx = random.choice([1, -1]) * Asteroid.SPEED * random.random() / size,
                                      dy = random.choice([1, -1]) * Asteroid.SPEED * random.random() / size)
        self.size = size

    def die(self):
        super(Asteroid, self).die()
        if self.size != Asteroid.SMALL:
            for i in range(Asteroid.SPAWN):
                new_asteroid = Asteroid(x = self.x,
                                        y = self.y,
                                        size = self.size -1)
                games.screen.add(new_asteroid)
        self.destroy()


class Ship(Collider):
    image = games.load_image("images/ship.png")
    sound = games.load_sound("Music/thruster.wav")

    ROTATION_STEP = 3
    VELOCITY_STEP = .13
    MISSILE_DELAY = 20


    def __init__(self):
        super(Ship,self).__init__(image = Ship.image,
                                  x=games.screen.width / 2,
                                  y=games.screen.height / 2)
        self.missile_wait = 0


    def update(self):
        super(Ship, self).update()
        if games.keyboard.is_pressed(games.K_LEFT) or games.keyboard.is_pressed(games.K_a):
            self.angle -= Ship.ROTATION_STEP

        if games.keyboard.is_pressed(games.K_RIGHT) or games.keyboard.is_pressed(games.K_d):
            self.angle += Ship.ROTATION_STEP

        if games.keyboard.is_pressed(games.K_w) or games.keyboard.is_pressed(games.K_UP):
            Ship.sound.play()
            angle = self.angle * math.pi/180
            self.dx += Ship.VELOCITY_STEP * math.sin(angle)
            self.dy += Ship.VELOCITY_STEP * -math.cos(angle)

        if self.missile_wait > 0:
            self.missile_wait -= 1

        if games.keyboard.is_pressed(games.K_SPACE) and self.missile_wait ==0:
            new_missile = Missile(self.x, self.y, self.angle)
            games.screen.add(new_missile)
            self.missile_wait = Ship.MISSILE_DELAY
            print("bang pop pow")



class Missile(Collider):
    image = games.load_image("images/missile.png", transparent = True)
    sound = games.load_sound("Music/missile.wav")
    BUFFER = 60
    VELOCITY_FACTOR = 9
    LIFETIME = 80

    def __init__(self, ship_x, ship_y, ship_angle):
        Missile.sound.play()
        angle = ship_angle * math.pi / 180


        # calculate missle's starting position

        buffer_x = Missile.BUFFER * math.sin(angle)
        buffer_y = Missile.BUFFER * -math.cos(angle)

        x = ship_x + buffer_x
        y = ship_y + buffer_y

        dx = Missile.VELOCITY_FACTOR * math.sin(angle)
        dy = Missile.VELOCITY_FACTOR * -math.cos(angle)
        super(Missile, self).__init__(image = Missile.image,
                                      x=x,
                                      y=y,
                                      dx=dx,
                                      dy=dy)
        self.lifetime = Missile.LIFETIME

    def update(self):
        super(Missile, self).update()
        self.lifetime -= 1
        if self.lifetime == 0:
            self.destroy()


        


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
    #games.music.play("Music/03 Chibi Ninja.mp4")




    #start main loop
    games.screen.mainloop()




main()