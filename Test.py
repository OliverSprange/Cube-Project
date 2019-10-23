import msvcrt
while True:
    buttonPress = msvcrt.getch()
    if msvcrt.kbhit():
        buttonPress += msvcrt.getch()
        print(buttonPress)