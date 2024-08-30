
def onIn_background():
    while True:
        if 10 > maqueen.ultrasonic(PingUnit.CENTIMETERS):
            music.play(music.string_playable("C5 B A G F E D C ", 300),
            music.PlaybackMode.UNTIL_DONE)
        else:
            basic.pause(100)   

control.in_background(onIn_background)

def do_drive_forwad(speed:number, duration: number):
    maqueen.write_led(maqueen.LED.LED_ALL, maqueen.LEDswitch.TURN_ON)
    maqueen.motor_run(maqueen.Motors.ALL, maqueen.Dir.CW, speed )
    basic.pause(duration)
    maqueen.motor_stop(maqueen.Motors.ALL)




def on_logo_event_pressed():
    music.built_in_playable_melody(Melodies.POWER_UP)
    do_drive_forwad(100,1000)


input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_event_pressed)

base.show_icon(IconNames.CONFUSED)