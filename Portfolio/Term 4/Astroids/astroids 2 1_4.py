#astroids
#Jared M.

#imports

from superwires import games, color
import random, math


#Global info

games.init(screen_width = 1280, screen_height = 1000, fps = 60)





#Classes

class Game(object):
    def __init__(self):
        #set level
        self.level = 0
        #load sound for level advancement
        self.sound = games.load_sound("Music/level change.wav")
        #create score
        self.score = games.Text(value = 0,
                                size = 30,
                                color = color.white,
                                top = 5,
                                right = games.screen.width - 10,
                                )
        games.screen.add(self.score)

        self.ship = Ship(game = self,
                           x = games.screen.width/2,
                           y = games.screen.height/2)
        games.screen.add(self.ship)

    def play(self):
        games.music.load("Music/music.mp3")
        games.music.play(-1)

        bg_img = games.load_image("images/background.png", transparent=False)
        games.screen.background = bg_img

        self.advance()

        games.screen.mainloop()

    def advance(self):
        self.level += 1
        #amount of space around ship to preserve when creating asteroids
        BUFFER = 150

        #create objects
        for i in range(self.level):
            x_min = random.randrange(BUFFER)
            y_min = BUFFER - x_min

            #choose distance along the axises based on min distance
            x_distance = random.randrange(x_min, games.screen.width - x_min)
            y_distance = random.randrange(y_min, games.screen.height - y_min)

            #calculate location based on distance
            x = self.ship.x + x_distance
            y = self.ship.y + y_distance

            #wrap around screen if necessary
            x %= games.screen.width
            y %= games.screen.height

            #create asteroid
            new_asteroid = Asteroid(game = self, x=x, y=y, size=Asteroid.LARGE)
            games.screen.add(new_asteroid)

            #display level number
            level_message = games.Message(value = "Level" + str(self.level),
                                          size = 40,
                                          color = color.pink,
                                          x = games.screen.width/2,
                                          y = games.screen.height/10,
                                          lifetime = 3 * games.screen.fps,
                                          is_collideable = False)
            games.screen.add(level_message)

            #play new level sound (except at first level)
            if self.level > 1:
                self.sound.play()

    def end(self):
        """End the game."""
        end_message = games.Message(value = "Game Over",
                                    size = 90,
                                    color = color.red,
                                    x = games.screen.width/2,
                                    y = games.screen.height/2,
                                    lifetime = 5 * games.screen.fps,
                                    after_death = games.screen.quit,
                                    is_collideable = False)
        games.screen.add(end_message)





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


class Asteroid(Wrapper):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3
    images = {SMALL: games.load_image("images/astroid_Small.png"),
              MEDIUM: games.load_image("images/astroid_Medium.png"),
              LARGE: games.load_image("images/astroid_large.png")}
    SPEED = 2
    SPAWN = 3
    POINTS = 30
    total = 0

    def __init__(self, game, x, y, size):
        """ Initialize asteroid sprite. """
        Asteroid.total += 1

        super(Asteroid, self).__init__(
            image=Asteroid.images[size],
            x=x, y=y,
            dx=random.choice([1, -1]) * Asteroid.SPEED * random.random() / size,
            dy=random.choice([1, -1]) * Asteroid.SPEED * random.random() / size)

        self.game = game
        self.size = size

    def die(self):

        Asteroid.total -= 1

        self.game.score.value += int(Asteroid.POINTS / self.size)
        self.game.score.right = games.screen.width - 10

        # if asteroid isn't small, replace with two smaller asteroids
        if self.size == Asteroid.LARGE or self.size == Asteroid.MEDIUM:
            self.size-=1
            for i in range(Asteroid.SPAWN):
                new_asteroid = Asteroid(game=self.game,
                                        x=self.x,
                                        y=self.y,
                                        size=self.size)
                games.screen.add(new_asteroid)
        else:
            self.die

        # if all asteroids are gone, advance to next level
        if Asteroid.total == 0:
            self.game.advance()

        super(Asteroid, self).die()


class Ship(Collider):
    image = games.load_image("images/ship.png")
    sound = games.load_sound("Music/thruster.wav")

    ROTATION_STEP = 3
    VELOCITY_STEP = .13
    MISSILE_DELAY = 20
    MAX_VELOCITY = 3


    def __init__(self,game,x,y):
        super(Ship,self).__init__(image = Ship.image,x=x,y=y)
        self.game = game
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
            self.dx = min(max(self.dx, -Ship.MAX_VELOCITY), Ship.MAX_VELOCITY)
            self.dy = min(max(self.dy, -Ship.MAX_VELOCITY), Ship.MAX_VELOCITY)


        if self.missile_wait > 0:
            self.missile_wait -= 1

        if games.keyboard.is_pressed(games.K_SPACE) and self.missile_wait ==0:
            new_missile = Missile(self.x, self.y, self.angle)
            games.screen.add(new_missile)
            self.missile_wait = Ship.MISSILE_DELAY
            print("bang pop pow")

    def die(self):
        self.game.end()
        super(Ship, self).die()





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


        

def main():
    asteroids = Game()
    asteroids.play()


main()
