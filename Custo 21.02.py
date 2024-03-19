import pyautogui as P
import os
from time import sleep
import keyboard

transacao_path = os.path.abspath("transacao.jpg")
importe_path = os.path.abspath("importe.jpg")
importepasta_path = os.path.abspath("importepasta.jpg")
importarxml_path = os.path.abspath("importar.jpg")
confirmar = os.path.abspath("confirmar.jpg")
piscofins = os.path.abspath("piscofins.jpg")
totalitens = os.path.abspath("totalitens.jpg")
geral = os.path.abspath("geral.jpg")
pagamento = os.path.abspath("pagamento.jpg")
selecionar = os.path.abspath("selecionar.jpg")
gravar = os.path.abspath("gravar.jpg")
nao = os.path.abspath("nao.jpg")
okpg = os.path.abspath("gravar.pg.jpg")
caminho_do_arquivo = "dados.txt"


def clicar_imagem(transacao, codigo, tentativas=100):
    for _ in range(tentativas):
        try:
            posicao = P.locateOnScreen(transacao, confidence=0.9)
            if posicao is not None:
                centro_x, centro_y = P.center(posicao)
                P.click(centro_x, centro_y)
                P.write(codigo)
                P.press('enter')
                sucesso = True
                break
            else:
                print(f"...")
        except Exception as e:
            print(f"Procurando transação {e}")
    else:
       if not sucesso:  # Se a flag de sucesso ainda for False, então nenhum sucesso foi alcançado
            raise Exception(f"Erro {tentativas} tentativas.")
    
def clicar_importe(importe, tentativas=200):
    for _ in range(tentativas):
        try:
            posicao = P.locateOnScreen(importe, confidence=0.9)
            if posicao is not None:
                centro_x, centro_y = P.center(posicao)
                P.click(centro_x, centro_y)
                P.press('enter')
                break
            else:
                print(f"...")
        except Exception as e:
            print(f"Erro: tentar_clicar_importe {e}")
    else:
        raise Exception(f"Erro {tentativas} tentativas.")

def clicar_importepasta(importepasta, xml, tentativas=500):
    for _ in range(tentativas):
        try:
            posicao = P.locateOnScreen(importepasta, confidence=0.9)

            if posicao is not None:
                centro_x, centro_y = P.center(posicao)
                P.move(centro_x, centro_y)
                sleep(0.5)
                P.write(xml)
                break
            else:
                print(f"...")
        except Exception as e:
            print(f"Erro: tentar_clicar_importepasta {e}")

    else:
        raise Exception(f"Erro {tentativas} tentativas.")

def clicar_xml(importarxml, tentativas=200):
    for _ in range(tentativas):
        try:
            posicao = P.locateOnScreen(importarxml, confidence=0.9)
            if posicao is not None:
                sleep(1)
                centro_x, centro_y = P.center(posicao)
                P.click(centro_x, centro_y)
                break
            else:
                print(f"...")
        except Exception as e:
            print(f"Erro: clicar_xml {e}")
    else:
        raise Exception(f"Erro {tentativas} tentativas.")

def clicar_importar(confirmar, tentativas=200):
    for _ in range(tentativas):
        try:
            posicao = P.locateOnScreen(confirmar, confidence=0.9)
            if posicao is not None:
                centro_x, centro_y = P.center(posicao)
                P.click(centro_x, centro_y)
                sleep(2)
                #Clicar não cst 109
                for _ in range(10):
                    P.click(812, 410)
                    sleep(0.2)                  
                break
            else:
                print(f"...")
        except Exception as e:
            print(f"Erro: tentar_clicar_importar {e}")
    else:
        raise Exception(f"Erro {tentativas} tentativas.")


    #Alterar data
    for _ in range(5): 
        P.press('tab')

    P.write('29022024')             
    for _ in range(7): 
        P.press('tab')
                                    

    #Tab DP
    ''''for _ in range(12):
        P.press('tab')''''' 
    P.write(dp)
    P.press('tab')
    P.press('tab')
    P.write('5068')
    #Tab Modelo NF PIS
    for _ in range(21):
        P.press('tab') 
    P.write('55')   

