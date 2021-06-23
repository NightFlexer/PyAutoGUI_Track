import pynput
import time
import pyautogui
out_fn = "tmp_text.txt"
#--------------
def position():
    x, y = pyautogui.position()
    t = 1 # время движения
    #print(x, y)
    return(x, y, t) # функция вернёт x, y
#--------------
def f_moveTo():
    tmp_text = open(out_fn, 'a')
    tmp_text.write("pyautogui.moveTo")
    tmp_text.write(str(position()))
    tmp_text.write("\n")
    tmp_text.close()
#---------------
def f_dragTo():
    tmp_text = open(out_fn, 'a')
    tmp_text.write("pyautogui.dragTo")
    tmp_text.write(str(position()))
    tmp_text.write("\n")
    tmp_text.close()
#---------------
from pynput import keyboard

def on_press(key):
    try:
        print('Нажата клавиша: {0} '.format(key.char))
    except AttributeError:
        print('Нажата клавиша: {0}'.format(key))

def on_release(key):
    #print('{0} released'.format(key))
    if key == keyboard.Key.esc:
        # Stop listener
        return False
    elif key == keyboard.Key.ctrl_l:
        print("Захват точки moveTo")
        f_moveTo()
    elif key == keyboard.Key.alt_l:
        print("Отмечена точка dragTo")
        f_dragTo()
#--------------		
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

#--------------
listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)
listener.start()