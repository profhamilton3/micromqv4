
def onIn_background():
    while True:
        if 10 > maqueen.ultrasonic(PingUnit.CENTIMETERS):
            music.built_in_playable_melody(Melodies.WAWAWAWAA)
        else:
            basic.pause(100)   

control.in_background(onIn_background)

def do_drive_forward(speed:number, duration: number):
    maqueen.write_led(maqueen.LED.LED_ALL, maqueen.LEDswitch.TURN_ON)
    maqueen.motor_run(maqueen.Motors.ALL, maqueen.Dir.CW, speed )
    music.built_in_playable_melody(Melodies.POWER_UP)
    basic.pause(duration)
    maqueen.motor_stop(maqueen.Motors.ALL)

def do_drive_backward(speed:number, duration: number):
    maqueen.write_led(maqueen.LED.LED_ALL, maqueen.LEDswitch.TURN_ON)
    maqueen.motor_run(maqueen.Motors.ALL, maqueen.Dir.CCW, speed )
    music.built_in_playable_melody(Melodies.POWER_DOWN)
    basic.pause(duration)
    maqueen.motor_stop(maqueen.Motors.ALL)

def do_spin_left(speed:number, duration: number):
    maqueen.write_led(maqueen.LED.LED_ALL, maqueen.LEDswitch.TURN_OFF)
    maqueen.write_led(maqueen.LED.LED_LEFT, maqueen.LEDswitch.TURN_ON)
    maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CCW, speed )
    maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CW, speed )
    music.built_in_playable_melody(Melodies.PUNCHLINE)
    basic.pause(duration)
    maqueen.motor_stop(maqueen.Motors.ALL)

def do_spin_right(speed:number, duration: number):
    maqueen.write_led(maqueen.LED.LED_ALL, maqueen.LEDswitch.TURN_OFF)
    maqueen.write_led(maqueen.LED.LED_RIGHT, maqueen.LEDswitch.TURN_ON)
    maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CW, speed )
    maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CCW, speed )
    music.built_in_playable_melody(Melodies.PUNCHLINE)
    basic.pause(duration)
    maqueen.motor_stop(maqueen.Motors.ALL)


def on_logo_event_pressed():
    music.built_in_playable_melody(Melodies.POWER_UP)
    do_drive_forward(100,1000)
    do_spin_left(75,750)
    do_drive_backward(75,750)
    do_spin_right(75,750)
    do_drive_forward(50,500)
    


input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_event_pressed)

base.show_icon(IconNames.CONFUSED)