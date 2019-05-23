from pyparrot.Minidrone import Mambo

# you will need to change this to the address of YOUR mambo
mamboAddr = "e0:14:7e:65:3d:cb"

# make my mambo object
# remember to set True/False for the wifi depending on if you are using the wifi or the BLE to connect
mambo = Mambo(mamboAddr, use_wifi=False)
#connecting to drone
print("trying to connect")
success = mambo.connect(num_retries=3)
print("connected: %s" % success)
#functions to counteract each movement so there is less sway
def fw(p,d):
    mambo.fly_direct(roll=0, pitch=p, yaw=0, vertical_movement=0, duration=d)
    cp =p*-2
    cd =d*.25
    mambo.fly_direct(roll=0, pitch=cp, yaw=0, vertical_movement=0, duration=cd)
    
def sw(r,d):
    mambo.fly_direct(roll=r, pitch=0, yaw=0, vertical_movement=0, duration=d)
    cr =r*-2
    cd =d*.25
    mambo.fly_direct(roll=cr, pitch=0, yaw=0, vertical_movement=0, duration=cd)
    
if (success):
    # get the state information
    print("sleeping")
    mambo.smart_sleep(2)
    mambo.ask_for_state_update()
    mambo.smart_sleep(2)

    print("taking off!")
    mambo.safe_takeoff(1)
    mambo.smart_sleep(2)

    #going through the bottom of the chair
    
    mambo.fly_direct(roll=0, pitch=0, yaw=0, vertical_movement=-5, duration=2)
    fw(35,4)

    #going around rope
    #right
    mambo.smart_sleep(2)
    sw(20,1.75)
    #forward
    mambo.smart_sleep(2)
    fw(35,2)
    #left
    mambo.smart_sleep(3)
    sw(-20,3.5)
    #backwards all the way to chair
    mambo.smart_sleep(4)
    fw(-35,4.25)
    #flying up to go through back
    mambo.smart_sleep(2)
    mambo.fly_direct(roll=0, pitch=0, yaw=0, vertical_movement=10, duration=3)
    mambo.smart_sleep(2)
    #going to and through back of chair
    sw(20,2.25)
    #going through the horizontal part of chair
    mambo.smart_sleep(2)
    mambo.fly_direct(roll=0, pitch=0, yaw=0, vertical_movement=-7, duration=3)
    mambo.smart_sleep(2)
    #going backwards through bottom of chair to landing pad
    mambo.smart_sleep(2)
    fw(-35,3.5)
    #flip
    mambo.smart_sleep(2)
    mambo.flip(direction = "front")
    #landing
    print("landing")
    mambo.safe_land(5)
    mambo.smart_sleep(5)

    print("disconnect")
    mambo.disconnect()
