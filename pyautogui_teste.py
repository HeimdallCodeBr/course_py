import pyautogui

botao_atividade = pyautogui.locateOnScreen('3.png')
x, y, l, a = botao_atividade
pyautogui.click(botao_atividade)
print(x, y, l, a)
