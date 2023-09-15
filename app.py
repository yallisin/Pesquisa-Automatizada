import pyautogui as pa
import time

pa.PAUSE = 1

pa.press('win')
pa.write("chrome")
pa.press('ENTER')
time.sleep(2)
pa.click(x=334, y=648)
pa.write('Youtube')
pa.press('ENTER')
time.sleep(4)
pa.click(x=300, y=333)
time.sleep(6)
pa.click(x=602, y=112)
pa.write("Banda Resgate")
time.sleep(5)
pa.press('ENTER')
time.sleep(5)
pa.click(x=483, y=687)