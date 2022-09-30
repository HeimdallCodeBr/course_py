import pyautogui

botao_atividade = pyautogui.locateOnScreen('7.png')
print(botao_atividade)
pyautogui.click(botao_atividade)
