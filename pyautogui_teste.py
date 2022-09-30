import pyautogui

botao_atividade = pyautogui.locateOnScreen('1.png')
print(botao_atividade)
pyautogui.click(botao_atividade)
