control.inBackground(function onIn_background() {
    while (true) {
        if (10 > maqueen.Ultrasonic(PingUnit.Centimeters)) {
            music.play(music.stringPlayable("C5 B A G F E D C ", 300), music.PlaybackMode.UntilDone)
        } else {
            basic.pause(100)
        }
        
    }
})
input.onLogoEvent(TouchButtonEvent.Pressed, function on_logo_event_pressed() {
    music.builtInPlayableMelody(Melodies.PowerUp)
    do_drive_forwad
})
