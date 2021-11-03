import json
from datetime import datetime
import boto3

dynamodb = boto3.resource('dynamodb')

cadastrodb = dynamodb.Table('cadastrodb')


def lambda_handler(event, context):
    nome = "nome_usuario"
    sobrenome = "sobrenome_usuario"
    email = "email"
    senha = "senha_usuario"
    dataNasc = "data_nascimento"

    try:
        
        cadastrodb.put_item(
            Item={
                'email': email, # Chave de Partição  no Banco
                'nome' : nome,
                'sobrenome' : sobrenome,
                'senha' : senha,
                'dataNasc' : dataNasc
            }
        )

        return {
       
            'statusCode': 200,
            'body': json.dumps('Cadastrado com Sucesso')
        }

    except:
        print('Erro: lambda function terminada sem sucesso')
        return {
            'statusCode': 400,
            'body': json.dumps('Erro ao tentar inserir no BD')
        }
        