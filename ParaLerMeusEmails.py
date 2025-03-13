import pyautogui
import time

pyautogui.PAUSE = 0.5

pyautogui.press("win")

pyautogui.write("Google Chrome")

pyautogui.press("enter")

pyautogui.click(x=-33, y=149)  # ir até a conta

pyautogui.click(x=-290, y=599)  # selecionar email

pyautogui.click(x=-198, y=145)  # gmail

while True:

    pyautogui.click(x=-1638, y=208)  # selecionar tudo

    pyautogui.click(x=-1429, y=213)  # marcar como lido

    pyautogui.click(x=-100, y=211)  # passar a pagina

    time.sleep(2.5)
    
