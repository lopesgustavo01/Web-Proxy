from flask import Flask, request, render_template
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

# Armazenamento temporário de dados do usuário
user_sessions = {}

# Palavras-chave para restrição de conteúdo sensível
palavras_chave_sensiveis = ['buceta', 'Bicha', 'palavra3']

def substituir_palavras(html_content):
    # Use BeautifulSoup para analisar o HTML
    soup = BeautifulSoup(html_content, 'html.parser')

    # Encontre e substitua palavras específicas (substitua 'palavra_antiga' por sua palavra)
    for tag in soup.find_all(text=True):
        tag.replace_with(tag.replace('html', 'drussa'))

    # Retorne o HTML modificado
    return str(soup)

def modificar_links(html, proxy_url):
    soup = BeautifulSoup(html, 'html.parser')
    links = soup.find_all('a')

    for link in links:
        link['href'] = f"{proxy_url}?url={link['href']}"

    return str(soup)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/proxy')
def proxy():
    user_age = request.args.get('idade')
    user_url = request.args.get('url')

    # Verificação de idade
    if int(user_age) < 18 and any(keyword in user_url for keyword in palavras_chave_sensiveis):
        return "Acesso restrito a conteúdo sensível."

    # Seção do usuário
    if user_url:
        if user_age not in user_sessions:
            user_sessions[user_age] = {'current_url': user_url}
        else:
            user_sessions[user_age]['current_url'] = user_url

        response = requests.get(user_url)
        casa = substituir_palavras(response.text)
        #modified_content = modificar_links(response.text, request.base_url)
        return casa

    return "Erro: URL não fornecida."

if __name__ == '__main__':
    app.run(debug=True)
