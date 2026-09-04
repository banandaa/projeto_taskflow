# importar, rotas e iniciar aplicação (ordem)

# importar  bibliotecas

from flask import Flask, render_template, request

###################################################################################################
# criar objeto flask "apelido - app"
app = Flask(__name__)

###################################################################################################
#base fake

base_fake = []

###################################################################################################
# rotas
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/atividades/criar', methods=['GET', 'POST'])
def criar_atividade():
    if request.method == 'POST':
        #aqui recebe dados do formulário
        nome_atividade = request.form.get('form_nome')
        data_atividade = request.form.get('form_data')
        descricao_atividade = request.form.get('form_descricao')
        categoria_atividade = request.form.get('form_categoria')
        prioridade_atividade = request.form.getlist('form_prio')

        dados = {
            'nome': nome_atividade,
            'data': data_atividade,
            'descricao': descricao_atividade,
            'categoria': categoria_atividade,
            'prioridade': prioridade_atividade,
        }

        print(f'dados cadastrados: {dados}')
        base_fake.append(dados)
        print(f'base_fake: {base_fake}')
        return render_template('listar_atividade.html', dados_atividade = base_fake)



    return render_template('criar_atividade.html')

@app.route('/atividades/listar')
def listar_atividade():
    return render_template('listar_atividade.html')

@app.route('/pessoa')
def pessoa():
    return render_template('pessoa.html')

###################################################################################################
# iniciar aplicação web

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)

# nada deve ser colocado abaixo
# debug apresenta erros e bugs de forma mais detalhada



