#Jared M.
#10/12/18
loops = 2

while True:
    print("I have looped", loops, "times")
    loops = (loops*loops)/1.9999
    if loops > 9999999999999999999:
        break
