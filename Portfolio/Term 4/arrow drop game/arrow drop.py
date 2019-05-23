from superwires import games, color
import random
SCORE = 0

games.init(screen_width=580, screen_height=480, fps=50)

class Arrow(games.Sprite):


    def handle_collide(self):
        global SCORE
        self.x = random.randrange(games.screen.width)
        self.y = random.randrange(games.screen.width)
        SCORE += 1
    def update(self):
        global SCORE
        "Reverse a velocity component if edge of the screen is reached"
        if self.right > games.screen.width or self.left < 0:
            self.dx = -self.dx

        if self.bottom > games.screen.height or self.top < 0:
            self.dy = -self.dy


        # if self.left > games.screen.width:
        #     self.right = 0
        #     SCORE +=1
        # if self.right < 0:
        #     self.left = games.screen.width
        #     SCORE +=1
        # if self.bottom > games.screen.height or self.top < 0:
        #     self.dy = -self.dy
        #     SCORE +=1



class Target(games.Sprite):
    def update(self):
        self.x = games.mouse.x
        self.check_collide()
    def check_collide(self):
        for arrow in self.overlapping_sprites:
            arrow.handle_collide()






class ScText(games.Text):
    def update(self):
        self.value = SCORE



def main():
    #load images
    bg_img = games.load_image("images\castle.jpg", transparent=False)
    games.screen.background = bg_img
    target_img = games.load_image("images/target.jfif", transparent=True)
    arrow_img = games.load_image("images\Arrow.jfif", transparent=True)

    #set images
    arrow = Arrow(image=arrow_img,
                  x=games.screen.width/2,
                  y=games.screen.height/2,
                  dx=10,
                  dy=-10)
    arrow1 = Arrow(image=arrow_img,
                  x=games.screen.width / 2,
                  y=games.screen.height / 2,
                  dx=-15,
                  dy=15)
    arrow2 = Arrow(image=arrow_img,
                  x=games.screen.width / 2,
                  y=games.screen.height / 2,
                  dx=20,
                  dy=20)
    target = Target(image=target_img,
                    x=games.mouse.x,
                    y=450)


    score = ScText(value=SCORE,
                   is_collideable= False,
                   size=60,
                   color= color.black,
                   x=530,
                   y=30)

    #add images
    games.screen.add(score)
    games.screen.add(arrow)
    games.screen.add(arrow1)
    games.screen.add(arrow2)
    games.screen.add(target)

    games.screen.mainloop()

# game_over = games.Message(value="Game Over",
#                           size=100,
#                           color=color.blue,
#                           x=games.screen.width/2,
#                           y=games.screen.height/2,
#                           lifetime=250,
#                           after_death=games.screen.quit)
# games.screen.add(game_over)





    games.screen.mainloop()

main()