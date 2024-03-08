# Passo a Passo do projeto 
# testando uma atualização de arquivo
# Passo 1: Entrar no sistema da empresa 
 #https://dlp.hashtagtreinamentos.com/python/intensivao/login
import pyautogui
import time

pyautogui.PAUSE = 0.5

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")

#dar uma pausa
time.sleep(2)

# Passo 2 : Fazer login

pyautogui.click(x=874, y=371)       

pyautogui.write("epprecht.ruth@gmail.com")
pyautogui.press("tab")
pyautogui.write("Pai.mae484372378")

pyautogui.click(x=983, y=539)
time.sleep(3)

# Passo 3: Importar a base de dados

import pandas

tabela = pandas.read_csv("produtos.csv")

# Passo 4: Cadastrar 1 produto

pyautogui.click(x=690, y=260)

#codigo do produto
for linha in tabela.index:

    #clicar no primeiro campo
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(codigo)
    pyautogui.press("tab")

    pyautogui.write(tabela.loc[linha, "marca"])
    pyautogui.press("tab")

    pyautogui.write(tabela.loc[linha, "tipo"])
    pyautogui.press("tab")

    # str= string -> texto
    # str "um" = "1"
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    obs = (tabela.loc[linha , "obs"])  
    if not pandas.isna(obs):
        pyautogui.write(obs)
    pyautogui.press("tab")

    pyautogui.press("enter") 
    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.click(x=259, y=679)
    pyautogui.scroll(5000)
     




# Passo 5: Repetir o processo de cadastro até acabar
