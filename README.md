<h1 align="center">
📄<br>README - Projeto Sistema Pokémon
</h1>

## Índice 

* [Descrição do Projeto](#descrição-do-projeto)
* [Funcionalidades e Demonstração da Aplicação](#funcionalidades-e-demonstração-da-aplicação)
* [Pré requisitos](#pré-requisitos)
* [Execução](#execução)
* [Bibliotecas](#bibliotecas)

# Descrição do projeto
> Este repositório é meu projeto Python de criação de sistema de escolha de Pokémon. O objetivo do projeto foi treinar várias áreas da programação em Python: automação web, criação de dicionário, exportação de base de dados, criação de sistema (janela interativa). Inicialmente, no arquivo "automacao_pokemon.py", por meio de automação web, informações de todos os mais de 1000 Pokémon, incluindo suas imagens, foram coletadas e armazenadas respectivamente em uma planilha Excel e em uma pasta "Revisão - Pokémon". Então, no arquivo "sistema_pokemon.py", a partir de um sistema interativo criado por meio de janela Tkinter, é possível escolher um Pokémon entre todos aqueles cujas informações e imagens foram coletados.

# Funcionalidades e Demonstração da Aplicação

Sistema Tkinter de escolha do Pokémon:<br>
![Screenshot_1](https://user-images.githubusercontent.com/128300382/228620970-312e6e97-85f4-467d-95ef-0436242cc84e.png)

## Pré requisitos

* Sistema operacional Windows
* IDE de python (ambiente de desenvolvimento integrado de python)
* Planilha com as informações dos Pokémon (arquivo Excel criado em "automacao_pokemon.py")
* Pasta com as imagens de todos os Pokémon (arquivos png criados em "automacao_pokemon.py")

## Execução

Primeiramente, deve-se executar o arquivo "automacao_pokemon.py", no qual todas as informações dos Pokémon serão exportados para uma planilha Excel, assim como suas respectivas imagens serão salvas em uma pasta "Revisão - Pokémon". Então, executa-se o arquivo "sistema_pokemon.py", o qual apresentará ao usuário a janela Tkinter interativa na qual pode-se escolher um Pokémon qualquer baseado em certos atributos: região, tipo primário e tipo secundário. O Pokémon escolhido aparecerá em uma nova janela Tkinter.

## Bibliotecas

* <strong>tkinter:</strong> biblioteca de criação e edição de janela interativa<br>
* <strong>pandas:</strong> bibliotecas de integração de arquivos excel, csv e outros, possibilitando análise de dados<br>
* <strong>selenium, webdriver_manager:</strong> bibliotecas que permitem a automação web (web-scrapping)<br>
* <strong>time:</strong> biblioteca que permite o gerenciamento do tempo na execução de certas linhas de código<br>
* <strong>PIL:</strong> biblioteca de integração de imagem<br>
* <strong>os, shutil:</strong> biblioteca de integração de arquivos e pastas do computador<br>
* <strong>pprint:</strong> biblioteca que permite uma melhor visualização de dicionários complexos<br>
* <strong>urllib.request:</strong> biblioteca que permite a digitação de textos em urls<br>
* <strong>io:</strong> biblioteca que permite a utilização de imagem<br>
