
from bangtal import *

setGameOption(GameOption.INVENTORY_BUTTON, False)
setGameOption(GameOption.MESSAGE_BOX_BUTTON, False)

sceneWHITE = Scene("강의 콘텐츠", "pyim/scene.jpg")

image1 = Object("pyim/1.jpg")
image2 = Object("pyim/2.jpg")
image3 = Object("pyim/3.jpg")
image4 = Object("pyim/4.jpg")
image5 = Object("pyim/5.jpg")
image6 = Object("pyim/6.jpg")
image7 = Object("pyim/7.jpg")
image8 = Object("pyim/8.jpg")
image9 = Object("pyim/9.jpg")

image1.x = 100; image1.y = 444
image2.x = 322; image2.y = 444
image3.x = 544; image3.y = 444
image4.x = 100; image4.y = 444
image5.x = 322; image5.y = 444
image6.x = 544; image6.y = 444
image7.x = 100; image7.y = 444
image8.x = 322; image8.y = 444


image1.locate(sceneWHITE, 100, 444)
image3.locate(sceneWHITE, 322, 444)
image2.locate(sceneWHITE, 544, 444)
image7.locate(sceneWHITE, 100, 222)
image8.locate(sceneWHITE, 322, 222)
image6.locate(sceneWHITE, 544, 222)
image4.locate(sceneWHITE, 100, 000)
image5.locate(sceneWHITE, 322, 000)
# image9.locate(sceneWHITE, 544, 000)
# 9번이 안보이는 이미지. 

image1.show()
image2.show()
image3.show()
image4.show()
image5.show()
image6.show()
image7.show()
image8.show()
image9.show()

def MouseMOVE1(x,y,action):
    if action == MouseAction.DRAG_LEFT:
        if image1.x != 100:
           image1.x = image1.x - 222
    if action == MouseAction.DRAG_RIGHT:
        if image1.x != 544:
            image1.x = image1.x + 222
    if action == MouseAction.DRAG_UP:
        if image1.y != 444:
            image1.y = image1.y + 222
    if action == MouseAction.DRAG_DOWN:
        if image1.y != 0:
            image1.y = image1. y - 222
    image1.locate(sceneWHITE, image1.x, image1.y)
    winpos(x,y)

def MouseMOVE2(x,y,action):
    if action == MouseAction.DRAG_LEFT:
        if image2.x != 100:
           image2.x = image2.x - 222
    if action == MouseAction.DRAG_RIGHT:
        if image2.x != 544:
            image2.x = image2.x + 222
    if action == MouseAction.DRAG_UP:
        if image2.y != 444:
            image2.y = image2.y + 222
    if action == MouseAction.DRAG_DOWN:
        if image2.y != 0:
            image2.y = image2. y - 222
    image2.locate(sceneWHITE, image2.x, image2.y)
    winpos(x,y)

def MouseMOVE3(x,y,action):
    if action == MouseAction.DRAG_LEFT:
        if image3.x != 100:
           image3.x = image3.x - 222
    if action == MouseAction.DRAG_RIGHT:
        if image3.x != 544:
            image3.x = image3.x + 222
    if action == MouseAction.DRAG_UP:
        if image3.y != 444:
            image3.y = image3.y + 222
    if action == MouseAction.DRAG_DOWN:
        if image3.y != 0:
            image3.y = image3. y - 222
    image3.locate(sceneWHITE, image3.x, image3.y)
    winpos(x,y)

def MouseMOVE4(x,y,action):
    if action == MouseAction.DRAG_LEFT:
        if image4.x != 100:
           image4.x = image4.x - 222
    if action == MouseAction.DRAG_RIGHT:
        if image4.x != 544:
            image4.x = image4.x + 222
    if action == MouseAction.DRAG_UP:
        if image4.y != 444:
            image4.y = image4.y + 222
    if action == MouseAction.DRAG_DOWN:
        if image4.y != 0:
            image4.y = image4. y - 222
    image4.locate(sceneWHITE, image4.x, image4.y)
    winpos(x,y)

def MouseMOVE5(x,y,action):
    if action == MouseAction.DRAG_LEFT:
        if image5.x != 100:
           image5.x = image5.x - 222
    if action == MouseAction.DRAG_RIGHT:
        if image5.x != 544:
            image5.x = image5.x + 222
    if action == MouseAction.DRAG_UP:
        if image5.y != 444:
            image5.y = image5.y + 222
    if action == MouseAction.DRAG_DOWN:
        if image5.y != 0:
            image5.y = image5. y - 222
    image5.locate(sceneWHITE, image5.x, image5.y)
    winpos(x,y)

def MouseMOVE6(x,y,action):
    if action == MouseAction.DRAG_LEFT:
        if image6.x != 100:
           image6.x = image6.x - 222
    if action == MouseAction.DRAG_RIGHT:
        if image6.x != 544:
            image6.x = image6.x + 222
    if action == MouseAction.DRAG_UP:
        if image6.y != 444:
            image6.y = image6.y + 222
    if action == MouseAction.DRAG_DOWN:
        if image6.y != 0:
            image6.y = image6. y - 222
    image6.locate(sceneWHITE, image6.x, image6.y)
    winpos(x,y)

def MouseMOVE7(x,y,action):
    if action == MouseAction.DRAG_LEFT:
        if image7.x != 100:
           image7.x = image7.x - 222
    if action == MouseAction.DRAG_RIGHT:
        if image7.x != 544:
            image7.x = image7.x + 222
    if action == MouseAction.DRAG_UP:
        if image7.y != 444:
            image7.y = image7.y + 222
    if action == MouseAction.DRAG_DOWN:
        if image7.y != 0:
            image7.y = image7. y - 222
    image7.locate(sceneWHITE, image7.x, image7.y)
    winpos(x,y)

def MouseMOVE8(x,y,action):
    if action == MouseAction.DRAG_LEFT:
        if image8.x != 100:
           image8.x = image8.x - 222
    if action == MouseAction.DRAG_RIGHT:
        if image8.x != 544:
            image8.x = image8.x + 222
    if action == MouseAction.DRAG_UP:
        if image8.y != 444:
            image8.y = image8.y + 222
    if action == MouseAction.DRAG_DOWN:
        if image8.y != 0:
            image8.y = image8. y - 222
    image8.locate(sceneWHITE, image8.x, image8.y)
    


def winpos(x,y):
    if image1.x ==100 & image1.y ==444 & image2.x ==322 & image2.y ==444 & image3.x ==544 & image3.y ==444:
        if image4.x ==100 & image2.y ==222 & image5.x ==322 & image5.y ==222 & image6.x ==544 & image6.y ==222:
            if image7.x ==100 & image7.y ==000 & image8.x ==322 & image8.y ==000:
                print("GG")
                endgame()
image1.onMouseAction = MouseMOVE1
image2.onMouseAction = MouseMOVE2
image3.onMouseAction = MouseMOVE3
image4.onMouseAction = MouseMOVE4
image5.onMouseAction = MouseMOVE5
image6.onMouseAction = MouseMOVE6
image7.onMouseAction = MouseMOVE7
image8.onMouseAction = MouseMOVE8



startGame(sceneWHITE)
