import pyautogui

botao_atividade = pyautogui.locateOnScreen('1.png')
pyautogui.click(botao_atividade)
print(botao_atividade)
