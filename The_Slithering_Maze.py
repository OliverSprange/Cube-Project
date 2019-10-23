import sys, string, time
from os import system, name
from os.path import dirname, join
from random import randrange


playerPosRow = 4
playerPosColumn = 0

lives = 3
theFlag = False

current_dir = dirname(__file__)

moveMathDict = {'UP': -1, 'LEFT': -1, 'DOWN': 1, 'RIGHT': 1}
maze = [["" for rows in range(5)] for columns in range(5)]

maze[playerPosRow][playerPosColumn] = 'PLYR'

def screen_clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

if sys.platform == 'win32':
    import msvcrt
    arrowDictx00 = {b'\x00H': 'UP', b'\x00K': 'LEFT', b'\x00P': 'DOWN', b'\x00M': 'RIGHT'}
    arrowDictxe0 = {b'\xe0H': 'UP', b'\xe0K': 'LEFT', b'\xe0P': 'DOWN', b'\xe0M': 'RIGHT'}
    def get_arrow():
        buttonPress = msvcrt.getch()
        while True:
            if msvcrt.kbhit() and buttonPress == b'\x00':
                buttonPress += msvcrt.getch()
                return arrowDictx00.get(buttonPress)
            elif msvcrt.kbhit() and buttonPress == b'\xe0':
                buttonPress += msvcrt.getch()
                return arrowDictxe0.get(buttonPress)
            else:
                time.sleep(0.01)
                continue

else:
    arrowDict = {'w': 'UP', 'a': 'LEFT', 's': 'DOWN', 'd': 'RIGHT'}
    def get_arrow():
        while True:
            try:
                directionOfPlayer = input("Please type 'W', 'A', 'S' or 'D' and Enter to choose a direction...")
            except ValueError:
                continue
            
            directionOfPlayer = directionOfPlayer.translate(str.maketrans('', '', string.punctuation))

            if directionOfPlayer.lower() in arrowDict:
                return arrowDict.get(directionOfPlayer.lower())
            else:
                continue

def clearTile():
    maze[playerPosRow][playerPosColumn] = " "

def challenge(chal):
    global lives, theFlag
    currentChallenge = []
    screen_clear()
    with open(join(current_dir, "./challenges.txt"), "r") as f:
        while True:
            line = f.readline()
            if chal in line:
                while True:
                    if line == "\n":
                        theFlag = True
                        break
                    else:
                        #if chal in line:
                        #    line = f.readline()
                        currentChallenge.append(line)
                        line = f.readline()
            if theFlag == True:
                theFlag = False
                break

    for elements in currentChallenge:
        if elements == 2:
            print()
        print("".join(elements), end="")
    currentChallenge.clear()
    numList = []

    with open(join(current_dir, "./solutions.txt"), "r") as f:
        solutions = f.readline()
        for numbers in solutions:
            if numbers.isdigit():
                numList.append(int(numbers))
        for line in f:
            if line == chal + '\n':
                for _ in range(4):
                    if _ == 0:
                        print()
                    print("".join(f.__next__()), end="")
    
    while True:
        try:
            answer = int(input("\nChoose one of the 4 possibilities:\n\n"))
        except ValueError:
            print("\nOnly accepted characters are numbers.")
            continue

        if answer < 0 or answer > 4:
            print("\nOnly the numbers 1, 2, 3 & 4 are accepted.")
            continue

        if answer != numList[int(''.join(filter(str.isdigit, chal))) - 1]:
            lives -= 1
            if lives == 2:
                print("\nYou have", lives, "lives remaining. Try again.")
                continue
            elif lives == 1:
                print("\nYou have", lives, "life remaining. Try again.")
                continue
            else:
                print("\nYou have lost the game.")
                time.sleep(10)
                break
        else:
            print("\nThat is correct.")
            break

def moveThePlayer():
    hasPrinted = False
    while True:
        if not hasPrinted:
            print("\nPlease choose a direction - you can't go outside the boundaries!\n")
            hasPrinted = True

        direction = get_arrow()
        
        # Here comes the "borders" which probably can be made easier, but meh
        if direction == 'UP':
            if playerPosRow == 0:
                print("You can't go any further up.\n")
                continue
            else:
                return direction, moveMathDict.get(direction)
                
        elif direction == 'DOWN':
            if playerPosRow == 4:
                print("You can't go any further down.\n")
                continue
            else:
                return direction, moveMathDict.get(direction)
                
        elif direction == 'LEFT':
            if playerPosColumn == 0:
                print("You can't go any further left.\n")
                continue
            else:
                return direction, moveMathDict.get(direction)
                
        elif direction == 'RIGHT':
            if playerPosColumn == 4:
                print("You can't go any further right.\n")
                continue
            else:
                return direction, moveMathDict.get(direction)

for i in range(0, 24):
    while True:
        tempRow = randrange(0, 25) // 5
        tempColumn = randrange(0, 25) % 5

        if maze[tempRow][tempColumn] == "":
            if i == 0:
                maze[tempRow][tempColumn] = "EXIT"
                break
            elif i < 10:
                maze[tempRow][tempColumn] = "CH0" + str(i)
                break
            else:
                maze[tempRow][tempColumn] = "CH" + str(i)
                break
        else:
            continue

screen_clear()
print("\n\033[93m||===== '\033[91mThe Slithering Maze\033[93m' =====||\033[0m")
time.sleep(0.25)
print("Sorry to disappoint you, but it's not really maze...")
time.sleep(0.25)
print("This map is a copy of the overworld map, but a new one.")
time.sleep(0.25)
print("If you're using Windows, you can move around with the arrow keys..")
time.sleep(0.25)
print("...")
time.sleep(0.25)
print("At least you should be able to.. Depends on the OEM-specific type of your PC")
time.sleep(1)
print("Otherwise, you have to use 'W' for up, 'A' for left, 'S' for down and 'D' for right,")
print("and you have to press [ENTER] in order for me to understand it..!!!")
time.sleep(0.25)
print("The exit randomly spawns on the map, you have to find it.")
print("But beware: On the way, you will encounter challenges!")
time.sleep(0.25)
print("You get 3 lives when you spawn in.")
print("If you answer incorrectly on any challenge, you lose a life.")
print("If you lose your last life, you lose the game.")
time.sleep(0.5)
print("When you get to a challenge, you answer with 1, 2, 3 or 4.")
print("Remember to press [Enter] as well, otherwise I won't \"hear\" it")
input("\nPress [ENTER] to start the game...")
screen_clear()

# Here comes the game itself
while True:
    clearTile()
    print("\nCurrent position (x,y): [ %s , %s ]" % (playerPosRow, playerPosColumn))
    movement = moveThePlayer()
    if movement[0] == 'UP' or movement[0] == 'DOWN':
        playerPosRow += movement[1]
    else:
        playerPosColumn += movement[1]
    moveList = list(movement)
    moveList.clear()
    movement = moveList

    print("Row:", playerPosRow)
    print("Column:", playerPosColumn)

    # Here comes the part where the program checks the upcoming tile
    tileToBe = maze[playerPosRow][playerPosColumn]
    if tileToBe[0] == 'C':
        challenge(tileToBe)
        if lives < 1:
            break
        continue
    elif tileToBe[0] == ' ':
        print("There used to be something here, but it's gone now..")
        continue
    else:
        print("YOU WIN!")
        time.sleep(10)
        break
