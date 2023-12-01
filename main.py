from flask import Flask, render_template, request, Response
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/proxy', methods=['GET', 'POST'])
def proxy():
    if request.method == 'POST':
        user_url = request.form.get('url')
    else:
        user_url = request.args.get('url')

    if not user_url:
        return "Erro: URL não fornecida."

    # Fazer uma requisição HTTP para a URL fornecida
    response = requests.get(user_url)

    # Verificar se a requisição foi bem-sucedida (código de status 200)
    if response.status_code == 200:
        # Encaminhar a resposta para o cliente
        return Response(response.content, content_type=response.headers['Content-Type'])

    else:
        return f'Erro ao acessar a URL. Código de status: {response.status_code}'

if __name__ == '__main__':
    app.run(debug=True)
