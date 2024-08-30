
def onIn_background():
    while True:
        
        if maqueen.ultrasonic(10):
            pass
        else:
            pass
        
control.in_background(onIn_background)