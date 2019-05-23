#Read Key inputs
#Demonstrates reading the keyboard

from superwires import games


games.init(screen_width = 900, screen_height = 720, fps = 50)


class Ship(games.Sprite):
    ship_image = games.load_image("images/ship.png")


    ROTATION_STEP = 6
    VELOCITY_STEP = .03

    def __init__(self):
        super(Ship,self).__init__(image = Ship.ship_image,
                                  x=games.screen.width / 2,
                                  y=games.screen.height / 2)

    def update(self):

        if games.keyboard.is_pressed(games.K_a) or games.keyboard.is_pressed(games.K_LEFT):
            self.angle-=8
        if games.keyboard.is_pressed(games.K_d) or games.keyboard.is_pressed(games.K_RIGHT):
            self.angle+=8
        if games.keyboard.is_pressed(games.K_w) or games.keyboard.is_pressed(games.K_UP):
            Ship.sound.play()
            angle = self.angle * math.pi/180
            self.dx += Ship.VELOCITY_STEP * math.sin(angle)
            self.dy += Ship.VELOCITY_STEP * -math.cos(angle)


def main():

    # load data
    space_image = games.load_image("images/background.png", transparent = False)
    explosion_files =["animations/explosion1.png",
                      "animations/explosion2.png",
                      "animations/explosion3.png",
                      "animations/explosion4.png",
                      "animations/explosion5.png",
                      "animations/explosion6.png",
                      "animations/explosion7.png",
                      "animations/explosion8.png",]
    ##missle_sound = games.load_sound("")
    games.music.load("Music/03 Chibi Ninja.mp3")


    # create objects
    the_ship = Ship()
    explosion = games.Animation(images = explosion_files,
                                x = games.screen.width/2,
                                y = games.screen.height/2,
                                n_repeats = 0,
                                repeat_interval = 4)


    # draw
    games.screen.background = space_image
    games.screen.add(the_ship)
    games.screen.add(explosion)


    # games setup
    games.music.play("Music/03 Chibi Ninja.mp3")


    # start loop
    games.screen.mainloop()

main()