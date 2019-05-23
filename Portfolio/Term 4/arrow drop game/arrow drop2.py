from superwires import games, color
import random
SCORE = 0

games.init(screen_width=580, screen_height=480, fps=50)


class Target(games.Sprite):
    """
    A target controlled by player to catch falling pizzas.
    """
    image = games.load_image("images/target.jfif")

    def __init__(self):
        """ Initialize Pan object and create Text object for score. """
        super(Target, self).__init__(image=Target.image,
                                  x=games.mouse.x,
                                  bottom=games.screen.height)

        self.score = games.Text(value=0, size=25, color=color.black,
                                top=5, right=games.screen.width - 10)
        games.screen.add(self.score)


    def update(self):
        """ Move to mouse x position. """
        self.x = games.mouse.x

        if self.left < 0:
            self.left = 0

        if self.right > games.screen.width:
            self.right = games.screen.width

        self.check_catch()

    def check_catch(self):
        """ Check if catch pizzas. """
        for arrow in self.overlapping_sprites:
            self.score.value += 10
            self.score.right = games.screen.width - 10
            arrow.handle_caught()


class Arrow(games.Sprite):
    """
    A pizza which falls to the ground.
    """
    image = games.load_image("images\Arrow.jfif")
    speed = 2

    def __init__(self, x, y=90):
        """ Initialize a Pizza object. """
        super(Arrow, self).__init__(image=Arrow.image,
                                    x=x, y=y,
                                    dy=Arrow.speed)

    def update(self):
        """ Check if bottom edge has reached screen bottom. """
        if self.bottom > games.screen.height:
            self.end_game()
            self.destroy()

    def handle_caught(self):
        """ Destroy self if caught. """
        self.destroy()

    def end_game(self):
        """ End the game. """
        end_message = games.Message(value="Game Over",
                                    size=90,
                                    color=color.red,
                                    x=games.screen.width / 2,
                                    y=games.screen.height / 2,
                                    lifetime=5 * games.screen.fps,
                                    after_death=games.screen.quit)
        games.screen.add(end_message)


class Robin(games.Sprite):
    """
    A chef which moves left and right, dropping pizzas.
    """
    image = games.load_image("images/robin hood.png")

    def __init__(self, y=55, speed=2, odds_change=200):
        """ Initialize the Chef object. """
        super(Robin, self).__init__(image=Robin.image,
                                   x=games.screen.width / 2,
                                   y=y,
                                   dx=speed)

        self.odds_change = odds_change
        self.time_til_drop = 0

    def update(self):
        """ Determine if direction needs to be reversed. """
        if self.left < 0 or self.right > games.screen.width:
            self.dx = -self.dx
        elif random.randrange(self.odds_change) == 0:
            self.dx = -self.dx

        self.check_drop()

    def check_drop(self):
        """ Decrease countdown or drop pizza and reset countdown. """
        if self.time_til_drop > 0:
            self.time_til_drop -= 1
        else:
            new_arrow = Arrow(x=self.x)
            games.screen.add(new_arrow)

            # set buffer to approx 30% of pizza height, regardless of pizza speed
            self.time_til_drop = int(new_arrow.height * 1.3 / Arrow.speed) + 1


def main():
    """ Play the game. """
    bg_image = games.load_image("images/castle.jpg", transparent=False)
    games.screen.background = bg_image

    the_robin = Robin()
    games.screen.add(the_robin)

    the_target = Target()
    games.screen.add(the_target)

    games.mouse.is_visible = False

    games.screen.event_grab = True
    games.screen.mainloop()


# start it up!
main()