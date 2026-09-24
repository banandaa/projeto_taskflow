# importar, rotas e iniciar aplicação (ordem)

# importar  bibliotecas

from flask import Flask, render_template, request, flash
from sqlalchemy.exc import SQLAlchemyError

from models import Pessoa, db_session

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

@app.route('/criar_pessoa', methods=['GET', 'POST'])
def criar_pessoa():
    #verifica o metodo, se for get vai para a pagina do formulario
    if request.method == 'GET':
        return render_template('criar_pessoa.html')


    #recebe os dados do formulario via POST
    nome_form = request.form.get('form_nome')
    email_form = request.form.get('form_email')
    senha_form = request.form.get('form_senha')
    print(f'nome: {nome_form}, email: {email_form}, senha: {senha_form}')
    if not nome_form:
        flash('Preencha o nome', 'error')
        return render_template('criar_pessoa.html')

    try:
        #Cria uma nova pessoa e adiciona na base de dados
        nova_pessoa = Pessoa(nome_pessoa=nome_form, email_pessoa=email_form, senha_pessoa=senha_form)


        #inicializa a sessão com o banco de dados
        db_session.add(nova_pessoa)
        db_session.commit()
        print(f'{nova_pessoa}')
        return render_template('pessoa.html')
    except SQLAlchemyError as e:
        db_session.rollback() #reverte a transação em caso de erro
        print (f'Erro ao salvar pessoa no banco: {e}')
        flash('Erro ao salvar pessoa no banco', 'error')
        return render_template('criar_pessoa.html')
    except Exception as e:
        db_session.rollback()
        print(f'Espero inesperado: {e}')
        flash('Espero inesperado', 'error')
        return render_template('criar_pessoa.html')


###################################################################################################
# iniciar aplicação web

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)

# nada deve ser colocado abaixo
# debug apresenta erros e bugs de forma mais detalhada



