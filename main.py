import pyautogui
from win10toast import ToastNotifier
from time import sleep
import threading

# Configuracoes iniciais
toaster = ToastNotifier()
hp = pyautogui.locateOnScreen('HP.png')
hp_color = (227, 114, 14)
hp_position = (hp[0]+6, hp[1]+14)
hp_position2 = (hp[0]+35, hp[1]+14)
hp_position3 = (hp[0]+150, hp[1]+14)
hp_position4 = (hp[0]+180, hp[1]+14)
item_position = (hp[0]+45, hp[1]+301)
loot_position = (hp[0]+17, hp[1]+174)


def nexus():

    if pyautogui.pixelMatchesColor(int(hp_position[0]), int(hp_position[1]), (227, 114, 14)) == True or pyautogui.pixelMatchesColor(int(hp_position2[0]), int(hp_position2[1]), (227, 114, 14)) == True:
        pyautogui.press('r')
        pyautogui.press('r')
        pyautogui.press('r')
        toaster.show_toast("Realm Mad God!!!",
                           "!!! HP baixo, voltando a nexus !!! ",
                           icon_path="rotmg.ico",
                           duration=10)
        sleep(2)

    else:
        pass


def controle_hp():
    if pyautogui.pixelMatchesColor(int(item_position[0]), int(item_position[1]), (84, 84, 84)) == False:
        if pyautogui.pixelMatchesColor(int(hp_position3[0]), int(hp_position3[1]), (84, 84, 84)) == True or pyautogui.pixelMatchesColor(int(hp_position4[0]), int(hp_position4[1]), (84, 84, 84)) == True:

            pyautogui.press('f')

        else:
            pass
    else:
        pass


def autoloot():

    atual = pyautogui.position()
    
    if pyautogui.pixelMatchesColor(int(hp[0]+15), int(hp[1]+376), (71,71,71)) == True:
        pyautogui.doubleClick(int(hp[0]+15), int(hp[1]+376))
        pyautogui.moveTo(atual)

    if pyautogui.pixelMatchesColor(int(hp[0]+15)+58, int(hp[1]+376), (71,71,71)) == True:
        pyautogui.doubleClick(int(hp[0]+15)+58, int(hp[1]+376))
        pyautogui.moveTo(atual)

    if pyautogui.pixelMatchesColor(int(hp[0]+15)+58*2, int(hp[1]+376), (71,71,71)) == True:
        pyautogui.doubleClick(int(hp[0]+15)+58*2, int(hp[1]+376))
        pyautogui.moveTo(atual)

    if pyautogui.pixelMatchesColor(int(hp[0]+15)+58*3, int(hp[1]+376), (71,71,71)) == True:
        pyautogui.doubleClick(int(hp[0]+15)+58*3, int(hp[1]+376))
        pyautogui.moveTo(atual)

  

    
    

def aim():
    #Em teste ainda#
    try:
        hp = pyautogui.locateOnScreen('teste.png')
        hp_position = (hp[0]+6, hp[1]+14)
        pyautogui.click(int(hp_position[0]), int(hp_position[1]))

    except:
        print('Nao localizado.')


pyautogui.moveTo(int(hp_position[0]), int(hp_position[1]))
toaster.show_toast("Realm Mad God!!!",
                   "!!! Achamos seu HP confira a posicao !!! ",
                   icon_path="rotmg.ico",
                   duration=10)



    

while True:

    controle_hp()
    autoloot()
    threading.Thread(target=nexus).start()

