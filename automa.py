import pyautogui
import time
import pandas as pd

pyautogui.PAUSE = 0.5
# 1º passo entrar no sistema da empresa - https://dlp.hashtagtreinamentos.com/python/intensivao/login
pyautogui.press("win")
pyautogui.write("Microsoft Edge Dev")
pyautogui.press("enter")

pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(1)

# 2º passo fazer login

pyautogui.click(x=-1167, y=362)
pyautogui.write("cacotpds@gmail.com")
time.sleep(0.5)
pyautogui.press("tab")
pyautogui.write("123456")
pyautogui.press("tab")
pyautogui.press("enter")

# 3º Importar base de dados

time.sleep(3)

produtos = pd.read_csv("../Bot/Python Power Up/produtos.csv")

print(produtos)

# 4º Cadastrar um produto
# 5º Repetir para todos os produtos
