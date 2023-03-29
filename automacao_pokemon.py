#!/usr/bin/env python
# coding: utf-8

# # Desafio Tkinter
# 
# Criar um sistema (tkinter, figma.com, proxlight designer) como ferramenta de pesquisa de Pokémon. A busca dos Pokémon poderá ser feita por API (requests, json) ou por web-scrapping (Selenium).
# 
# - arquivo 'REVISÃO - Pokémon (automações)': coleta das informações dos pokémon por meio de automações
# - arquivo 'REVISÃO - Pokémon (tkinter)': criação do sistema com a interface para o usuário

# In[16]:


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
servico = Service(ChromeDriverManager().install())
import time
from PIL import Image
import os
import shutil
from pprint import pprint
import urllib
import pandas as pd


# ##### Coletar as informações do site
# https://pokemondb.net/pokedex/national

# In[21]:


# acessar o site
browser = webdriver.Chrome(service=servico)
browser.maximize_window()
browser.get('https://pokemondb.net/pokedex/national')

# pegar as informações de cada pokémon
lista_pokemon = browser.find_elements(By.CLASS_NAME, 'infocard')

dicionario = {}

for i, pokemon in enumerate(lista_pokemon):
    
    #numero
    i += 1
    
    #nome
    nome = pokemon.find_element(By.CLASS_NAME, 'ent-name').text
    nome = nome.lower()
    
    #tipos
    lista_tipos = pokemon.find_elements(By.CLASS_NAME, 'itype')
    for tipos in lista_tipos:
        tipo = lista_tipos[0].text
        if len(lista_tipos)>1:
            tipo = f'{lista_tipos[0].text} / {lista_tipos[1].text}'
            
    #url imagem
    nome_url = nome.replace("'", "").replace(".", "").replace(" ", "-").replace(":", "").replace('♀', '-f').replace('♂', '-m')
    if i <= 905:
        url_imagem = f'https://img.pokemondb.net/sprites/home/normal/2x/{nome_url}.jpg'
    elif i >= 906:
        url_imagem = f'https://img.pokemondb.net/sprites/scarlet-violet/normal/{nome_url}.png'

    nome_imagem = f'{i} - {nome_url}.png'
    
    #geração
    if i <= 151:
        geracao = 'Kanto (gen 1)'
    elif 152 <= i <= 251:
        geracao = 'Johto (gen 2)'
    elif 252 <= i <= 386:
        geracao = 'Hoenn (gen 3)'
    elif 387 <= i <= 493:
        geracao = 'Sinnoh (gen 4)'
    elif 494 <= i <= 649:
        geracao = 'Unova (gen 5)'
    elif 650 <= i <= 721:
        geracao = 'Kalos (gen 6)'
    elif 722 <= i <= 809:
        geracao = 'Alola (gen 7)'
    elif 810 <= i <= 905:
        geracao = 'Galar (gen 8)'
    elif 906 <= i <= 1010:
        geracao = 'Paldea (gen 9)'
    
    #print e salvar em dicionário
    time.sleep(0.5)
    print(f'{i} - {nome} - {tipo} - {geracao} - {url_imagem} - {nome_imagem}')
    dicionario[i] = nome, tipo, geracao, url_imagem, nome_imagem


# ###### Exportar o dicionário de informações em arquivo csv

# In[47]:


df = pd.DataFrame.from_dict(dicionario, orient='index', columns=['nome', 'tipo', 'gen', 'url', 'png'])
display(df)

df.to_excel('dicionario_pokemon.xlsx')


# In[ ]:


# CASO EU QUISESSE ACESSAR ESTE DICIONÁRIO DIRETAMENTE NO OUTRO ARQUIVO 'REVISÃO - Pokémon (tkinter)':

# abrir bloco de notas
# copiar e colar todo o dicionário 
# salvar o bloco de notas como 'arquivo.py'
# no outro arquivo python, para importar o dicionário: from arquivo import dicionario


# ###### Gerar as imagens dos pokémon

# In[51]:


#imagens
#abrir navegador
browser = webdriver.Chrome(service=servico)
browser.maximize_window()
time.sleep(1)

for chave in dicionario:  
    
    # definir 'i' e 'nome'
    i = chave
    nome_url = dicionario[chave][4]
    
    if i >= 669:
    
        # acessar o link da imagem
        url = dicionario[chave][3]
        url = url.replace('♀', '-f').replace('♂', '-m').replace('é', 'e')
        print(url)
        browser.get(url)
        time.sleep(1)
        
        #placeholder do local de armazenamento das imagens
        local_arquivo_python = os.getcwd()
        local_imagens = fr'{local_arquivo_python}\REVISÃO - Pokémon'

        #printar a página
        browser.save_screenshot(fr'{local_imagens}\{nome_url}')

        #abrir, editar, salvar o print
        imagem = Image.open(fr'{local_imagens}\{nome_url}')
        elemento = browser.find_element(By.XPATH, '/html/body/img')
        posicao = elemento.location
        tamanho = elemento.size
        imagem = imagem.crop((posicao['x'], posicao['y'], posicao['x']+tamanho['width'], posicao['y']+tamanho['height']))
        imagem.save(fr'{local_imagens}\{nome_url}')


# Ir para o arquivo 'REVISÃO - Pokémon (tkinter)' para a janela tkinter e finalziação do projeto!

# In[ ]:




