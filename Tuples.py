game_list= ("Dead and Buried",
            "TF2",
            "Rocket League",
            "Just Cause 3",
            "Stick Fight",
            "Portal 2",
            "Cluster Truck",
            "The Lab",
            "Geometry Dash",
            "SSBB")
print(len(game_list))
num5game = game_list[4]
print(num5game)
middle5 = game_list[3:7]
print(middle5)
last4 = game_list[6:]
print(last4)
evens = game_list[::2]
print(evens)
backwards = game_list[::-1]
print(backwards)
for i in game_list:
    print(i)
print(game_list)
game_list += ("11",12,13.0,14,"15")
print(game_list)
