from flask import Flask, request, render_template
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

import re
import read_words

app = Flask(__name__)

# Armazenamento temporário de dados do usuário
user_sessions = {}

# Palavras-chave para restrição de conteúdo sensível
palavras_chave_sensiveis = read_words.read_txt()


# Função que susbstitui as palavras indesejadas
def substituir_palavras(html_content):
    # Usamos a bibilioteca BeautifulSoup para analisar o HTML
    soup = BeautifulSoup(html_content, 'html.parser')


    # Procuramos cada palavra do .txt dentro do HTML
    for palavra_sensivel in palavras_chave_sensiveis:
        # Verificamos e substituímos palavras específicas, se encontradas.
        for tag in soup.find_all(text=True):
            # Caso exista, substituímos pela string "***SENSIVEL***";
            # Utilizamos o .lower() para tratar somente com strings sem Uppercase (intuito de evitar erro ou mais verificações).
            if palavra_sensivel.lower() in tag.lower():
                print(f"Substituindo {palavra_sensivel} por ***SENSIVEL***")
                # Utilizamos  a função "replace_with" da biblioteca bs4 para substituir
                tag.replace_with(re.sub(re.escape(palavra_sensivel), '***SENSIVEL***', tag, flags=re.IGNORECASE))

    # Retornamos o HTML modificado
    return str(soup)

# Função que modifica os links 
def modificar_links(html, base_url):
    # Carrega o HTML e cria uma estrutura de árvore usando BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Encontra todas as tags 'a', 'link', 'script', 'img' no HTML
    tags = soup.find_all(['a', 'link', 'script', 'img'])

    # Para cada tag encontrada
    for tag in tags:
        # Para os atributos 'href' e 'src'
        for attr in ['href', 'src']:
            # Se o atributo existe na tag
            if attr in tag.attrs:
                # Transformamos 
                tag[attr] = urljoin(base_url, tag[attr])

                # Se a tag é uma âncora ('<a>'), adicionamos o link do proxy
                if tag.name == 'a':
                    tag[attr] = f"http://127.0.0.1:5000/proxy?idade={request.args.get('idade')}&url={tag[attr]}"

    # Converte a estrutura de árvore de volta para uma string HTML
    return str(soup)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/proxy')
def proxy():
    user_age = request.args.get('idade')
    user_url = request.args.get('url')

    # Seção do usuário
    if user_url:
        if user_age not in user_sessions:
            user_sessions[user_age] = {'current_url': user_url}
        else:
            user_sessions[user_age]['current_url'] = user_url

        response = requests.get(user_url)
        
        if int(user_age) < 18:
            casa = substituir_palavras(response.text)
        else:
            casa = response.text
        
        modified_content = modificar_links(casa, user_url)
        
        return modified_content

    return "Erro: URL não fornecida."

if __name__ == '__main__':
    app.run(debug=True)