def clicar_pis(piscofins, tentativas=200):
    for _ in range(tentativas):
        try:
            posicao = P.locateOnScreen(piscofins, confidence=0.9)
            if posicao is not None:
                centro_x, centro_y = P.center(posicao)
                P.click(centro_x, centro_y)
                break
            else:
                print(f"...")
        except Exception as e:
            print(f"Erro: tentar_clicar_importar {e}")
    else:
        raise Exception(f"Erro {tentativas} tentativas.")

def clicar_pagamento(pagamento, tentativas=200):
    for _ in range(tentativas):
        try:
            posicao = P.locateOnScreen(pagamento, confidence=0.9)
            if posicao is not None:
                centro_x, centro_y = P.center(posicao)
                P.click(centro_x, centro_y)
                break
            else:
                print(f"...")
        except Exception as e:
            print(f"Erro: clicar_pagamento {e}")
    else:
        raise Exception(f"Erro {tentativas}")
    
def clicar_okpg(okpg, tentativas=500):
    for _ in range(tentativas):
        try:
            posicao = P.locateOnScreen(okpg, confidence=0.7)
            if posicao is not None:
                centro_x, centro_y = P.center(posicao)
                P.click(centro_x, centro_y)
                break
            else:
                print(f"...")
        except Exception as e:
            print(f"Procurando ok.pg {e}")
    else:
        raise Exception(f"Erro {tentativas}")

def clicar_selecionar(selecionar, tentativas=500):
    for _ in range(tentativas):
        try:
            posicao = P.locateOnScreen(selecionar, confidence=0.9)
            if posicao is not None:
                centro_x, centro_y = P.center(posicao)
                P.click(centro_x, centro_y)
                P.press('0')
                P.press('tab')
                P.write('100')
                P.press('enter')
                P.press('tab')
                P.press('tab')
                P.press('tab')
                P.press('enter')
                break
            else:
                print(f"...")
        except Exception as e:
            print(f"Erro: clicar_pagamento {e}")
    else:
        raise Exception(f"Erro {tentativas}")
    
def clicar_totalitens(totalitens, tentativas=500):
    for _ in range(tentativas):
        try:
            posicao = P.locateOnScreen(totalitens, confidence=0.9)
            if posicao is not None:
                centro_x, centro_y = P.center(posicao)
                P.click(centro_x, centro_y)
                break
            else:
                print(f"...")
        except Exception as e:
            print(f"Procurando total dos itens {e}")

    else:
        raise Exception(f"Erro {tentativas} tentativas.")
    
    for _ in range(1): 
        sleep(1)
        P.press('tab')
    P.write(codtri)
    P.press('tab')
    P.press('enter')
    sleep(3)
    sleep(1)

def clicar_gravar(gravar, tentativas=200):
    for _ in range(tentativas):
        try:
            posicao = P.locateOnScreen(gravar, confidence=0.9)
            if posicao is not None:
                sleep(1)
                centro_x, centro_y = P.center(posicao)
                P.click(centro_x, centro_y)
                sleep(1)
                sleep(1)
                P.press('enter')
                break
            else:
                print(f"...")
        except Exception as e:
            print(f"Erro: clicar_gravar {e}")
    else:
        raise Exception(f"Erro {tentativas} tentativas.")   

with open(caminho_do_arquivo, 'r') as arquivo:
    for linha in arquivo:
        partes = linha.split('*')
        codigo = partes[3].strip() if len(partes) > 3 else None
        xml = partes[0].strip() if len(partes) > 0 else None
        dp = partes[2].strip() if len(partes) > 2 else None
        codtri = partes[1].strip() if len(partes) > 1 else None

        try:
            clicar_imagem(transacao_path, codigo)
            clicar_importe(importe_path)
            clicar_importepasta(importepasta_path, xml)
            clicar_xml(importarxml_path)
            clicar_importar(confirmar)
            clicar_pis(piscofins)
            clicar_pagamento(pagamento)
            clicar_okpg(okpg)
            clicar_selecionar(selecionar)
            clicar_totalitens(totalitens)
            clicar_gravar(gravar)
            print('Custo', xml,'efetivado!')
        except Exception as e:
            print(f"Erro geral: {e}")
