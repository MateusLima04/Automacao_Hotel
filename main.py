import pyautogui
import time

pyautogui.PAUSE = 2


#abrir o navegador
pyautogui.press("win")
time.sleep(2)
pyautogui.click(x=2122, y=81)
pyautogui.write("chrome")
pyautogui.press("enter")
time.sleep(2)
pyautogui.write("http://localhost:63342/Hotel/Hotel-Front/index.html?_ijt=4eldr7m9dtf6v5a8581cl1qtvi&_ij_reload=RELOAD_ON_SAVE")
pyautogui.press("enter")
time.sleep(2)

# função para definir o tipo do quarto
def tipo_quarto(numero):
    final = numero % 100 

    if final in [1, 2]:
        return 0  # Simples
    elif final in [3, 4]:
        return 1  # Duplo
    else:
        return 2  # Luxo

pyautogui.PAUSE = 0.3
# loop pelos andares
for andar in [100, 200, 300]:
    
    # loop pelos quartos de cada andar
    for i in range(1, 7):  # 1 até 6
        numero_quarto = andar + i

        # clicar no campo número
        pyautogui.click(x=1588, y=507)
        pyautogui.write(str(numero_quarto))

        # ir para seleção do tipo
        pyautogui.press("tab")

        # escolher o tipo correto
        tipo = tipo_quarto(numero_quarto)

        pyautogui.press("enter")  # abre dropdown

        for _ in range(tipo):
            pyautogui.press("down")

        pyautogui.press("enter")  # seleciona

        # ir para botão cadastrar
        pyautogui.press("tab")
        pyautogui.press("enter")


        time.sleep(1)  # pequeno delay para garantir
