#!/usr/bin/env python
# coding: utf-8

# # Desafio Tkinter
# 
# Criar um sistema (tkinter, figma.com, proxlight designer) como ferramenta de pesquisa de Pokémon. A busca dos Pokémon poderá ser feita por API (requests, json) ou por web-scrapping (Selenium).
# 
# - arquivo 'REVISÃO - Pokémon (automações)': coleta das informações dos pokémon por meio de automações
# - arquivo 'REVISÃO - Pokémon (tkinter)': criação do sistema com a interface para o usuário

# In[2]:


from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import urllib.request
import io
import pandas as pd


# In[3]:


# importar o dicionário do arquivo backend 'RevisaoPokemonAutomacoes'
df = pd.read_excel('dicionario_pokemon.xlsx')
df = df.drop('Unnamed: 0', axis=1)

# criar lista com todos os tipos
df['tipo'] = df['tipo'].str.split(' / ')
df['tipo 1'] = 0
df['tipo 2'] = 0
for linha in df.index:
    nome = df.loc[linha, 'nome']
    tipagem = df.loc[linha, 'tipo']
    if len(tipagem) > 1:
        df.loc[linha, 'tipo 1'] = tipagem[0]
        df.loc[linha, 'tipo 2'] = tipagem[1]
    elif len(tipagem) == 1:
        df.loc[linha, 'tipo 1'] = tipagem[0]
        df.loc[linha, 'tipo 2'] = tipagem[0]
df = df.drop('tipo', axis=1)
df = df.reset_index()
df['index'] = df['index']+1

#display(df)

# CASO EU QUISESSE ACESSAR ESTE DICIONÁRIO DIRETAMENTE DO OUTRO ARQUIVO 'REVISÃO - Pokémon (automações)':
# abrir bloco de notas
# copiar e colar todo o dicionário 
# salvar o bloco de notas como 'arquivo.py'
# neste arquivo python, para importar o dicionário: from arquivo import dicionario


# In[4]:


#criação da janela
janela = Tk()

#tamanho da janela
janela.geometry("800x800")

#criação do título da janela
janela.title('POKÉMON')

#ajuste/redimensionamento automático da janela
#janela.rowconfigure([0,1], weight=1)
janela.columnconfigure([0,1,2], weight=1)

#definição do background
janela.configure(bg = "#ffffff")

################################################################################################################################

#mensagem (.Label)
#lista suspensa (.Combobox)
#botão (.Button)
mensagem1 = Label(text='Sistema de Busca de Pokémon', font=('Bangers', 25), background='#4169E1', foreground='#7FFFD4', height=4)
mensagem1.grid(row=0, column=0, columnspan=3, sticky='nsew')

mensagem2 = Label(text='Região (geração):', font=('Calibri', 20), height=2)
mensagem2.grid(row=1, column=0, columnspan=2, sticky='nsew')

regioes = list(df['gen'].unique())
listasuspensa1 = ttk.Combobox(janela, values=regioes)
listasuspensa1.grid(row=1, column=2, sticky='nsew')

mensagem3 = Label(text='Tipo primário:', font=('Calibri', 20), height=2)
mensagem3.grid(row=2, column=0, columnspan=2, sticky='nsew')

tipos_primarios = list(df['tipo 1'].unique())
listasuspensa2 = ttk.Combobox(janela, values=tipos_primarios)
listasuspensa2.grid(row=2, column=2, sticky='nsew')

mensagem4 = Label(text='Tipo secundário:', font=('Calibri', 20), height=2)
mensagem4.grid(row=3, column=0, columnspan=2, sticky='nsew')

listasuspensa3 = ttk.Combobox(janela, values=tipos_primarios)
listasuspensa3.grid(row=3, column=2, sticky='nsew')

mensagem5 = Label(text='Lista de Pokémon ?', font=('Calibri', 20))
mensagem5.grid(row=5, column=0, columnspan=2, sticky='nsew')

listasuspensa4 = ttk.Combobox(janela, values=[])
listasuspensa4.grid(row=5, column=2, sticky='nsew')

def filtrar_pokemon():
    
    regiao_escolhida = listasuspensa1.get()
    tipo1_escolhido = listasuspensa2.get()
    tipo2_escolhido = listasuspensa3.get()
    
    if tipo2_escolhido == tipo1_escolhido:
        df1 = df.loc[(df['gen']==regiao_escolhida) & (df['tipo 1']==tipo1_escolhido) & (df['tipo 2']==tipo1_escolhido), :]
        pokemon = df1.loc[:, 'nome']
        
        if len(pokemon)==0:    
            mensagem5['text']='Pokémon não encontrado :('
        else:
            mensagem5['text']='Escolha um Pokémon:'
            listasuspensa4['values']=list(pokemon)
        
    elif tipo2_escolhido != tipo1_escolhido:
        df1 = df.loc[(df['gen']==regiao_escolhida) & (df['tipo 1']==tipo1_escolhido) & (df['tipo 2']==tipo2_escolhido), :]
        pokemon = df1.loc[:, 'nome']
        
        if len(pokemon)==0:    
            mensagem5['text']='Pokémon não encontrado :('
        else:
            mensagem5['text']='Escolha um Pokémon:'           
            listasuspensa4['values']=list(pokemon)
    
    
    
def buscar_pokemon():
    
    # cria uma nova janela
    new_window = Toplevel(janela)
    
    pokemon_escolhido = listasuspensa4.get()
    url_pokemon_escolhido = df.loc[df['nome']==pokemon_escolhido, 'url'].values[0]
        
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
    request = urllib.request.Request(url_pokemon_escolhido, headers=headers)
    with urllib.request.urlopen(request) as u:
        raw_data = u.read()
        
    # Converte a imagem em formato TK
    img = Image.open(io.BytesIO(raw_data))
    img_tk = ImageTk.PhotoImage(img)
    
    # exibe a imagem na nova janela
    label = Label(new_window, image=img_tk)
    label.pack()
    
    # mantém a referência para a imagem para que ela não seja destruída
    label.image = img_tk
    

    
botao1 = Button(text='Filtrar Pokémon', font=('Calibri', 20), command=filtrar_pokemon, background='#FFD700', borderwidth=2, height=1)
botao1.grid(row=4, column=0, columnspan=3, sticky='nsew')

pokemon_escolhido = listasuspensa4.get()

botao2 = Button(text='Buscar Pokémon', font=('Calibri', 20), command=buscar_pokemon, background='#FFD700', borderwidth=2, height=1)
botao2.grid(row=6, column=0, columnspan=3, sticky='nsew')

#Visualização da janela
janela.mainloop()


# In[ ]:




