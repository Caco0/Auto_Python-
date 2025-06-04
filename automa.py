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

# print(produtos)
# 4º Cadastrar um produto
for linha in produtos.index:
    pyautogui.click(x=-1263, y=244)

    codigo = str(produtos.loc[linha, "codigo"])
    pyautogui.write(codigo)
    pyautogui.press("tab")

    marca = str(produtos.loc[linha, "marca"])
    pyautogui.write(marca)
    pyautogui.press("tab")

    tipo = produtos.loc[linha, "tipo"]
    pyautogui.write(tipo)
    pyautogui.press("tab")

    categoria = str(produtos.loc[linha, "categoria"])
    pyautogui.write(categoria)
    pyautogui.press("tab")

    preco_unitario = str(produtos.loc[linha, "preco_unitario"])
    pyautogui.write(preco_unitario)
    pyautogui.press("tab")

    custo = str(produtos.loc[linha, "custo"])
    pyautogui.write(custo)
    pyautogui.press("tab")

    obs = str(produtos.loc[linha, "obs"])
    if obs != "nan":
        pyautogui.write(obs)
    else:
        pyautogui.write("")

    pyautogui.press("tab")
    pyautogui.press("enter")

    pyautogui.scroll(10000)


# 5º Repetir para todos os produtos
