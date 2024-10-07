#importações
import requests
import json
from datetime import datetime


link = "https://pj1924-d36b2-default-rtdb.firebaseio.com/"

# Function Logs
def Horario():
    data = datetime.now().isoformat()
    return data

def Event_Log(conteudo, action):
    data = Horario()
    
    if action == "Delete":
        dados = {
            'created_at': data,
            'action' : action,
            'Content' : conteudo
        }
        requisicao = requests.post(f'{link}/Log/Delete/.json', data=json.dumps(dados))

    elif action == "Create":
        dados = {
            'created_at': data,
            'action' : action,
            'Content' : conteudo
        }
        requisicao = requests.post(f'{link}/Log/Create/.json', data=json.dumps(dados))

    elif action == "Likes":
        dados = {
            'created_at': data,
            'action' : action,
            'Content' : conteudo
        }
        requisicao = requests.post(f'{link}/Log/Likes/.json', data=json.dumps(dados))

    elif action == "Posts":
        dados = {
            'created_at': data,
            'action' : action,
            'Content' : conteudo
        }
        requisicao = requests.post(f'{link}/Log/Posts/.json', data=json.dumps(dados))

    elif action == "Comments":
        dados = {
            'created_at': data,
            'action' : action,
            'Content' : conteudo
        }
        requisicao = requests.post(f'{link}/Log/Comments/.json', data=json.dumps(dados))

# Gerar Id
def Gerar_Id():
    requisisao = requests.get(f'{link}/Ids/.json')
    consulta = requisisao.json()
    for id in consulta:
        Id = consulta['ID']
        break
    Id = Id + 1
    dado={
        'ID':Id
    }
    requisicao = requests.patch(f'{link}/Ids/.json', data=json.dumps(dado))
    return Id
    
# Criar Conta
def Creat_Account(nome, email, senha):

    id = Gerar_Id()

    data = Horario()
    dados1 = {
        'user_id':id,
        'username': nome,
        'email': email,
        'password_hash' : senha,
        'created_at' : data,
    }
    dados2 = {
        'profile_id':id,
        'user_id': id,
        'full_name': nome,
        'bio' : '',
        'profile_picture_url' : '',
        'birthdate' : '',
        'location' : ''
    }

    requisicao = requests.post(f'{link}/Users/.json', data=json.dumps(dados1))
    requisicao2 = requests.post(f'{link}/Profiles/.json', data=json.dumps(dados2))
    Event_Log(f"Conta Criada o id é {id}, e o nome é {nome}", "Create")

# Entrar na conta
def Enter_Cont(nomex):
    dados = 'https://pj1924-d36b2-default-rtdb.firebaseio.com/Users/.json'
    
    # Faz a requisição à URL especificada
    requisicao = requests.get(dados)
    
    # Converte a resposta JSON para um dicionário Python
    consulta = requisicao.json()
    
    # Inicializa uma variável para verificar se o nome foi encontrado
    encontrado = False
    
    # Itera sobre os itens do dicionário
    for nome, info in consulta.items():
        # Verifica se o nome procurado está presente e exibe a senha
        if info['username'] == nomex:
            senha = info['password_hash']
            encontrado = True
            break
    
    # Se o nome não foi encontrado, exibe "NAO TEM SENHA"
    if encontrado:
        return senha
    else:
        return False
    
# Function Exclusao De Conta
def Delete_Cont(id):
    nome_dicionario1 = None
    nome_dicionario2 = None

    requisicao = requests.get(f'{link}/Users/.json')
    consulta = requisicao.json()
    for chave, conteudo in consulta.items():
        if conteudo.get('user_id') == id:
            nome_dicionario1 = chave
            break
    
    # Procurando no Profiles
    requisicao = requests.get(f'{link}/Profiles/.json')
    consulta = requisicao.json()
    for chave, conteudo in consulta.items():
        if conteudo.get('user_id') == id:
            nome_dicionario2 = chave
            break
    
    if nome_dicionario1 and nome_dicionario2:
        requisisao = requests.delete(f'{link}/Users/{nome_dicionario1}/.json')
        requisisao = requests.delete(f'{link}/Profiles/{nome_dicionario2}/.json')
        Event_Log(f"Conta Excluida foi a {id}", "Delete")
    else:
        print("Conta não encontrada!")